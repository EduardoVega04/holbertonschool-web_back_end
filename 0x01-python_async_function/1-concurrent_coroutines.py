#!/usr/bin/env python3
"""Let's execute multiple coroutines at the same time with async
"""
import asyncio
from asyncio.futures import Future
from typing import Iterator, List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Return the list of all the delays"""
    iterator_futures: Iterator[Future] = asyncio.as_completed(
        [wait_random(max_delay) for _ in range(n)])

    delays: List[float] = [await future for future in iterator_futures]
    return delays
