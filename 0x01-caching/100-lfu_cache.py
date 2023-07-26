#!/usr/bin/python3
""" LFU caching
"""

from base_caching import BaseCaching
from collections import OrderedDict


class LFUCache(BaseCaching):
    """ LFUCache defines:
      - caching system which inherits from BaseCaching
    """

    def __init__(self):
        """ Initialize
        """
        super().__init__()
        self.frequency = {}

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.frequency[key] += 1
            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    min_freq = min(self.frequency.values())
                    lfu_keys = [k for k in self.frequency
                                if self.frequency[k] == min_freq]
                    lfu_cache = {k: self.cache_data[k] for k in lfu_keys}
                    lru_key = min(lfu_cache, key=lambda k: self.order.index(k))
                    self.order.remove(lru_key)
                    del self.cache_data[lru_key]
                    del self.frequency[lru_key]
                    print("DISCARD: {}".format(lru_key))
                self.cache_data[key] = item
                self.frequency[key] = 1
            self.order.append(key)

    def get(self, key):
        """ Get an item by key
        """
        if key in self.cache_data:
            self.frequency[key] += 1
            return self.cache_data[key]
        return None
