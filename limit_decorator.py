import asyncio
import functools
from typing import Callable


def limit(max: int):
    def decorator(fn: Callable):
        sem = asyncio.Semaphore(max)
        @functools.wraps(fn)
        async def wrapper(*args, **kwargs):
            async with sem:
                return await fn(*args, **kwargs)
        return wrapper
    return decorator


if __name__ == "__main__":
    print("please run main.py")
