#!/usr/bin/env python3
""" cashing system"""

BaseCashing = __import__('base_caching').BaseCaching


class BasicCache(BaseCashing):
    """ class of cashing"""
    def __init__(self):
        """ initiaion, super inheret"""
        super().__init__()

    def put(self, key, item):
        """append a new item"""
        if key is not None and item is not None:
            self.cache_data.update({key: item})

    def get(self, key):
        """ print item"""
        return self.cache_data.get(key)
