import logging
import unittest

from LRUCache import LRUCache

# logging.basicConfig(level=logging.INFO)


class TestLRUCache(unittest.TestCase):
    def setUp(self):
        self.cache = LRUCache(3)
        self.cache.set("Jesse", "Pinkman")
        self.cache.set("Walter", "White")

    def testSetNew(self):
        print("should set 2 new nodes")
        self.assertEqual(self.cache._LRUCache__count, 2)
        self.assertEqual(self.cache._LRUCache__head.next.key, "Walter")
        self.assertEqual(self.cache._LRUCache__head.next.next.key, "Jesse")

    def testReset(self):
        print("should reset the value and put the node to DLL head.next")
        self.cache.set("Jesse", "James")
        self.assertEqual(self.cache._LRUCache__count, 2)
        self.assertEqual(self.cache._LRUCache__head.next.key, "Jesse")
        self.assertEqual(self.cache._LRUCache__head.next.next.key, "Walter")

    def testGet(self):
        print("should return the value by key")
        self.cache.set("Jesse", "James")
        self.assertEqual(self.cache.get("Jesse"), "James")

    def testRemove(self):
        print("should remove the value by key")
        self.cache.rem("Walter")
        self.assertEqual(self.cache._LRUCache__count, 1)

    def testGetByErrorKey(self):
        print("should handle KeyError exception")
        with self.assertRaises(KeyError):
            self.cache.get("key")


if __name__ == "__main__":
    unittest.main()
