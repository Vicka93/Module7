"""
Author:Viktoria Denys
Program:basic_list.py


"""

def make_list():
    user_list = []
    for i in range(0, 3):
        try:
            user_input = int(get_input())
        except ValueError:
            pass
        else:
            user_list.insert(i, user_input)
    return user_list

def get_input():
    user_input = input("give me a number: ")
    return user_input


if __name__ == '__main__':
    try:
        test_list = make_list()
    except ValueError:
        print("Enter valid number")
    print(test_list)