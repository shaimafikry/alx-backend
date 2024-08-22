#!/usr/bin/python3
"""caching system"""
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ caching system"""
    def __init__(self):
        """ initation"""
        super().__init__()

    def put(self, key, item):
        """adding items fifo"""
        if key is not None and item is not None:
            self.cache_data.update({key: item})
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # return the last key
            key_d = list(self.cache_data)[-2]
            del self.cache_data[key_d]
            print(f"DISCARD: {key_d}")

    def get(self, key):
        """ print item"""
        if key is not None:
            # delete the recent used and put it at last
            val = self.cache_data.pop(key, None)
            if val is not None:
                self.cache_data[key] = val
        return self.cache_data.get(key)
