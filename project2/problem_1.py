from collections import OrderedDict

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        if (capacity < 1):
            print("Please enter a valid capacity. Capacity must be greater than zero.")
        else:
            self.cache = OrderedDict()
            self.capacity = capacity
        return

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        value = -1
        if (key in self.cache.keys()):
            value = self.cache[key]
            # move to back of line
            self.cache.pop(key)
            self.cache[key] = value
        return value

    def set(self, key, value):
        # Set the value if the key is not present in the cache. 
        # If the cache is at capacity remove the oldest item. And add new one
        if (len(self.cache) >= self.capacity):
            # remove oldest item FIFO & add new one
            self.cache.popitem(last=False)
            self.cache[key] = value
        if (key in self.cache.keys()):
            print("Key already in cache. Cannot update value.")
        else:
            self.cache[key] = value
        return

# given test case           
our_cache = LRU_Cache(5)
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)
print(our_cache.get(1))       # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(9))      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

print(our_cache.get(3))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

# test case 2
cache = LRU_Cache(-3)
# should print invalid cache side. Must have cache size of at least 1

# test case 3
cache_1 = LRU_Cache(5)
cache_1.set(1, 1)
cache_1.set(2, 2)
cache_1.set(1, 3)
# should print out 'key' already exists. cannot update
