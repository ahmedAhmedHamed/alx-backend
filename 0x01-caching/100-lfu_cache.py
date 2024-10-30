#!/usr/bin/env python3
"""
MRUCache module
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    MRUCache  class
    """

    def __init__(self):
        super().__init__()
        self.mru = []
        self.timer = 0

    def key_accessed_in_lfu(self, key):
        """
        makes time of key zero
        """
        for i in range(len(self.mru)):
            if self.mru[i][0] == key:
                self.mru[i][1] = self.timer
                self.mru[i][2] = self.mru[i][2] + 1
                break

    def discard_lfu(self):
        max_frequency_instances = []
        min_frequency = 99999999999
        for _, _, frequency in self.mru:
            min_frequency = min(frequency, min_frequency)
        for i in range(len(self.mru)):  # build array containing all==max freq
            if min_frequency == self.mru[i][2]:
                # 0: key, 1: timer, i: idx in mru
                max_frequency_instances.append([self.mru[i][0], self.mru[i][1], i])
        # get lru out of mru
        # least recently used = smallest timer
        smallest_timer = 9999999999
        removed_key = None
        removed_idx = None
        
        for i in range(len(max_frequency_instances)):
            if max_frequency_instances[i][1] < smallest_timer:
                smallest_timer = max_frequency_instances[i][1]
                removed_key = max_frequency_instances[i][0]
                removed_idx = max_frequency_instances[i][2]

        self.mru.pop(removed_idx)
        del self.cache_data[removed_key]
        print(f"DISCARD: {removed_key}")

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
            self.discard_lfu()
        if flag:
            self.mru.append([key, self.timer, 1])
        else:
            self.key_accessed_in_lfu(key)
        self.timer += 1  # possible use case for decorators!

    def get(self, key):
        """
        dict.get func
        """
        if key is None:
            return
        self.key_accessed_in_lfu(key)
        self.timer += 1
        return self.cache_data.get(key)
