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

    def key_accessed_in_lru(self, key):
        for i in range(len(self.lru)):
            if self.lru[i][0] == key:
                self.lru[i][1] = 0
                break

    def put(self, key, item):
        """
        dict.put func
        """
        if key is None or item is None:
            return
        if self.cache_data.get(key) is None:
            self.lru.append([key, 0])
        else:
            self.key_accessed_in_lru(key)
        self.cache_data[key] = item
        if len(self.cache_data) > self.MAX_ITEMS:
            maximum = -1
            maximum_idx = -1
            maximum_key = None
            for i in range(len(self.lru)):
                if maximum < self.lru[i][1]:
                    maximum = self.lru[i][1]
                    maximum_idx = i
                    maximum_key = self.lru[i][0]
            self.lru.pop(maximum_idx)
            del self.cache_data[maximum_key]
            print(f"DISCARD: {maximum_key}")
        for i in range(len(self.lru)):
            self.lru[i][1] += 1

    def get(self, key):
        """
        dict.get func
        """
        if key is None:
            return
        self.key_accessed_in_lru(key)
        return self.cache_data.get(key)
