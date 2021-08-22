#!/usr/bin/python3
"""Create FIFOCache class that inherits from BaseCaching"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Simulates a FIFO cache system"""

    def __init__(self):
        """Initializes the FIFO cache system"""
        super().__init__()

    def put(self, key, item):
        """Puts an entry in the FIFO system"""
        fifo_queue_list = []
        if key and item:
            self.cache_data[key] = item
            fifo_queue_list.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            removed = fifo_queue_list.pop(0)
            del self.cache_data[removed]
            print(f"DISCARD: {removed}")

    def get(self, key):
        """Gets and returns an entry from the cache system"""
        return self.cache_data.get(key)
