import pytest
from sorting_algorithms import merge_sort

class TestMergeSort:
    def test_sorted_array(self):
        # Already sorted array
        assert merge_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    def test_reverse_sorted_array(self):
        # Reverse sorted array
        assert merge_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

    def test_unsorted_array(self):
        # Unsorted array
        assert merge_sort([3, 1, 4, 5, 2]) == [1, 2, 3, 4, 5]

    def test_array_with_duplicates(self):
        # Array with duplicate elements
        assert merge_sort([4, 2, 2, 8, 5, 5]) == [2, 2, 4, 5, 5, 8]

    def test_empty_array(self):
        # Empty array
        assert merge_sort([]) == []

    def test_single_element_array(self):
        # Array with a single element
        assert merge_sort([42]) == [42]

    def test_large_array(self):
        # Large array
        large_array = list(range(1000, 0, -1))  # Array sorted in reverse
        sorted_array = list(range(1, 1001))    # Correctly sorted array
        assert merge_sort(large_array) == sorted_array
