import inspect
import re
from jinja2 import Environment
from pathlib import Path
from typing import Collection, Union

from kaiju_tools.services import Service
from kaiju_tools.rpc.server import JSONRPCServer

__all__ = ['RPCClientCodeGenerator']


module_template = """import uuid
from typing import *

from kaiju_tools.rpc.client import RPCClientService


class {{ app_name }}Client(RPCClientService):
    {{ service_doc }}

    {% for method in methods %}
    async def {{ method['name'] }}({{ method['signature'] }}):
        {{ method['doc'] }}
        return await self.call(
            method='{{ method['rpc_name'] }}',
            params={{ method['params'] }}
        )
    {% endfor %}

"""


class RPCClientCodeGenerator(Service):
    """It can generate python code for an RPC application client."""

    def __init__(self, *args, template_path: Union[str, Path] = None, **kws):
        """Initialize."""
        super().__init__(*args, **kws)
        if template_path is None:
            self._template = module_template
        else:
            with open(template_path) as f:
                self._template = f.read()

    def generate_source_file(self, output: Union[str, Path], services: Collection[str] = None) -> None:
        """Create source files for a client from application services."""
        app_name = self._reformat_app_name(self.app.name)
        service_doc = f'"""Auto-generated {app_name} RPC client."""'
        rpc = self.discover_service(None, cls=JSONRPCServer)
        if services:
            services = frozenset(services)
        methods = []
        for method_name, method_info in rpc._methods.items():  # noqa
            if services is not None and method_info.service_name not in services:
                continue
            f = method_info['f']
            sig = inspect.signature(f)
            sig_text = ['self']
            sig_text.extend([str(value) for key, value in sig.parameters.items() if not key.startswith('_')])
            sig_text = ', '.join(sig_text)
            params = ', '.join(f'{key}={key}' for key in sig.parameters.keys() if not key.startswith('_'))
            service_name = self._reformat_service_name(method_info['service_name'])
            name = f'{service_name}_{f.__name__}'
            method_data = {
                'rpc_name': method_name,
                'name': name,
                'doc': f'"""{f.__doc__}"""' if f.__doc__ else f'"""Call {method_name} remotely."""',
                'signature': sig_text,
                'params': f'dict({params})',
            }
            methods.append(method_data)

        template = Environment().from_string(module_template)
        code = template.render(app_name=app_name, service_doc=service_doc, methods=methods)
        with open(output, 'w') as f:
            f.write(code)

    @staticmethod
    def _reformat_app_name(name: str) -> str:
        name = name.replace('-', '_').split('_')
        name = ''.join(part.capitalize() for part in name)
        return name

    @staticmethod
    def _reformat_service_name(name: str) -> str:
        name_parts = re.findall('[A-Z][^A-Z]*', name)
        if name_parts:
            name = '_'.join(part.lower() for part in name_parts)
        return name.replace('.', '_')
