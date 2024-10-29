#!/usr/bin/python3
"""
Basic Cache module
"""
from caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Basic cache class
    """

    def __init__(self):
        """
        just calls super init
        """
        super().__init__()

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
