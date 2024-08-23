# cashing

# Using OrderedDict for FIFO
collections.OrderedDict was introduced to remember the order entries were added, making it suitable for FIFO operations. When you pop items from an OrderedDict, you can specify whether to pop the last inserted item (LIFO) or the first inserted item (FIFO).
```
from collections import OrderedDict

# Creating an OrderedDict
fifo_dict = OrderedDict()

# Adding items
fifo_dict['polo1'] = 789
fifo_dict['polo2'] = 123
fifo_dict['polo3'] = 4556

# Popping the first inserted item (FIFO)
first_item = fifo_dict.popitem(last=False)
print(first_item)  # Output: ('polo1', 789)

```

In this example, popitem(last=False) removes and returns the first inserted item, demonstrating FIFO behavior 1.

# using next(iter())

The line `oldest_key = next(iter(self.cache_data))` is used to retrieve the oldest key in the `self.cache_data` dictionary, which is assumed to represent the first item inserted into the cache based on the FIFO (First In, First Out) principle. Let's break down how this works:

1. **`iter(self.cache_data)`:** This function returns an iterator object that iterates over the keys of the `self.cache_data` dictionary. In Python dictionaries, iteration order is preserved starting from Python 3.7, meaning that the keys will be returned in the order they were inserted into the dictionary. This behavior allows us to assume that the first key returned by the iterator is the oldest key, i.e., the key of the first item inserted into the cache.

2. **`next()`:** The `next()` function takes an iterator object and returns the next item from the iterator. When called without arguments, `next()` retrieves the first item from the iterator. In the context of `next(iter(self.cache_data))`, it retrieves the first key from the iterator over `self.cache_data.keys()`, which, due to the preservation of insertion order in dictionaries, is the oldest key.

Combining these two functions, `oldest_key = next(iter(self.cache_data))` effectively retrieves the key of the first item inserted into the cache, allowing us to identify and subsequently discard the oldest item when the cache reaches its maximum size limit according to the FIFO caching algorithm.


What is LRU (Least Recently Used)?
LRU (Least Recently Used) is a cache replacement policy that evicts the least recently accessed item when the cache reaches its capacity. The idea behind LRU is that data that hasn't been accessed for the longest time is less likely to be needed again soon, so it should be the first to be removed.

How LRU Works:
Tracking Usage: LRU keeps track of the order in which items are accessed. This can be done using data structures like linked lists or by storing timestamps or counters with each item.
Eviction: When the cache reaches its maximum size and a new item needs to be added, the LRU algorithm removes the item that was accessed the longest time ago.
Example:
Imagine a cache with a capacity of 3 items: [A, B, C].
If you access item B, the order of access might look like [A, C, B].
If you then add a new item D to the cache, the LRU item (which is A, as it was accessed the longest time ago) will be evicted, resulting in the new cache state [C, B, D].


# Rearranging Based on Access Order (for LRU)
For something like LRU, you might want to rearrange the dictionary whenever an item is accessed. This would involve removing the item and re-inserting it to move it to the end (or beginning) of the dictionary:

```
cache = {'a': 1, 'b': 2, 'c': 3}

# Simulate accessing key 'b'
value = cache.pop('b', None)
cache['b'] = value

print(cache)  # Output: {'a': 1, 'c': 3, 'b': 2} (moved 'b' to the end)
```
