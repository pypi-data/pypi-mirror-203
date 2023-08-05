import asyncio
from time import time
from types import SimpleNamespace
from uuid import uuid4

import pytest

from ..services import JSONRPCServer
from ..etc import JSONRPCHeaders
from ..jsonrpc import *
from .fixtures import *
from kaiju_tools.services import Scope


@pytest.mark.asyncio
async def test_rpc_server_performance(system_information, rpc_interface, logger):

    requests, parallel, n = 1000, 32, 5
    counter = 0

    async def _do_call(rpc):
        nonlocal counter
        data = {'id': 0, 'method': 'do.sleep', 'params': {'test': True}}
        while counter < requests:
            await rpc.call(data, {})
            counter += 1

    class _Service(AbstractRPCCompatible):
        @property
        def routes(self) -> dict:
            return {'sleep': self.do_sleep}

        async def do_sleep(self, test):
            return test

    print(f'\nJSON RPC Queued Service simple benchmark (best of {n}).')
    print(f'{parallel} connections\n')
    print(system_information)

    async with rpc_interface as rpc:
        rpc.register_service('do', _Service(None))
        tasks = [asyncio.create_task(_do_call(rpc)) for _ in range(parallel)]
        t0 = time()
        while counter < requests:
            await asyncio.sleep(0.1)
        t1 = time()
        await asyncio.gather(*tasks)

    dt = t1 - t0
    rps = round(counter / dt)
    print(f'{dt}')
    print(f'{counter} requests')
    print(f'{rps} req/sec')


