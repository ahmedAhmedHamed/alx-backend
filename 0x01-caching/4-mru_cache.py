#!/usr/bin/env python3
"""
MRUCache module
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache  class
    """

    def __init__(self):
        super().__init__()
        self.mru = []
        self.timer = 0

    def key_accessed_in_mru(self, key):
        """
        makes time of key zero
        """
        for i in range(len(self.mru)):
            if self.mru[i][0] == key:
                self.mru[i][1] = self.timer
                break

    def put(self, key, item):
        """
        dict.put func
        """
        if key is None or item is None:
            return
        flag = False
        if self.cache_data.get(key) is None:
            flag = True
        self.cache_data[key] = item
        if len(self.cache_data) > self.MAX_ITEMS:
            maximum = -1
            maximum_idx = -1
            maximum_key = None
            for i in range(len(self.mru)):
                if maximum < self.mru[i][1]:
                    maximum = self.mru[i][1]
                    maximum_idx = i
                    maximum_key = self.mru[i][0]
            self.mru.pop(maximum_idx)
            del self.cache_data[maximum_key]
            print(f"DISCARD: {maximum_key}")
        if flag:
            self.mru.append([key, self.timer])
        else:
            self.key_accessed_in_mru(key)
        self.timer += 1  # possible use case for decorators!

    def get(self, key):
        """
        dict.get func
        """
        if key is None:
            return
        self.key_accessed_in_mru(key)
        self.timer += 1
        return self.cache_data.get(key)
