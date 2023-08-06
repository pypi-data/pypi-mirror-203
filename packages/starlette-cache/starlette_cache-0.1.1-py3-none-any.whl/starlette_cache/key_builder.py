from typing import Callable, Optional

from starlette.requests import Request
from starlette.responses import Response
from acb.hash import hash
from . import StarletteCache


def default_key_builder(
    func: Callable,
    namespace: Optional[str] = "",
    request: Optional[Request] = None,
    response: Optional[Response] = None,
    args: Optional[tuple] = None,
    kwargs: Optional[dict] = None,
) -> str:
    prefix = f"{StarletteCache.get_prefix()}:{namespace}:"
    cache_key = prefix + hash.blake2b(
        f"{func.__module__}:{func.__name__}:{args}:{kwargs}"
    )
    return cache_key
