"""Basic Cache module
"""
BaseCaching = __import__('caching').BaseCaching


class BasicCache(BaseCaching):

    def put(self, key, item):
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """default dict behaviour
        """
        if key is None:
            return
        return self.cache_data.get(key)
