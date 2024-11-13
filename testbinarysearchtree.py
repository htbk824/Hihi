import unittest

class TestBinarySearchTree(unittest.TestCase):
    def setUp(self):
        # Initialize a Binary Search Tree for testing
        self.bst = BinarySearchTree()
        # Insert some initial nodes
        self.bst.insert(50)
        self.bst.insert(30)
        self.bst.insert(70)
        self.bst.insert(20)
        self.bst.insert(40)
        self.bst.insert(60)
        self.bst.insert(80)

    def test_search_existing_key(self):
        # Test searching for existing keys
        self.assertIsNotNone(self.bst.search(50), "Key 50 should be found")
        self.assertEqual(self.bst.search(30).value, 30, "Key 30 should return the correct node")
        self.assertEqual(self.bst.search(70).value, 70, "Key 70 should return the correct node")

    def test_search_non_existing_key(self):
        # Test searching for a non-existing key
        self.assertIsNone(self.bst.search(100), "Key 100 should not be found")
        self.assertIsNone(self.bst.search(-10), "Key -10 should not be found")

    def test_search_edge_cases(self):
        # Test edge cases: smallest and largest elements
        self.assertEqual(self.bst.search(20).value, 20, "Key 20 should be found as the smallest element")
        self.assertEqual(self.bst.search(80).value, 80, "Key 80 should be found as the largest element")

    def test_empty_tree(self):
        # Test searching in an empty tree
        empty_bst = BinarySearchTree()
        self.assertIsNone(empty_bst.search(10), "Searching in an empty tree should return None")

if __name__ == "__main__":
    unittest.main()
