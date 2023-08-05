import abc
from typing import *

from kaiju_tools.serialization import Serializable
from kaiju_tools.exceptions import parse_base_exception, APIException

__all__ = (
    'JSONRPC',
    'RPCMessage',
    'RPCRequest',
    'RPCResponse',
    'RPCError',
    'InternalError',
    'InvalidParams',
    'JSONParseError',
    'MethodNotFound',
    'InvalidRequest',
    'RequestTimeout',
    'AbortedByServer',
    'ServerClosing',
    'PermissionDenied',
    'NotAuthorized',
)

JSONRPC = '2.0'  #: JSON RPC supported protocol version

# Base message classes


class RPCMessage(Serializable, abc.ABC):
    """Base RPC message class compatible with JSON serializer.

    :param id: message identifier
    """

    jsonrpc = JSONRPC

    __slots__ = ('id',)

    def __init__(self, id: Union[int, None]):
        self.id = id


class RPCRequest(RPCMessage):
    """Valid JSONRPC request.

    :param id: request ID (UUID), None for random uuid4 based integer
    :param method: RPC method or function name
    :param params: RPC method args (list for positional args, dict for kws)
    """

    __slots__ = ('id', 'method', 'params')

    def __init__(
        self, id: Union[int, None] = False, method: str = None, params: Union[list, dict] = None, jsonrpc=None
    ):

        if id is False:
            self.id = 0
        else:
            self.id = id
        if method is None:
            raise TypeError()
        self.method = method
        self.params = params

    def repr(self):
        return {'jsonrpc': JSONRPC, 'id': self.id, 'method': self.method, 'params': self.params}

    def __repr__(self):
        return str(self.repr())


class RPCResponse(RPCMessage):
    """Valid JSON RPC response.

    :param id: request ID (for correlation)
    :param result: RPC method call result
    """

    __slots__ = ('id', 'result')

    def __init__(self, id: Union[int, None], result: Any, jsonrpc=None):
        self.id = id
        self.result = result

    def repr(self):
        return {'jsonrpc': JSONRPC, 'id': self.id, 'result': self.result}

    def __repr__(self):
        return str(self.repr())


class RPCError(Exception, Serializable, abc.ABC):
    """JSON RPC error base class.

    :param id: request ID (for correlation) or None if it cannot be determined
    :param message: error human-readable message
    :param data: additional metadata, which will be stored in `error.data`
    :param base_exc: base python exception object, you can pass it to trace
        the error, the data will be stored in 'error.data["traceback"]'.
    :param debug: debug mode
    """

    code = 0  #: RPC error code
    exc_type = None

    __slots__ = ('id', 'message', 'data', 'base_exc', 'debug')

    def __init__(
        self,
        id: Union[int, None] = None,
        message: str = '',
        base_exc: Exception = None,
        debug: bool = False,
        data: dict = None,
        jsonrpc=None,
    ):
        self.id = id
        self.message = message
        self.base_exc = base_exc
        self.data = data if data else {}
        self.debug = debug

    def repr(self):
        data = {'type': self.exc_type if self.exc_type else self.__class__.__name__, **self.data}
        if self.base_exc:
            data.update(parse_base_exception(self.base_exc, debug=self.debug))
        result = {
            'jsonrpc': JSONRPC,
            'id': self.id,
            'error': {'code': self.code, 'message': self.message, 'data': data},
        }
        return result

    @classmethod
    def from_api_exception(cls, id: Union[int, None], exc: APIException, debug: bool = False, **data):
        exc.data.update(data)
        new_exc = cls(id=id, debug=debug, message=exc.message, base_exc=exc.base_exc, data=exc.data)
        new_exc.code = exc.status_code
        new_exc.exc_type = exc.__class__.__name__
        return new_exc

    def __repr__(self):
        return str(self.repr())


# Standard JSON RPC errors


class JSONParseError(RPCError):
    """Error is raised when a server can't decode a request JSON body.

    :param id: request ID (for correlation) or None if it cannot be determined
    :param data: additional metadata, which will be stored in `error.data`
    :param base_exc: base python exception object, you can pass it to trace
    the error, the data will be stored in 'error.data["traceback"]'.
    :param debug: debug mode
    """

    code = -32700  #: RPC error code

    __slots__ = ('id', 'message', 'data', 'debug', 'base_exc')

    def __init__(
        self,
        id: Union[int, None] = None,
        base_exc: Exception = None,
        debug: bool = False,
        data: dict = None,
        message=None,
        jsonrpc=None,
    ):
        super().__init__(id, 'JSON Parse Error.', base_exc=base_exc, debug=debug, data=data)


class InvalidRequest(RPCError):
    """Error is raised whenever request format is invalid.

    :param id: request ID (for correlation) or None if it cannot be determined
    :param data: additional metadata, which will be stored in `error.data`
    :param base_exc: base python exception object, you can pass it to trace
    the error, the data will be stored in 'error.data["traceback"]'.
    :param debug: debug mode
    """

    code = -32600  #: RPC error code

    __slots__ = ('id', 'message', 'data', 'debug', 'base_exc')

    def __init__(
        self,
        id: Union[int, None] = None,
        base_exc: Exception = None,
        debug: bool = False,
        data: dict = None,
        message=None,
        jsonrpc=None,
    ):
        super().__init__(id, 'Invalid request.', base_exc=base_exc, debug=debug, data=data)


