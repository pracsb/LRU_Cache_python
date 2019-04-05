import sys
from lru_cache import LRUCache

try:
    if sys.version_info < (2, 7):
        import unittest2
    else:
        raise ImportError()
except ImportError:
    import unittest

FAILURE = "Incorrect"


class LRUTest(unittest.TestCase):
    def setUp(self):
        """
        creates an object of the LRUCache with max capacity (here, it is 4)
        """
        self.lru = LRUCache(4)

    def test_get_exists(self):
        print("Test to check get() returns desired value")
        # node1 = 1, 2
        # node2 = 9, 18
        print("Putting node ", 1, ",", 2, " in LRU cache")
        print("Putting node ", 9, ",", 18, " in LRU cache")
        self.lru.put(1, 2)
        self.lru.put(9, 18)
        self.lru.display()
        status, get_res = self.lru.get(1)
        print("Calling get() on the key =", 1, ": Returns - present in cache: ", status, "& gives value =", get_res)
        self.assertEqual(status, True, FAILURE)
        self.assertEqual(get_res, 2, FAILURE)
        print("PASSED: Test to check if get() called on a key present in the cache returns the right value")
        print("=================================================================================================")

    def test_get_does_not_exists(self):
        print("Test to check get() called when key does not exist")
        # node = 2, 4
        test_key = 6
        self.lru.put(2, 4)
        print("Putting node ", 2, ",", 4, " in LRU cache")
        status, get_res = self.lru.get(test_key)
        print("Calling get() on the key =", test_key, "returns", status)
        self.assertEqual(status, False, FAILURE)
        self.assertEqual(get_res, None, FAILURE)
        print(" PASSED : Test to check if get() is called on a key that is not present in the cache")
        print("=================================================================================================")

    def test_get_changes_order(self):
        print("Test to check get() call updates last used time of node")
        # node1 = 1,4
        # node2 = 2,6
        # node3 = 7,10
        self.lru.put(1, 4)
        self.lru.put(2, 6)
        self.lru.put(7, 10)
        print("BEFORE: Order of nodes in Cache")
        self.lru.display()
        status, value = self.lru.get(1)
        self.assertEqual(self.lru.head.next.key, 1, FAILURE)
        print("Calling get() on key present in cache updates Last Used Time of that node")
        print("AFTER: Order of nodes in cache after get()")
        self.lru.display()
        print("PASSED: Test to check if calling get() updates the LAST USED TIME of the node")
        print("=================================================================================================")

    def test_put_updated_val(self):
        print("Test to check put() returns desired value")
        # node1 = 5,10
        # node2 = 3,6
        self.lru.put(5, 10)
        print("Putting node ", 5, ",", 10, " in LRU cache")
        self.lru.put(3, 6)
        print("Putting node ", 3, ",", 6, " in LRU cache")
        self.lru.display()
        print("Calling get() on key =", 5, "gives value =", self.lru.get(5))
        # node3 = 5, 15
        self.lru.put(5, 15)
        print("# New Node with same key but different value #")
        print("Putting node ", 5, ",", 15, " in LRU cache")
        status, get_res = self.lru.get(5)
        print("Now Calling get() on key =", 5, "gives value =", get_res)
        self.lru.display()
        self.assertEqual(status, True, FAILURE)
        self.assertEqual(get_res, 15, FAILURE)
        print("PASSED : Test to check if put() updates the cache with new value for already existent key if new node")
        print("with same key is added to it.The new node is now at the front.")
        print("=================================================================================================")

    def test_put_cache_order(self):
        print("Test to check put() updates cache order")
        # Inserting these values in cache in order:
        # node1 = 5, 10
        # node2 = 3, 6
        # node3 = 2, 4
        # node4 = 7, 14
        # node5 = 8, 16
        self.lru.put(5, 10)
        print("Putting node ", 5, " in LRU cache")
        self.lru.put(3, 6)
        print("Putting node ", 3, " in LRU cache")
        self.lru.put(2, 4)
        print("Putting node ", 2, " in LRU cache")
        self.lru.put(7, 14)
        print("Putting node ", 7, " in LRU cache")
        print("BEFORE: Cache filled with maximum capacity : ")
        self.lru.display()
        print("Putting node ", 8, " in LRU cache")
        self.lru.put(8, 16)
        print("AFTER : putting new node in full LRU cache ")
        print("Evicts least recently used node from cache and inserts this new node")
        self.lru.display()
        self.assertEqual(self.lru.head.next.key, 8, FAILURE)
        self.assertNotEqual(self.lru.tail.prev.key, 5, FAILURE)
        print("PASSED: Checking capacity constraint when calling put on full cache ")
        print("=================================================================================================")


if __name__ == '__main__':
    import xmlrunner

    unittest.main(
        testRunner=xmlrunner.XMLTestRunner(output='test-reports'),
        failfast=True,
        buffer=False,
        catchbreak=False)
