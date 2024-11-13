import pytest

class TestBinarySearchTree:
    @pytest.fixture
    def bst(self):
        # Create and return a BinarySearchTree for testing
        bst = BinarySearchTree()
        bst.insert(50)
        bst.insert(30)
        bst.insert(70)
        bst.insert(20)
        bst.insert(40)
        bst.insert(60)
        bst.insert(80)
        return bst

    def test_search_existing_key(self, bst):
        # Test searching for existing keys
        assert bst.search(50) is not None, "Key 50 should be found"
        assert bst.search(30).value == 30, "Key 30 should return the correct node"
        assert bst.search(70).value == 70, "Key 70 should return the correct node"

    def test_search_non_existing_key(self, bst):
        # Test searching for a non-existing key
        assert bst.search(100) is None, "Key 100 should not be found"
        assert bst.search(-10) is None, "Key -10 should not be found"

    def test_search_edge_cases(self, bst):
        # Test edge cases: smallest and largest elements
        assert bst.search(20).value == 20, "Key 20 should be found as the smallest element"
        assert bst.search(80).value == 80, "Key 80 should be found as the largest element"

    def test_empty_tree(self):
        # Test searching in an empty tree
        empty_bst = BinarySearchTree()
        assert empty_bst.search(10) is None, "Searching in an empty tree should return None"
