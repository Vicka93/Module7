"""
Author:Viktoria Denys
Program:basic_list.py


"""

def make_list():
    user_list = []
    for i in range(0, 3):
        user_input = int(get_input())
        user_list.insert(i, user_input)
    return user_list

def get_input():
    pass



# if __name__ == '__main__':