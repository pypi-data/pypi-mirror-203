import sys
import traceback
import types
from typing import Union

from aiohttp.client import ClientResponseError
from fastjsonschema import JsonSchemaException

from kaiju_tools.serialization import Serializable

__all__ = [
    'parse_base_exception',
    'ensure_traceback',
    'APIException',
    'InternalError',
    'ClientError',
    'ValidationError',
    'NotFound',
    'ServerUnavailableError',
    'MethodNotAllowed',
    'Conflict',
    'JSONParseError',
    'PermissionDenied',
    'NotAuthorized',
    'PartiallySucceeded',
    'InvalidLicense',
]


def ensure_traceback(exc: Exception):
    """Add an empty traceback to the exception which points at this line of code."""
    if exc.__traceback__:
        return exc
    tb = None
    base_exc = getattr(exc, 'base_exc')
    if base_exc and base_exc.__traceback__:
        tb = base_exc.__traceback__
    if not tb:
        frame = sys._getframe(0)
        tb = types.TracebackType(None, frame, frame.f_lasti, frame.f_lineno)  # artificial traceback
    return exc.with_traceback(tb)


def parse_base_exception(base_exc: Exception, debug: bool = False) -> dict:
    data = {'base_exc_type': base_exc.__class__.__name__}
    data['base_exc_data'] = base_exc_data = getattr(base_exc, 'extras', {})
    if isinstance(base_exc, JsonSchemaException):
        base_exc_data.update(
            {
                'definition': base_exc.definition,
                'name': base_exc.name,
                'path': base_exc.path,
                'rule': base_exc.rule,
                'rule_definition': base_exc.rule_definition,
                'value': base_exc.value,
            }
        )
    elif isinstance(base_exc, ClientResponseError):
        base_exc_data.update({'status': base_exc.status})
        if debug:
            base_exc_data.update(
                {
                    'method': str(base_exc.request_info.method),
                    'url': str(base_exc.request_info.url),
                    'params': getattr(base_exc, 'params', None),
                    'took_ms': getattr(base_exc, 'took_ms', None),
                    'request': getattr(base_exc, 'request', None),
                    'response': getattr(base_exc, 'response', None),
                }
            )
    # if debug:
    #     tb = traceback.TracebackException.from_exception(base_exc)
    #     stack = [
    #         {'filename': frame.filename, 'lineno': frame.lineno, 'name': frame.name, 'line': frame.line}
    #         for frame in tb.stack
    #     ]
    #     data['traceback'] = stack
    return data


class APIException(Serializable, Exception):
    """Base exception class.

    Also see :class:`.Serializable`.

    :param message: user friendly message or message template
    :param code: app friendly error code string, which can be used for localization
        or in error processing, by default code will be identical to `status_code` value
    :param extras: any other information you want to provide
    """

    __slots__ = ('message', 'status', 'data', 'id', 'debug', 'base_exc')

    status_code = 500

    def __init__(
        self,
        message: str = '',
        id: Union[int, None] = None,
        base_exc: Exception = None,
        debug: bool = False,
        data: dict = None,
        **extras,
    ):
        """Initialize."""
        self.id = id
        self.message = message
        self.base_exc = base_exc
        self.data = data if data else {}
        self.data.update(extras)
        self.debug = debug

    def __str__(self):
        return self.message

    def repr(self) -> dict:
        data = {'code': self.status_code, 'message': self.message, 'data': {'type': self.__class__.__name__}}
        if self.base_exc:
            base_exc_data = parse_base_exception(self.base_exc, debug=self.debug)
            data['data'].update(base_exc_data)
        data['data'].update(self.data)
        return data


class PartiallySucceeded(APIException):
    """Partially succeeded request (in case of bulk operations)."""

    status_code = 200
    __slots__ = APIException.__slots__


class ClientError(APIException):
    """Any kind of error happened because of a client's actions."""

    status_code = 400
    __slots__ = APIException.__slots__


class JSONParseError(ClientError, ValueError):
    """Wrongly formatted JSON data."""

    status_code = 400
    __slots__ = ClientError.__slots__


class NotAuthorized(ClientError):
    """Authorization required."""

    status_code = 401
    __slots__ = ClientError.__slots__


class PermissionDenied(ClientError):
    """User has no rights to make current request."""

    status_code = 403
    __slots__ = ClientError.__slots__


class NotFound(ClientError):
    """Requested object or resource doesn't exist."""

    status_code = 404
    __slots__ = ClientError.__slots__


class MethodNotAllowed(ClientError):
    """Method or route is not allowed due to the app/method limitations."""

    status_code = 405
    __slots__ = ClientError.__slots__


class Conflict(ClientError):
    """New object/data is in conflict with existing."""

    status_code = 409
    __slots__ = ClientError.__slots__


class ValidationError(ClientError):
    """Correctly formatted data containing invalid values."""

    status_code = 422
    __slots__ = ClientError.__slots__


class FailedDependency(APIException):
    status_code = 424
    __slots__ = APIException.__slots__


class InternalError(APIException):
    """Any internal error happened on the server and not caused by a client."""

    status_code = 500
    __slots__ = APIException.__slots__


class ServerUnavailableError(InternalError):
    """External service is unavailable."""

    status_code = 503
    __slots__ = InternalError.__slots__


class InvalidLicense(ClientError):
    """InvalidLicense exception."""

    status_code = 451
