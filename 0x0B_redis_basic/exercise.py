#!/usr/bin/env python3
"""Redis cache system"""
import redis
import uuid
from typing import Callable, Optional, Union


class Cache:
    """Class for caching with Redis"""
    def __init__(self):
        """Initialize Redis"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Takes a data argument and returns a string"""
        key: str = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable]) -> str:
        """Gets an element from Redis"""
        element = self._redis.get(key)
        if fn:
            return fn(element)
        return element

    def get_str(self, key) -> str:
        """TBD"""
        return key.decode()


    def get_int(self, key) -> int:
        """TBD"""
        return int(key)
