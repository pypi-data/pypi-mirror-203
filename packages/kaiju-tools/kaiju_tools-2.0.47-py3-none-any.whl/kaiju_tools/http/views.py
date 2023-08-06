from typing import cast

from aiohttp.web import Request, Response, View, json_response, WebSocketResponse, WSMsgType
from aiohttp.http_websocket import WSMessage
from aiohttp_cors import CorsViewMixin

from kaiju_tools.serialization import dumps, loads
from kaiju_tools.services import Scope, Session
from kaiju_tools.rpc.services import JSONRPCServer
from kaiju_tools.rpc.etc import JSONRPCHeaders

__all__ = ['JSONRPCView', 'jsonrpc_websocket_handler']


async def jsonrpc_websocket_handler(request: Request, rpc_server_name: str = 'rpc'):
    """Read from websocket."""
    ws = WebSocketResponse()
    counter = 0
    rpc: JSONRPCServer = getattr(request.app.services, rpc_server_name)  # noqa
    session: Session = request.get('session', None)
    scope: Scope = session.scope if session else Scope.GUEST
    headers = dict(request.headers)

    async def _send_response(_session: Session, headers: dict, result):  # noqa
        nonlocal session, scope, request
        session = request['session'] = _session
        scope = session.scope
        await ws.send_json(result.repr(), dumps=dumps)

    await ws.prepare(request)

    async for msg in ws:
        msg = cast(WSMessage, msg)
        if msg.type == WSMsgType.TEXT:
            if msg.data == 'close':
                await ws.close()
            else:
                data = loads(msg.data)
                counter += 1
                if 'id' not in data:
                    data['id'] = counter
                result = await rpc.call(
                    data, headers=headers, session=session, scope=scope, nowait=True, callback=_send_response
                )
                if result:
                    headers, exc = result
                    await ws.send_json(exc.repr(), dumps=dumps)
        elif msg.type == WSMsgType.ERROR:
            request.app.logger.error('Websocket error: %s', ws.exception())

    if session:
        ws._headers[JSONRPCHeaders.SESSION_ID_HEADER] = session.id  # noqa

    return ws


class JSONRPCView(CorsViewMixin, View):
    """JSON RPC server endpoint."""

    route = '/public/rpc'
    rpc_server_name = 'rpc'

    async def post(self):
        """Make an RPC request."""
        if not self.request.can_read_body:
            return Response()
        data = await self.request.text()
        session: Session = self.request.get('session', None)
        scope: Scope = session.scope if session else Scope.GUEST
        rpc: JSONRPCServer = getattr(self.request.app.services, self.rpc_server_name)  # noqa
        headers, data = await rpc.call(
            loads(data), headers=dict(self.request.headers), session=session, scope=scope, nowait=False
        )
        return json_response(data, headers=headers, dumps=dumps)