class MethodNotFound(RPCError):
    """RPC server doesn't have a registered method with name specified in a request.

    :param id: request ID (for correlation) or None if it cannot be determined
    :param data: additional metadata, which will be stored in `error.data`
    :param base_exc: base python exception object, you can pass it to trace
    the error, the data will be stored in 'error.data["traceback"]'.
    :param debug: debug mode
    """

    code = -32601  #: RPC error code

    __slots__ = ('id', 'message', 'data', 'debug', 'base_exc')

    def __init__(
        self,
        id: Union[int, None] = None,
        base_exc: Exception = None,
        debug: bool = False,
        data: dict = None,
        message=None,
        jsonrpc=None,
    ):
        super().__init__(id, 'Method not found.', base_exc=base_exc, debug=debug, data=data)


class InvalidParams(RPCError):
    """RPC server method can't proceed with the provided request params.

    :param id: request ID (for correlation) or None if it cannot be determined
    :param data: additional metadata, which will be stored in `error.data`
    :param base_exc: base python exception object, you can pass it to trace
        the error, the data will be stored in 'error.data["traceback"]'.
    :param debug: debug mode
    """

    code = -32602  #: RPC error code

    __slots__ = ('id', 'message', 'data', 'debug', 'base_exc')

    def __init__(
        self,
        id: Union[int, None] = None,
        base_exc: Exception = None,
        debug: bool = False,
        data: dict = None,
        message=None,
        jsonrpc=None,
    ):
        super().__init__(id, 'Invalid request params.', base_exc=base_exc, debug=debug, data=data)


class InternalError(RPCError):
    """Internal RPC method error has occurred.

    :param id: request ID (for correlation) or None if it cannot be determined
    :param data: additional metadata, which will be stored in `error.data`
    :param base_exc: base python exception object, you can pass it to trace
    the error, the data will be stored in 'error.data["traceback"]'.
    :param debug: debug mode
    """

    code = -32603  #: RPC error code

    __slots__ = ('id', 'message', 'data', 'debug', 'base_exc')

    def __init__(
        self,
        id: Union[int, None] = None,
        base_exc: Exception = None,
        debug: bool = False,
        data: dict = None,
        message=None,
        jsonrpc=None,
    ):
        super().__init__(id, 'Internal server error.', base_exc=base_exc, debug=debug, data=data)


class RequestTimeout(RPCError):
    """Error is raised whenever request execution deadline is reached.

    :param id: request ID (for correlation) or None if it cannot be determined
    :param data: additional metadata, which will be stored in `error.data`
    :param base_exc: base python exception object, you can pass it to trace
    the error, the data will be stored in 'error.data["traceback"]'.
    :param debug: debug mode
    """

    code = 408  #: The error code is not specified in the original JSON RPC spec

    __slots__ = ('id', 'message', 'data', 'debug', 'base_exc')

    def __init__(
        self,
        id: Union[int, None] = None,
        base_exc: Exception = None,
        debug: bool = False,
        data: dict = None,
        message=None,
        jsonrpc=None,
    ):
        super().__init__(id, 'Request execution deadline.', base_exc=base_exc, debug=debug, data=data)


class AbortedByServer(RPCError):
    """Execution aborted by the server."""

    code = 418
    __slots__ = tuple()


class ServerClosing(RPCError):
    """Indicates that the RPC server is stopping and won't handle new requests.

    :param id: request ID (for correlation) or None if it cannot be determined
    :param data: additional metadata, which will be stored in `error.data`
    :param base_exc: base python exception object, you can pass it to trace
    the error, the data will be stored in 'error.data["traceback"]'.
    :param debug: debug mode
    """

    code = 503  #: The error code is not specified in the original JSON RPC spec

    __slots__ = ('id', 'message', 'data', 'debug', 'base_exc')

    def __init__(
        self,
        id: Union[int, None] = None,
        base_exc: Exception = None,
        debug: bool = False,
        data: dict = None,
        message=None,
        jsonrpc=None,
    ):
        super().__init__(id, 'Server is closing.', base_exc=base_exc, debug=debug, data=data)


class PermissionDenied(RPCError):
    """Indicates that the RPC server doesn't allow the method execution for this particular user.

    :param id: request ID (for correlation) or None if it cannot be determined
    :param data: additional metadata, which will be stored in `error.data`
    :param base_exc: base python exception object, you can pass it to trace
    the error, the data will be stored in 'error.data["traceback"]'.
    :param debug: debug mode
    """

    code = 403  #: The error code is not specified in the original JSON RPC spec

    __slots__ = ('id', 'message', 'data', 'debug', 'base_exc')

    def __init__(
        self,
        id: Union[int, None] = None,
        base_exc: Exception = None,
        debug: bool = False,
        data: dict = None,
        message=None,
        jsonrpc=None,
    ):
        super().__init__(id, 'Permission denied.', base_exc=base_exc, debug=debug, data=data)


class NotAuthorized(RPCError):
    """Indicates that the RPC server doesn't allow the method execution because the user is not authenticated.

    :param id: request ID (for correlation) or None if it cannot be determined
    :param data: additional metadata, which will be stored in `error.data`
    :param base_exc: base python exception object, you can pass it to trace
    the error, the data will be stored in 'error.data["traceback"]'.
    :param debug: debug mode
    """

    code = 401  #: The error code is not specified in the original JSON RPC spec

    __slots__ = ('id', 'message', 'data', 'debug', 'base_exc')

    def __init__(
        self,
        id: Union[int, None] = None,
        base_exc: Exception = None,
        debug: bool = False,
        data: dict = None,
        message=None,
        jsonrpc=None,
    ):
        super().__init__(id, 'Not authorized.', base_exc=base_exc, debug=debug, data=data)
