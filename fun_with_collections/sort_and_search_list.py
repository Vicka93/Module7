"""
Author:Viktoria Denys
Program: sort_and_search_list.py


"""


def sort_list(lst):
    lst.sort()
    return lst


# since same list reference is passwed to the function any changes in
# list within the function will also be visible outside the function in the list
# so no need to add a return statement


# if element is present in the list function returns index else -1
def search_list(lst, value):
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
