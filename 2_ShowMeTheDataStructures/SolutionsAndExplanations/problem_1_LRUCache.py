class DLLNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.dic = dict()
        self.head = DLLNode(0, 0)
        self.tail = DLLNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key in self.dic:
            n = self.dic[key]
            self._remove(n)
            self._add(n)
            return n.value
        return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache
        # is at capacity remove the oldest item.
        if key in self.dic:
            self._remove(self.dic[key])
        n = DLLNode(key, value)
        self._add(n)
        self.dic[key] = n
        if len(self.dic) > self.capacity:
            n = self.head.next
            self._remove(n)
            del self.dic[n.key]

    def _remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    def _add(self, node):
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.prev = p
        node.next = self.tail


# Tests
# Testcase 1
print('***** Testcase 1 *****')
our_cache1 = LRU_Cache(5)
our_cache1.set(1, 1)
our_cache1.set(2, 2)
our_cache1.set(3, 3)
our_cache1.set(4, 4)
print(our_cache1.get(1))  # returns 1
print(our_cache1.get(2))  # returns 2
print(our_cache1.get(9))  # returns -1 because 9 is not present in the cache
our_cache1.set(5, 5)
our_cache1.set(6, 6)
# returns -1 because the cache reached it's capacity and 3 was the LRU entry
print(our_cache1.get(3))

# Testcase 2
print('***** Testcase 2 *****')
our_cache2 = LRU_Cache(1)
our_cache2.set(1, 1)
our_cache2.set(2, 2)
print(our_cache2.get(1))
print(our_cache2.get(2))
our_cache2.set(5, 5)
print(our_cache2.get(5))
print(our_cache2.get(6))

# Testcase 3
print('***** Testcase 3 *****')
our_cache2 = LRU_Cache(3)
our_cache2.set(1, 1)
our_cache2.set(2, 2)
print(our_cache2.get(1))
print(our_cache2.get(2))
our_cache2.set(5, 5)
print(our_cache2.get(5))
print(our_cache2.get(6))
