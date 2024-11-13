import pytest
from search_algorithms import linear_search

class TestLinearSearch:
    def test_element_present(self):
        # Test when the target element is present in the array
        arr = [10, 20, 30, 40, 50]
        assert linear_search(arr, 30) == 2, "Target 30 should be found at index 2"
        assert linear_search(arr, 10) == 0, "Target 10 should be found at index 0"
        assert linear_search(arr, 50) == 4, "Target 50 should be found at index 4"

    def test_element_not_present(self):
        # Test when the target element is not in the array
        arr = [10, 20, 30, 40, 50]
        assert linear_search(arr, 60) == -1, "Target 60 should not be found"
        assert linear_search(arr, 0) == -1, "Target 0 should not be found"

    def test_empty_array(self):
        # Test with an empty array
        arr = []
        assert linear_search(arr, 10) == -1, "Search in an empty array should return -1"

    def test_array_with_duplicates(self):
        # Test with an array containing duplicate elements
        arr = [10, 20, 30, 20, 40]
        assert linear_search(arr, 20) == 1, "Target 20 should return the first occurrence at index 1"

    def test_single_element_array(self):
        # Test with a single element array
        arr = [42]
        assert linear_search(arr, 42) == 0, "Target 42 should be found at index 0"
        assert linear_search(arr, 10) == -1, "Target 10 should not be found"
