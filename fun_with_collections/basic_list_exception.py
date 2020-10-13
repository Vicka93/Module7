"""
Author:Viktoria Denys
Program:basic_list.py


"""

def make_list():
    # asks for 3 user input in a loop
    user_list = []
    for i in range(0, 3):
        # casts the input to desired type, raising exception on non-numeric input
        try:
            user_input = int(get_input())
        except ValueError:
            pass
        else:
            user_list.insert(i, user_input)
            # returns the list
    return user_list

def get_input():
    # prompt user for input
    user_input = input("give me a number: ")
    return user_input


if __name__ == '__main__':
    try:
        test_list = make_list()
    except ValueError:
        print("Enter valid number")
    print(test_list)