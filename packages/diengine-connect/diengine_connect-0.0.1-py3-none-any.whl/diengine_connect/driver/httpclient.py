import json
import logging
import os
import re
import uuid
from base64 import b64encode
from typing import Optional, Dict, Any, Sequence, Union, List, Callable, Generator, BinaryIO

from urllib3 import Timeout
from urllib3.exceptions import HTTPError
from urllib3.poolmanager import PoolManager
from urllib3.response import HTTPResponse

from diengine_connect import common
from diengine_connect.datatypes import registry
from diengine_connect.datatypes.base import ClickHouseType
from diengine_connect.driver.client import Client
from diengine_connect.driver.common import dict_copy, coerce_bool, coerce_int
from diengine_connect.driver.compression import available_compression
from diengine_connect.driver.exceptions import DatabaseError, OperationalError, ProgrammingError
from diengine_connect.driver.httputil import ResponseSource, get_pool_manager, get_response_data, \
    default_pool_manager, get_proxy_manager, all_managers
from diengine_connect.driver.insert import InsertContext
from diengine_connect.driver.query import QueryResult, QueryContext, quote_identifier, bind_query
from diengine_connect.driver.transform import NativeTransform

logger = logging.getLogger(__name__)
columns_only_re = re.compile(r'LIMIT 0\s*$', re.IGNORECASE)


