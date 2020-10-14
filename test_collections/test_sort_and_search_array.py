import unittest
from unittest.mock import patch
from fun_with_collections import sort_and_search_array


def test_sort(arr):
    new_arr = sorted(arr)
    sort_and_search_array.sort_array(arr)
    if arr == new_arr:
        print("Test Passed")
    else:
        print("Test Failed")


def test_search(arr, value):
    index = sort_and_search_array.search_array(arr, value)
    if index == -1:
        print(value, "not present in the array")
    else:
        print(value, " present in the array at index: ", index)


my_arr = [5, 7, 2, 4, 0]

test_search(my_arr, 9)
test_search(my_arr, 2)

test_sort(my_arr)

if __name__ == '__main__':
    unittest.main()
