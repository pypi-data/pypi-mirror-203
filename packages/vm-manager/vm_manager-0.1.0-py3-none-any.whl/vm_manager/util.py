from functools import lru_cache, wraps
from typing import Any, Callable

import time


def ttl_cache(max_age: int, maxsize: int = 128, hash: Callable[[tuple[Any, ...]], Any] | None = hash):
    params = ((), {})

    def decorator(func: Callable[..., Any]):
        @lru_cache(maxsize=maxsize)
        def cached_func(t, key):
            args, kwargs = params
            return func(*args, **kwargs)

        @wraps(func)
        def wrapped_func(*args: Any, **kwargs: Any):
            nonlocal params
            params = args, kwargs
            key = hash(args) if hash is not None else None
            return cached_func(time.time() // max_age, key)

        return wrapped_func

    return decorator