# pylint: disable=too-many-instance-attributes
class HttpClient(Client):
    params = {}
    valid_transport_settings = {'database', 'buffer_size', 'session_id',
                                'compress', 'decompress', 'session_timeout',
                                'session_check', 'query_id', 'quota_key',
                                'wait_end_of_query', 'client_protocol_version'}
    optional_transport_settings = {'send_progress_in_http_headers',
                                   'http_headers_progress_interval_ms',
                                   'enable_http_compression'}
    _owns_pool_manager = False

    # pylint: disable=too-many-arguments,too-many-locals,too-many-branches,too-many-statements,unused-argument
    def __init__(self,
                 interface: str,
                 host: str,
                 port: int,
                 username: str,
                 password: str,
                 database: str,
                 compress: Union[bool, str] = True,
                 query_limit: int = 0,
                 query_retries: int = 2,
                 connect_timeout: int = 10,
                 send_receive_timeout: int = 300,
                 client_name: Optional[str] = None,
                 send_progress: bool = True,
                 verify: bool = True,
                 ca_cert: Optional[str] = None,
                 client_cert: Optional[str] = None,
                 client_cert_key: Optional[str] = None,
                 session_id: Optional[str] = None,
                 settings: Optional[Dict[str, Any]] = None,
                 pool_mgr: Optional[PoolManager] = None,
                 http_proxy: Optional[str] = None,
                 https_proxy: Optional[str] = None,
                 server_host_name: Optional[str] = None):
        """
        Create an HTTP ClickHouse Connect client
        See diengine_connect.get_client for parameters
        """
        self.url = f'{interface}://{host}:{port}/api/engine/v1/sql/superset'
        self.headers = {}
        ch_settings = settings or {}
        self.http = pool_mgr
        if interface == 'https':
            if not https_proxy and 'HTTPS_PROXY' in os.environ:
                https_proxy = os.environ['HTTPS_PROXY']
            if client_cert:
                if not username:
                    raise ProgrammingError('username parameter is required for Mutual TLS authentication')
                self.headers['X-ClickHouse-User'] = username
                self.headers['X-ClickHouse-SSL-Certificate-Auth'] = 'on'
            verify = coerce_bool(verify)
            # pylint: disable=too-many-boolean-expressions
            if not self.http and (server_host_name or ca_cert or client_cert or not verify or https_proxy):
                options = {
                    'ca_cert': ca_cert,
                    'client_cert': client_cert,
                    'verify': verify,
                    'client_cert_key': client_cert_key
                }
                if server_host_name:
                    if verify:
                        options['assert_hostname'] = server_host_name
                    options['server_hostname'] = server_host_name
                self.http = get_pool_manager(https_proxy=https_proxy, **options)
                self._owns_pool_manager = True
        if not self.http:
            if not http_proxy and 'HTTP_PROXY' in os.environ:
                http_proxy = os.environ['HTTP_PROXY']
            if http_proxy:
                self.http = get_proxy_manager(host, http_proxy)
            else:
                self.http = default_pool_manager

        if not client_cert and username:
            self.headers['Authorization'] = 'Basic ' + b64encode(f'{username}:{password}'.encode()).decode()
        self.headers['User-Agent'] = common.build_client_name(client_name)
        self._read_format = self._write_format = 'Native'
        self._transform = NativeTransform()
        self._server_host_name = server_host_name

        connect_timeout, send_receive_timeout = coerce_int(connect_timeout), coerce_int(send_receive_timeout)
        self.timeout = Timeout(connect=connect_timeout, read=send_receive_timeout)
        self.query_retries = coerce_int(query_retries)
        self.http_retries = 1
        self._send_progress = None
        self._send_comp_header = False
        self._progress_interval = None

        if session_id:
            ch_settings['session_id'] = session_id
        elif 'session_id' not in ch_settings and common.get_setting('autogenerate_session_id'):
            ch_settings['session_id'] = str(uuid.uuid1())

        if coerce_bool(compress):
            compression = ','.join(available_compression)
            self.write_compression = available_compression[0]
        elif compress and compress not in ('False', 'false', '0'):
            if compress not in available_compression:
                raise ProgrammingError(f'Unsupported compression method {compress}')
            compression = compress
            self.write_compression = compress
        else:
            compression = None

        super().__init__(database=database, uri=self.url, query_limit=coerce_int(query_limit))
        self.params = self._validate_settings(ch_settings)
        comp_setting = self._setting_status('enable_http_compression')
        self._send_comp_header = not comp_setting.is_set and comp_setting.is_writable
        if comp_setting.is_set or comp_setting.is_writable:
            self.compression = compression
        send_setting = self._setting_status('send_progress_in_http_headers')
        self._send_progress = not send_setting.is_set and send_setting.is_writable
        if (send_setting.is_set or send_setting.is_writable) and \
                self._setting_status('http_headers_progress_interval_ms').is_writable:
            self._progress_interval = str(min(120000, (send_receive_timeout - 5) * 1000))

    def set_client_setting(self, key, value):
        str_value = self._validate_setting(key, value, common.get_setting('invalid_setting_action'))
        if str_value is not None:
            self.params[key] = str_value

    def get_client_setting(self, key) -> Optional[str]:
        values = self.params.get(key)
        return values[0] if values else None

    def _prep_query(self, context: QueryContext):
        final_query = super()._prep_query(context)
        # if context.is_insert:
        #     return final_query
        # return f'{final_query}\n FORMAT {self._write_format}'
        return final_query

    def _query_with_context(self, context: QueryContext) -> QueryResult:
        headers = {'Content-Type': 'text/plain; charset=utf-8'}
        params = {}
        if self.database:
            params['database'] = self.database
        if self.protocol_version:
            params['client_protocol_version'] = self.protocol_version
            context.block_info = True
        params.update(context.bind_params)
        params.update(self._validate_settings(context.settings))
        if columns_only_re.search(context.uncommented_query):
            response = self._raw_request(f'{context.final_query}\n FORMAT JSON',
                                         params, headers, retries=self.query_retries)
            json_result = json.loads(response.data)
            # ClickHouse will respond with a JSON object of meta, data, and some other objects
            # We just grab the column names and column types from the metadata sub object
            names: List[str] = []
            types: List[ClickHouseType] = []
            for col in json_result['meta']:
                names.append(col['name'])
                types.append(registry.get_from_name(col['type']))
            return QueryResult([], None, tuple(names), tuple(types))

        if self.compression:
            headers['Accept-Encoding'] = self.compression
            if self._send_comp_header:
                params['enable_http_compression'] = '1'
        response = self._raw_request(self._prep_query(context),
                                     params,
                                     headers,
                                     stream=True,
                                     retries=self.query_retries,
                                     server_wait=not context.streaming)
        
        data = json.loads(response.data)
        query_result = self._transform.diengine_pares_response(data)
        
        # byte_source = RespBuffCls(ResponseSource(response))  # pylint: disable=not-callable
        # query_result = self._transform.parse_response(byte_source, context)
        if 'X-ClickHouse-Summary' in response.headers:
            try:
                summary = json.loads(response.headers['X-ClickHouse-Summary'])
                query_result.summary = summary
            except json.JSONDecodeError:
                pass
        query_result.query_id = response.headers.get('X-ClickHouse-Query-Id')
        return query_result

    def data_insert(self, context: InsertContext):
        """
        See BaseClient doc_string for this method
        """
        if context.empty:
            logger.debug('No data included in insert, skipping')
            return
        if context.compression is None:
            context.compression = self.write_compression
        block_gen = self._transform.build_insert(context)

        def error_handler(response: HTTPResponse):
            # If we actually had a local exception when building the insert, throw that instead
            if context.insert_exception:
                ex = context.insert_exception
                context.insert_exception = None
                raise ProgrammingError('Internal serialization error.  This usually indicates invalid data types ' +
                                       'in an inserted row or column') from ex  # type: ignore
            self._error_handler(response)

        self.raw_insert(context.table,
                        context.column_names,
                        block_gen,
                        context.settings,
                        self._write_format,
                        context.compression,
                        error_handler)
        context.data = None

    def raw_insert(self, table: str,
                   column_names: Optional[Sequence[str]] = None,
                   insert_block: Union[str, bytes, Generator[bytes, None, None], BinaryIO] = None,
                   settings: Optional[Dict] = None,
                   fmt: Optional[str] = None,
                   compression: Optional[str] = None,
                   status_handler: Optional[Callable] = None):
        """
        See BaseClient doc_string for this method
        """
        write_format = fmt if fmt else self._write_format
        headers = {'Content-Type': 'application/octet-stream'}
        if compression:
            headers['Content-Encoding'] = compression
        cols = f" ({', '.join([quote_identifier(x) for x in column_names])})" if column_names is not None else ''
        params = {'query': f'INSERT INTO {table}{cols} FORMAT {write_format}'}
        if self.database:
            params['database'] = self.database
        params.update(self._validate_settings(settings or {}))
        response = self._raw_request(insert_block, params, headers, error_handler=status_handler)
        logger.debug('Insert response code: %d, content: %s', response.status, response.data)

    def command(self,
                cmd,
                parameters: Optional[Union[Sequence, Dict[str, Any]]] = None,
                data: Union[str, bytes] = None,
                settings: Optional[Dict] = None,
                use_database: int = True) -> Union[str, int, Sequence[str]]:
        """
        See BaseClient doc_string for this method
        """
        cmd, params = bind_query(cmd, parameters, self.server_tz)
        headers = {}
        payload = None
        if isinstance(data, str):
            headers['Content-Type'] = 'text/plain; charset=utf-8'
            payload = data.encode()
        elif isinstance(data, bytes):
            headers['Content-Type'] = 'application/octet-stream'
            payload = data
        if payload is None:
            if not cmd:
                raise ProgrammingError('Command sent without query or recognized data') from None
            payload = cmd
        elif cmd:
            params['query'] = cmd
        if use_database and self.database:
            params['database'] = self.database
        params.update(self._validate_settings(settings or {}))
        method = 'POST' if payload else 'GET'
        response = self._raw_request(payload, params, headers, method)
        result = json.loads(response.data)['data']
        # result = response.data.decode()[:-1].split('\t')
        # if len(result) == 1:
        #     try:
        #         return int(result[0])
        #     except ValueError:
        #         return result[0]
        return result

    def _error_handler(self, response: HTTPResponse, retried: bool = False) -> None:
        err_str = f'HTTPDriver for {self.url} returned response code {response.status})'
        err_content = get_response_data(response)
        if err_content:
            err_msg = err_content.decode(errors='backslashreplace')
            logger.error(err_msg)
            err_str = f':{err_str}\n {err_msg[0:240]}'
        raise OperationalError(err_str) if retried else DatabaseError(err_str) from None

    def _raw_request(self,
                     data,
                     params: Dict[str, str],
                     headers: Optional[Dict[str, Any]] = None,
                     method: str = 'POST',
                     retries: int = 0,
                     stream: bool = False,
                     server_wait: bool = True,
                     error_handler: Callable = None) -> HTTPResponse:
        if isinstance(data, str):
            data = data.encode()
        # headers = dict_copy(self.headers, headers)
        attempts = 0
        if server_wait:
            params['wait_end_of_query'] = '1'
        # We can't actually read the progress headers, but we enable them so ClickHouse sends something
        # to keep the connection alive when waiting for long-running queries and (2) to get summary information
        # if not streaming
        if self._send_progress:
            params['send_progress_in_http_headers'] = '1'
        if self._progress_interval:
            params['http_headers_progress_interval_ms'] = self._progress_interval
        url = f'{self.url}'
        headers['Content-Type'] = 'application/json'
        headers['authorization'] = 'init'
        kwargs = {
            'headers': headers,
            'timeout': self.timeout,
            'body': data,
            'retries': self.http_retries,
            'preload_content': not stream
        }
        if self._server_host_name:
            kwargs['assert_same_host'] = False
            kwargs['headers'].update({'Host': self._server_host_name})
        while True:
            attempts += 1
            try:
                response: HTTPResponse = self.http.request(method, url, **kwargs)
            except HTTPError as ex:
                if isinstance(ex.__context__, ConnectionResetError):
                    # The server closed the connection, probably because the Keep Alive has expired
                    # We should be safe to retry, as ClickHouse should not have processed anything on a connection
                    # that it killed.  We also only retry this once, as multiple disconnects are unlikely to be
                    # related to the Keep Alive settings
                    if attempts == 1:
                        logger.debug('Retrying remotely closed connection')
                        continue
                logger.exception('Unexpected Http Driver Exception')
                raise OperationalError(f'Error {ex} executing HTTP request {self.url}') from ex
            if 200 <= response.status < 300:
                return response
            if response.status in (429, 503, 504):
                if attempts > retries:
                    self._error_handler(response, True)
                logger.debug('Retrying requests with status code %d', response.status)
            else:
                if error_handler:
                    error_handler(response)
                self._error_handler(response)

    def ping(self):
        """
        See BaseClient doc_string for this method
        """
        try:
            response = self.http.request('GET', f'{self.url}/ping', timeout=3)
            return 200 <= response.status < 300
        except HTTPError:
            logger.debug('ping failed', exc_info=True)
            return False

    def raw_query(self,
                  query: str,
                  parameters: Optional[Union[Sequence, Dict[str, Any]]] = None,
                  settings: Optional[Dict[str, Any]] = None,
                  fmt: str = None,
                  use_database: bool = True) -> bytes:
        """
        See BaseClient doc_string for this method
        """
        final_query, bind_params = bind_query(query, parameters, self.server_tz)
        if fmt:
            final_query += f'\n FORMAT {fmt}'
        params = self._validate_settings(settings or {})
        if use_database and self.database:
            params['database'] = self.database
        params.update(bind_params)
        return self._raw_request(final_query, params).data

    def close(self):
        if self._owns_pool_manager:
            self.http.clear()
            all_managers.remove(self.http)
