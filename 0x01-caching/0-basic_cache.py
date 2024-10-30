#!/usr/bin/env python3
"""
basic cache module
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    basic cache class
    """

    def put(self, key, item):
        """
        dict.put func
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        dict.get func
        """
        if key is None:
            return
        return self.cache_data.get(key)
