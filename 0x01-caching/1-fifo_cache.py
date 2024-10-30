#!/usr/bin/env python3
"""
basic cache module
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache  class
    """

    def __init__(self):
        super().__init__()
        self.fifo = []

    def put(self, key, item):
        """
        dict.put func
        """
        if key is None or item is None:
            return
        flag = False
        if self.cache_data.get(key) is None:
            self.fifo.append(key)
            flag = True
        self.cache_data[key] = item
        if flag and len(self.fifo) > self.MAX_ITEMS:
            removed_key = self.fifo[0]
            self.fifo = self.fifo[1:]
            del self.cache_data[removed_key]
            print(f"DISCARD: {removed_key}")

    def get(self, key):
        """
        dict.get func
        """
        if key is None:
            return
        return self.cache_data.get(key)
