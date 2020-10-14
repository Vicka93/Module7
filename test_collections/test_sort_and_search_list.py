"""
Author:Viktoria Denys
Program: sort_and_search_list.py


"""

import unittest
from fun_with_collections import sort_and_search_list


# test sort if sort_list works print test passed else prints test failed

def test_sort(lst):
    new_lst = sorted(lst)
    sort_and_search_list.sort_list(lst)
    if lst == new_lst:
        print("Test Passed")
    else:
        print("Test Failed")


def test_search(lst, value):
    index = sort_and_search_list.search_list(lst, value)
    if index == -1:
        print(value, "not present in the list")
    else:
        print(value, " present in the list at index: ", index)


my_list = [5, 7, 2, 4, 0]

test_search(my_list, 9)
test_search(my_list, 2)

test_sort(my_list)


if __name__ == '__main__':
    unittest.main()
