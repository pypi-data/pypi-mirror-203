import abc
import uuid
from typing import *

from kaiju_tools.http import HTTPService
from kaiju_tools.types import REQUEST_CONTEXT
from . import jsonrpc
from .abc import AbstractRPCCompatible, AbstractTokenInterface
from .etc import JSONRPCHeaders
from ..mapping import get_field, set_field
from ..exceptions import APIException, ensure_traceback
from ..services import ContextableService

__all__ = ('RPCClientError', 'RPCClientService', 'BaseRPCClientService')


class RPCClientError(APIException):
    """JSON RPC Python exception class."""

    def __init__(self, *args, response=None, **kws):
        super().__init__(*args, **kws)
        self.response = response

    def __str__(self):
        return self.message


class BaseRPCClientService(ContextableService, abc.ABC):
    """Abstract RPC client service.

    To configure the client for your own transport you must set your own
    `init_session` and `close_session` and `rpc_request` methods.

    :param app: web app
    :param uri: RPC service default endpoint
    :param logger: logger instance
    """

    service_name = 'client'
    token_service_class = AbstractTokenInterface
    headers = JSONRPCHeaders

    def __init__(self, app, uri: str = '/rpc', logger=None):
        super().__init__(app=app, logger=logger)
        self._uri = uri

    async def init(self):
        pass

    @classmethod
    def _process_response_batch(cls, batch: List[dict], unpack_response: bool):
        errors, responses = [], []
        for n, data in enumerate(batch):
            response = cls._process_response(data, unpack_response)
            if isinstance(response, jsonrpc.RPCError):
                errors.append((n, response))
            responses.append(response)
        return errors, responses

    @staticmethod
    def _process_response(response: dict, unpack_response: bool):
        if 'error' in response:
            error = response['error']
            error_type = error.get('data', {}).get('type', jsonrpc.RPCError.__name__)
            error_type = getattr(jsonrpc, error_type, jsonrpc.RPCError)
            response = error_type(id=response['id'], data=error)
        else:
            response = jsonrpc.RPCResponse(**response)
            if unpack_response:
                response = response.result
        return response

    def _log_rpc_error(self, url, headers, request, error):
        def _get_exc_type(response):
            #: TODO стандартизировать ошибки
            base_exc = response['error'].get('data', {}).get('data', {}).get('base_exc_type')
            if not base_exc:
                base_exc = response['error'].get('data', {}).get('data', {}).get('type')
            if not base_exc:
                base_exc = str(error.__class__.__qualname__)
            return base_exc

        def _get_code(response):
            code = response.get('code')
            if not code:
                code = response['error'].get('data', {}).get('code')
            return code

        error = ensure_traceback(error)
        request = request.repr()
        response = error.repr()
        base_exc = _get_exc_type(response)
        code = _get_code(response)
        t = type(f'{request["method"]}_{base_exc}'.replace('.', '_'), (), {})
        extra = {
            'fingerprint': ['rpc_client', request['method'], code, base_exc],
            'capturer': 'rpc_client',
            'request': {'method': 'POST', 'url': url, 'headers': headers, 'body': request},
            'response': {'status': response['error']['code'], 'body': response},
        }
        self.logger.error(error, extra=extra, exc_info=(t, error, error.__traceback__))

    @staticmethod
    def _set_headers(headers: Optional[dict]) -> dict:
        """Write an auth token to the headers if required."""
        if headers is None:
            headers = {}
        ctx = REQUEST_CONTEXT.get()
        if ctx:
            if ctx['correlation_id']:
                headers[JSONRPCHeaders.CORRELATION_ID_HEADER] = ctx['correlation_id']
            # if ctx['request_deadline']:
            #     headers[JSONRPCHeaders.REQUEST_DEADLINE_HEADER] = ctx['request_deadline']
        return headers


class RPCClientService(BaseRPCClientService, AbstractRPCCompatible):
    """RPC client."""

    transport_service_class = HTTPService

    def __init__(self, *args, transport: Union[str, transport_service_class], **kws):
        super().__init__(*args, **kws)
        self._transport = self.discover_service(transport, cls=self.transport_service_class)

    @property
    def routes(self) -> dict:
        return {'call': self.call}

    @property
    def permissions(self) -> dict:
        return {'*': self.PermissionKeys.GLOBAL_SYSTEM_PERMISSION}

    async def iter_call(
        self,
        method: str,
        params: Any = None,
        headers: dict = None,
        offset: int = 0,
        limit: int = 10,
        count_key='count',
        offset_key='offset',
        limit_key='limit',
        raise_exception=True,
        unpack_response=True,
    ) -> AsyncGenerator:
        """Iterate over data."""
        count = offset + 1

        if params is None:
            params = {}

        while count > offset:
            set_field(params, offset_key, offset)
            set_field(params, limit_key, limit)
            headers = self._set_headers(headers)
            data = await self.call(
                method=method,
                params=params,
                headers=headers,
                raise_exception=raise_exception,
                unpack_response=unpack_response,
            )
            if type(data) is jsonrpc.RPCResponse:
                count = get_field(data.result, count_key, default=0)
            elif isinstance(data, jsonrpc.RPCError):
                count = 0
            else:
                count = get_field(data, count_key, default=0)
            yield data

            offset += limit

    async def call(
        self,
        method: str,
        params: Any = None,
        id=False,
        headers: dict = None,
        uri: str = None,
        raise_exception=True,
        unpack_response=True,
    ) -> Union[jsonrpc.RPCResponse, jsonrpc.RPCError, dict]:
        """Call a single remote RPC method.

        :param method: RPC method name
        :param params: any RPC parameters
        :param headers: headers, see `kaiju.rpc.spec` for a list of available
            headers
        :param id: optional request id
        :param raise_exception: if True, then it will rise an exception if
            any errors have been returned
        :param unpack_response: if True, then in case of valid response
            not RPCResponse objects but actual result data will be returned

        :raises RPCException: if `raise_exception` was set to True and errors
        have been returned
        """
        if uri is None:
            uri = self._uri
        request = jsonrpc.RPCRequest(id, method, params)
        headers = self._set_headers(headers)
        response = await self._transport.request('post', uri, json=request.repr(), headers=headers)
        response = self._process_response(response, unpack_response=unpack_response)
        if isinstance(response, jsonrpc.RPCError) and raise_exception:
            url = self._transport.resolve(uri)
            self._log_rpc_error(url, headers, request, response)
            raise RPCClientError(str(response), response=response)
        else:
            return response

    async def call_multiple(
        self, *requests: dict, headers: dict = None, uri: str = None, raise_exception=True, unpack_response=True
    ):
        """Call multiple remote RPC methods in a single batch.

        :param requests: list of request objects (see `JSONRPCHTTPClient.call`
            for each request parameters)
        :param headers: headers, see `kaiju.rpc.spec` for a list of available
            headers
        :param raise_exception: if True, then it will rise an exception if
            any errors have been returned
        :param unpack_response: if True, then in case of valid response
            not RPCResponse objects but actual result data will be returned

        :raises RPCException: if `raise_exception` was set to True and errors
            have been returned
        """
        if uri is None:
            uri = self._uri
        request = [jsonrpc.RPCRequest(**data).repr() for data in requests]
        headers = self._set_headers(headers)
        response = await self._transport.request('post', uri, json=request, headers=headers)
        errors, responses = self._process_response_batch(response, unpack_response=unpack_response)
        if errors and raise_exception:
            url = self._transport.resolve(uri)
            for n, error in errors:
                self._log_rpc_error(url, headers, request[n], error)
            raise RPCClientError(str(error), response=error)
        else:
            return response
