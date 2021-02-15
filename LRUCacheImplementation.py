# Code by Abinaya Ramachandran
# LRU cache is implemented using OrderedDict() in python as it preserves the order the keys are inserted into dict.
from collections import OrderedDict

class LRUCache:
    def __init__(self , capacity = 4):
        self.cache = OrderedDict()
        self.capacity = capacity

    def __getitem__(self, key):
        if key not in self.cache:
            return None

        val = self.cache[key]
        self.cache.move_to_end(key)
        return val

    def __setitem__(self, key, value):
        if len(self.cache) >= self.capacity:
            keys = list(self.cache.keys())
            key_to_remove = keys[-1]
            self.cache.pop(key_to_remove)

        self.cache[key] = value
        self.cache.move_to_end(key)


class TestLRUCache(object):
    def test_init(self):
        n = 10
        lru = LRUCache(capacity=n)
        assert lru.capacity == n
        assert hasattr(lru, "cache")

    def test_set(self):
        lru = LRUCache()
        lru["a"] = 1
        assert lru.cache["a"] == 1

    def test_evict_over_limit(self):
        n = 2
        lru = LRUCache(capacity=n)
        lru["a"] = 1
        lru["b"] = 2
        lru["c"] = 3

        assert len(lru.cache) == n

    def test_set_moves_to_top(self):
        lru = LRUCache(capacity=2)
        lru["a"] = 1
        lru["b"] = 2

        assert list(lru.cache.keys()) == ["a", "b"]

        lru["a"] = 1
        assert list(lru.cache.keys()) == ["b", "a"]

    def test_get(self):
        value = 1
        lru = LRUCache()
        lru["a"] = value
        assert lru["a"] == value

    def test_get_moves_to_top(self):
        lru = LRUCache()
        lru["a"] = 1
        lru["b"] = 2
        print(list(lru.cache.keys()))
        assert list(lru.cache.keys()) == ["a", "b"]

        lru["a"]
        assert list(lru.cache.keys()) == ["b", "a"]


tester = TestLRUCache()
for method in dir(tester):
    if not method.startswith("test"):
        continue
    getattr(tester, method)()
