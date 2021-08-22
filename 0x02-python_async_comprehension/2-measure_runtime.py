#!/usr/bin/env python3.7
"""
2. Run time for four parallel comprehensions
"""
import asyncio
from time import perf_counter
async_comp = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Will execute async_comprehension four times in parallel"""
    start: float = perf_counter()
    await asyncio.gather([async_comp() for _ in range(4)])
    end: float = perf_counter() - start
    return end
