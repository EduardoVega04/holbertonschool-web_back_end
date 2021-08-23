#!/usr/bin/python3
""" Create LFUCache class that inherits from BaseCaching """
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """Class than simulates a LFU caching system"""
    def __init__(self):
        """Initialize the LFU caching system"""
        super().__init__()
        self.cache_freq = {}
    
    def put(self, key, item):
        """Puts an entry in the LFU caching system"""
        limit = BaseCaching.MAX_ITEMS
        if key and item:
            if len(self.cache_data) == limit and key not in self.cache_data:
                for key, val in self.cache_freq.items():
                    target, rank = key, val
                    if val < rank:
                        target, rank = key, val
                del self.cache_data[target]
                del self.cache_freq[target]                
                print(f"DISCARD: {target}")
            if key not in self.cache_data:
                self.cache_freq[key] = 0
            self.cache_data[key] = item
    
    def get(self, key):
        """Gets an entry from the LFU caching system"""
        if key in self.cache_data:
            self.cache_freq[key] += 1
        return self.cache_data.get(key)
