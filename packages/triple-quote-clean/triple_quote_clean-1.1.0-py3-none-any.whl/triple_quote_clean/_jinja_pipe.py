import typing as t

from ._pipe import Pipe
from jinja2.nativetypes import NativeEnvironment


class JinjaPipe(Pipe):
    environment: NativeEnvironment
    render_args: t.Tuple
    render_kwargs: t.Dict
    env_kwargs: t.Dict[str, str] = dict(
        trim_blocks=True, lstrip_blocks=True, autoescape=True
    )

    def __init__(self, *args, env_kwargs=None, **kwargs):
        if env_kwargs is not None:
            self.env_kwargs.update(env_kwargs)
        self.environment = NativeEnvironment(**self.env_kwargs)
        self.render_args = args
        self.render_kwargs = kwargs

    def __call__(self, template: str) -> str:
        return self.environment.from_string(template).render(
            *self.render_args, **self.render_kwargs
        )
