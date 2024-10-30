#!/usr/bin/env python3
"""
LRUCache module
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache  class
    """

    def __init__(self):
        super().__init__()
        self.lru = []

    def put(self, key, item):
        """
        dict.put func
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > self.MAX_ITEMS:
            removed_key = self.lru.pop()
            self.lru.append(key)
            del self.cache_data[removed_key]
            print(f"DISCARD: {removed_key}")
        self.lru.append(key)

    def get(self, key):
        """
        dict.get func
        """
        if key is None:
            return
        return self.cache_data.get(key)
