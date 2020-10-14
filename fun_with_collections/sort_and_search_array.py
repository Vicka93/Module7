"""
Author:Viktoria Denys
Program: sort_and_search_array.py


"""
def sort_array(lst):
    # sort array
    lst.sort()


def search_array(my_arr ,value):
    # returns index of item or -1 if item not found
    for i in my_arr:
        if value in my_arr:
            return my_arr.index(value)

    return -1


if __name__ == '__main__':
    my_array = [99, 5, -8, 94]
    user_input = 5
    search = search_array(my_array, user_input)
    print(search)
    sort_array(my_array)
    print("sorted list is", my_array)  # prints the sorted list
