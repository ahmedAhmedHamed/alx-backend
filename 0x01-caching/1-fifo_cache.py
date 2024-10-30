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
        self.fifo.append(key)
        self.cache_data[key] = item
        if len(self.fifo) > self.MAX_ITEMS:
            removed_key = self.fifo[0]
            self.fifo = self.fifo[1:]
            del self.cache_data[removed_key]

    def get(self, key):
        """
        dict.get func
        """
        if key is None:
            return
        return self.cache_data.get(key)
