#!/usr/bin/python3
"""caching system"""
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ caching system"""
    def __init__(self):
        """ initation"""
        super().__init__()
        # to hold frequenceies
        self.freq = {}
        # to hold order
        self.order = []

    def put(self, key, item):
        """adding items fifo"""
        if key is not None and item is not None:
            self.cache_data.update({key: item})
            if self.freq.get(key):
                val = self.freq[key] + 1
                self.freq.update({key: val})
                self.order.remove(key)
                self.order.append(key)
            else:
                self.freq.update({key: 0})
                self.order.append(key)
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # get the least values in freq
            l_freq = min(self.freq.values())
            # get the keys based on values
            l_freq_keys = [k for k, v in self.freq.items() if v == l_freq]
            # check if i have more than one
            if len(l_freq_keys) > 1:
                # search for the key that appears first in self.order
                key_to_del = next(k for k in self.order if k in l_freq_keys)
            else:
                key_to_del = l_freq_keys[0]
            self.cache_data.pop(key_to_del, None)
            self.freq.pop(key_to_del, None)
            self.order.remove(key_to_del)
            print(f"DISCARD: {key_to_del}")

    def get(self, key):
        """ print item"""
        if self.freq.get(key):
            val = self.freq[key] + 1
            self.freq.update({key: val})
            self.order.remove(key)
            self.order.append(key)
        return self.cache_data.get(key)
