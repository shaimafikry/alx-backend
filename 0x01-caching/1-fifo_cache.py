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
        if key is not None and item is not None:
            self.cache_data.update({key: item})
        if len(self.cache_data) > BaseCashing.MAX_ITEMS:
            key_d = next(iter(self.cache_data))
            del self.cache_data[key_d]
            print(f"DISCARD: {key_d}")

    def get(self, key):
        """ print item"""
        return self.cache_data.get(key)
