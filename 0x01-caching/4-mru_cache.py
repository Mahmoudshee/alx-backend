#!/usr/bin/python3
""" MRU caching
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache defines:
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
            if key in self.cache_data:
                self.order.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                last_item = self.order[-1]
                self.order = self.order[:-1]
                del self.cache_data[last_item]
                print("DISCARD: {}".format(last_item))
            self.order.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key in self.cache_data:
            self.order.remove(key)
            self.order.append(key)
            return self.cache_data[key]
        return None
