#!/usr/bin/python3
"""
Basic Cache module
"""
BaseCaching = __import__('caching').BaseCaching


class BasicCache(BaseCaching):
    """
    Basic cache class
    """

    def put(self, key, item):
        """
        default dict behaviour
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        default dict behaviour
        """
        if key is None:
            return
        return self.cache_data.get(key)
