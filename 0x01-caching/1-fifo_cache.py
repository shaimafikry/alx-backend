#!/usr/bin/env python3
""" cashing system"""
from collections import OrderedDict
BaseCashing = __import__('base_caching').BaseCaching


class FIFOCache(BaseCashing):
    """cashing system"""
    def __init__(self):
        """ initition"""
        super().__init__()

    def put(self, key, item):
        """adding items fifo"""
        if len(self.cache_data) > BaseCashing.MAX_ITEMS:
            key_d = OrderedDict(self.cache_data).popitem(last=False)
            print(f"DISCARD: {key_d[0]}")
        if key is not None and item is not None:
            self.cache_data.update({key: item})

    def get(self, key):
        """ print item"""
        return self.cache_data.get(key)
