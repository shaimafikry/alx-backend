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
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data.update({key: item})
            self.freq[key] += 1
            self.order.remove(key)
            self.order.append(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
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
                # the key to remove
                self.cache_data.pop(key_to_del, None)
                self.freq.pop(key_to_del, None)
                self.order.remove(key_to_del)
                print(f"DISCARD: {key_to_del}")
        self.cache_data[key] = item
        self.freq.update({key: 1})
        self.order.append(key)

    def get(self, key):
        """ print item"""
        if key is None or key not in self.cache_data:
            return None
        self.freq[key] += 1
        self.order.remove(key)
        self.order.append(key)
        return self.cache_data.get(key)
