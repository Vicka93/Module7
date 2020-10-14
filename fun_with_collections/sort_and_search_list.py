"""
Author:Viktoria Denys
Program: sort_and_search_list.py


"""


def sort_list(lst):
    # return sorted list
    lst.sort()
    return lst


def search_list(lst, value):
    # if element is present in the list function returns index else -1
    for i in range(len(lst)):
        if value in lst:
            return lst.index(value)
        else:
            return -1


if __name__ == '__main__':
    user_list = [5, 2, 3]
    user_input = int(input("give me a value: "))
    search = search_list(user_list, user_input)
    print(search)
    print(sort_list(user_list))
