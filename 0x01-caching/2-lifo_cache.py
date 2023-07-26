#!/usr/bin/python3
""" LIFO caching
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache defines:
      - caching system which inherits from BaseCaching
    """

    def __init__(self):
        """ Initialize
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                last_item = self.order[-1]
                self.order = self.order[:-1]
                del self.cache_data[last_item]
                print("DISCARD: {}".format(last_item))
            self.order.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        return self.cache_data.get(key, None)
