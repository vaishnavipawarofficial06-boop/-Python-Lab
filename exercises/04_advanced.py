"""Advanced practice: generators, decorators, and async programming.

The async example uses only Python's standard library.
"""

import asyncio
import functools
import time
from collections.abc import Callable, Iterator
from typing import ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")


def chunked(items: list[R], size: int) -> Iterator[list[R]]:
    """Yield consecutive chunks; size must be positive."""
    # TODO: implement as a generator and validate size.
    raise NotImplementedError


def timed(func: Callable[P, R]) -> Callable[P, R]:
    """Decorator that prints elapsed time while preserving metadata."""
    @functools.wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        start = time.perf_counter()
        try:
            return func(*args, **kwargs)
        finally:
            elapsed = time.perf_counter() - start
            print(f"{func.__name__} took {elapsed:.6f}s")

    return wrapper


async def delayed_square(number: int, delay: float = 0.01) -> int:
    """Return the square after an asynchronous delay."""
    # TODO: reject negative delay, await asyncio.sleep, return the square.
    raise NotImplementedError


async def squares_concurrently(numbers: list[int]) -> list[int]:
    """Compute squares concurrently while preserving input order."""
    # TODO: use asyncio.gather with delayed_square.
    raise NotImplementedError


def main() -> None:
    print("Advanced practice: implement the TODOs, then add your own tests.")
    print(f"asyncio available: {asyncio.__name__}")


if __name__ == "__main__":
    main()
