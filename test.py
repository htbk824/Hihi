import pytest
from sorting_algorithms import insertion_sort

class TestInsertionSort:
    def test_sorted_array(self):
        # Already sorted array
        assert insertion_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    def test_reverse_sorted_array(self):
        # Reverse sorted array
        assert insertion_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

    def test_unsorted_array(self):
        # Unsorted array
        assert insertion_sort([3, 1, 4, 5, 2]) == [1, 2, 3, 4, 5]

    def test_array_with_duplicates(self):
        # Array with duplicate elements
        assert insertion_sort([4, 2, 2, 8, 5, 5]) == [2, 2, 4, 5, 5, 8]

    def test_empty_array(self):
        # Empty array
        assert insertion_sort([]) == []

    def test_single_element_array(self):
        # Array with a single element
        assert insertion_sort([42]) == [42]
