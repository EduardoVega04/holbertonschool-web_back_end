#!/usr/bin/env python3
"""
Async Generator
"""
import asyncio
from random import uniform


async def async_generator():
    """Asynchronous generator"""
    for _ in range(11):
        asyncio.sleep(1)
        yield uniform(0, 10)
