import kaiju_tools.jsonschema as js

__all__ = [
    'ConfigurationError',
    'Settings',
    'ServiceSettings',
    'AppSettings',
    'MainSettings',
    'ProjectSettings',
    'RunSettings',
]


class ConfigurationError(KeyError):
    """Configuration key not found."""


class Settings(dict):
    """Settings object."""

    validator: js.Object = None

    def __init__(self, seq):
        """Initialize."""
        if self.validator:
            seq = js.compile_schema(self.validator)(seq)
        super().__init__(seq)

    def __getattr__(self, item):
        """Get a parameter from settings dict."""
        try:
            return self[item]
        except KeyError:
            raise ConfigurationError(f'No such config value: {item}')


class AppSettings(Settings):
    """Web application init settings."""

    validator = js.Object(
        {'debug': js.Boolean(default=False), 'client_max_size': js.Integer(minimum=1024, default=1024**2)},
        additionalProperties=False,
        required=[],
    )


class RunSettings(Settings):
    """Server run settings."""

    validator = js.Object(
        {
            'host': js.String(minLength=1, nullable=True, default=None),
            'port': js.Integer(minimum=1, nullable=True, maximum=65535, default=None),
            'path': js.String(minLength=1, nullable=True, default=None),
            'shutdown_timeout': js.Integer(minimum=0, default=60),
            'keepalive_timeout': js.Integer(minimum=0, default=75),
        },
        additionalProperties=False,
        required=[],
    )


class MainSettings(Settings):
    """Main project settings."""

    validator = js.Object(
        {
            'name': js.String(minLength=1),
            'version': js.String(minLength=1),
            'env': js.String(minLength=1),
            'loglevel': js.Enumerated(['DEBUG', 'INFO', 'WARNING', 'ERROR'], default='INFO'),
        },
        additionalProperties=False,
        required=['name', 'version', 'env'],
    )


class ServiceSettings(Settings):
    """Service configuration."""

    validator = js.Object(
        {
            'cls': js.String(minLength=1),
            'name': js.String(minLength=1),
            'info': js.String(minLength=0),
            'enabled': js.Boolean(default=True),
            'settings': js.Object(),
        },
        additionalProperties=False,
        required=['cls'],
    )

    def __init__(self, seq):
        if type(seq) is str:
            seq = {'cls': seq}
        super().__init__(seq)


class ProjectSettings(Settings):
    """Validation schema for project settings."""

    def __init__(self, version, app, run, main, etc, services):
        """Initialize."""
        super().__init__(
            dict(
                version=version,
                app=AppSettings(app),
                run=RunSettings(run),
                main=MainSettings(main),
                etc=Settings(etc),
                services=tuple(ServiceSettings(srv) for srv in services),
            )
        )
