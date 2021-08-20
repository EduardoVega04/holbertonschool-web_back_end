#!/usr/bin/env python3
"""The basics of async"""

import asyncio
from random import uniform


async def wait_random(max_delay: float = 10) -> float:
    """Takes an intener, waits for a random delay and return it"""
    delay: float = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
