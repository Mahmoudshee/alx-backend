#!/usr/bin/python3
""" FIFO caching
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache defines:
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
                first_item = self.order[0]
                self.order = self.order[1:]
                del self.cache_data[first_item]
                print("DISCARD: {}".format(first_item))
            self.order.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        return self.cache_data.get(key, None)