@pytest.mark.asyncio
async def test_rpc_server_methods(rpc_interface, rpc_compatible_service, logger):
    logger.info('Testing service context initialization.')

    async with rpc_interface as rpc:

        service = rpc_compatible_service(app=rpc.app, logger=logger)
        rpc.register_service(service.service_name, service)

        correlation_id = uuid4()

        logger.info('Testing basic requests.')

        data = {'method': 'm.echo', 'params': None}
        _headers, response = await rpc.call(data, {})
        assert response.result == ((), {})

        data = {'id': None, 'method': 'm.echo', 'params': None}
        _result = await rpc.call(data, {})
        assert _result is None

        data = {'id': uuid4().int, 'method': 'm.echo', 'params': {'value': 42}}
        _headers, response = await rpc.call(data, {})
        assert response.result[1]['value'] == 42

        data = {'id': uuid4().int, 'method': 'm.aecho', 'params': {'a': 1, 'b': 2, 'c': 3}}
        _headers, response = await rpc.call(data, {})
        assert response.result[1] == {'a': 1, 'b': 2, 'c': 3}

        data = {'id': uuid4().int, 'method': 'm.echo', 'params': {'x': True}}
        _headers, response = await rpc.call(data, {})
        assert response.result == ((), {'x': True})

        logger.info('Testing data validation.')

        data = {'id': uuid4().int, 'method': 'm.validated', 'params': {'a': 11, 'b': 2}}
        _headers, response = await rpc.call(data, {})
        assert response.result == 22

        data = {'id': uuid4().int, 'method': 'm.validated', 'params': {'a': 11, 'b': 's'}}
        _headers, response = await rpc.call(data, {})
        logger.debug(response.repr())
        assert isinstance(response, InvalidParams)

        data = {'id': uuid4().int, 'method': 'm.validated', 'params': {'a': 11}}
        _headers, response = await rpc.call(data, {})
        logger.debug(response.repr())
        assert isinstance(response, InvalidParams)

        logger.info('Testing multi requests.')

        data = [
            {'id': uuid4().int, 'method': 'm.echo', 'params': {'x': True}},
            {'id': uuid4().int, 'method': 'm.echo', 'params': {'a': 1, 'b': 2}},
            {'id': uuid4().int, 'method': 'm.aecho', 'params': {'a': 1, 'b': 2}},
        ]
        _headers, response = await rpc.call(data, {})
        assert [r.result for r in response] == [((), {'x': True}), ((), {'a': 1, 'b': 2}), ((), {'a': 1, 'b': 2})]

        logger.info('Testing request error handling.')

        data = {'id': uuid4().int, 'method': 'm.unknown', 'params': {'x': True}}
        _headers, response = await rpc.call(data, {})
        assert isinstance(response, MethodNotFound)

        data = {'id': uuid4().int}
        _headers, response = await rpc.call(data, {})
        assert isinstance(response, InvalidRequest)

        data = {'id': uuid4().int, 'method': 'm.unknown', 'params': {'value': True}, 'shit': 1}
        _headers, response = await rpc.call(data, {})
        assert isinstance(response, InvalidRequest)

        data = {'id': uuid4().int, 'method': 'm.sum', 'params': {'x': 1, 'z': '2'}}
        _headers, response = await rpc.call(data, {})
        assert isinstance(response, InvalidParams)

        data = {'id': uuid4().int, 'method': 'm.fail', 'params': None}
        _headers, response = await rpc.call(data, {})
        assert isinstance(response, InternalError)

        logger.info('Testing timeouts.')

        headers = {}

        data = {'id': uuid4().int, 'method': 'm.long_echo', 'params': None}
        headers[JSONRPCHeaders.REQUEST_TIMEOUT_HEADER] = 1
        _headers, response = await rpc.call(data, headers)
        assert isinstance(response, RequestTimeout)

        data = {'id': uuid4().int, 'method': 'm.long_echo', 'params': None}
        headers[JSONRPCHeaders.REQUEST_TIMEOUT_HEADER] = 10
        _headers, response = await rpc.call(data, headers)
        assert isinstance(response, RPCResponse)

        logger.info('Testing for parallel task execution')

        tasks = []

        for _ in range(4):
            data = {'id': uuid4().int, 'method': 'm.standard_echo', 'params': None}
            headers[JSONRPCHeaders.REQUEST_DEADLINE_HEADER] = int(time() + 1)
            headers[JSONRPCHeaders.CORRELATION_ID_HEADER] = correlation_id
            tasks.append(rpc.call(data, headers))

        t = time()
        await asyncio.gather(*tasks)
        t = time() - t
        assert t <= 1

        logger.info('Testing separate bulk request error handling.')

        data = [
            {'method': 'm.echo', 'params': None},
            {'method': 'm.long_echo', 'params': None},
            {'method': 'm.fail', 'params': None},
            {'method': 'm.sum', 'params': {'x': 1, 'y': 2}},
        ]
        headers[JSONRPCHeaders.REQUEST_DEADLINE_HEADER] = int(time() + 1)
        _headers, response = await rpc.call(data, headers)
        assert isinstance(response[1], RequestTimeout)
        assert isinstance(response[2], RPCError)

        logger.info('Testing context handling.')

        session_1 = SimpleNamespace(id='1', test=True, permission=frozenset(), stored=True, loaded=False, changed=True)
        session_2 = SimpleNamespace(id='2', test=False, permission=frozenset(), stored=True, loaded=True, changed=False)
        data = {'id': uuid4().int, 'method': 'm.uses_context', 'params': None}
        r1, r2 = await asyncio.gather(rpc.call(data, {}, session=session_1), rpc.call(data, {}, session=session_2))
        assert r1[0][JSONRPCHeaders.SESSION_ID_HEADER] == session_1.id
        assert r2[0][JSONRPCHeaders.SESSION_ID_HEADER] == session_2.id

        logger.info('Testing permissions handling.')
        session = SimpleNamespace(id='1', permissions=set(), stored=True, loaded=True, changed=True)
        _, response = await rpc.call({'method': 'm.method_with_user_permission'}, session=session, scope=Scope.GUEST)
        assert isinstance(response, PermissionDenied)

        session.permissions.add('m.method_with_user_permission')
        _, response = await rpc.call({'method': 'm.method_with_user_permission'}, session=session, scope=Scope.GUEST)
        assert response.result is True
        _, response = await rpc.call({'method': 'm.method_with_user_permission_2'}, session=session, scope=Scope.GUEST)
        assert isinstance(response, PermissionDenied)

        logger.info('All tests finished.')
