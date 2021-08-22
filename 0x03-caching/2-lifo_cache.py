#!/usr/bin/python3
"""Create LIFOCache class that inherits from BaseCaching"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Simulates a LIFO cache system"""

    def __init__(self):
        """Initializes the LIFO cache system"""
        super().__init__()
        self.cache_lifo = []

    def put(self, key, item):
        """Puts an entry in the FIFO system"""
        if key and item:
            self.cache_data[key] = item
            self.cache_lifo.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            removed = self.cache_lifo.pop()
            del self.cache_data[removed]
            print(f"DISCARD: {removed}")

    def get(self, key):
        """Gets and returns an entry from the cache system"""
        return self.cache_data.get(key)
