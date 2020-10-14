"""
Author:Viktoria Denys
Program: basic_IO.py


"""
import os

FILE_NAME = 'student_info.txt'
MAX = 50
MIN = 1

def write_to_file(*args):
    print(args)
    file = open("student_info.txt", 'a')  # open file
    file.write(str(args) + '\n')
    file.close()  # close file

def get_student_info(**kwargs):
    print("Welcome, {} {}!".format(kwargs["first_name"],kwargs["last_name"]))
    scores=[]
    num = 0
    while num != -1:
        try:
            num = float(input("Please enter a score between {} and {}, (-1 to exit)").format(MIN,MAX))
            if num==-1:
              break
            elif num<MIN or num>MAX:
                raise ValueError("Score is out of range, it must be between {} and {}".format(MIN,MAX))
            else:
                scores.append(num)
        except ValueError as err:
            print(err)
    all_scores = kwargs["first_name"], kwargs["last_name"], scores

    write_to_file(all_scores)

def read_from_file():
    file_dir = os.path.dirname(__file__)
    f = open(os.path.join(file_dir, FILE_NAME), "r")
    line1 = f.read()
    print(line1)
    f.close()


if __name__ == '__main__':
    get_student_info(first_name="Viktoriia", last_name="Denys")
    get_student_info(first_name="Bret", last_name="Gorre")
    # read_from_file()

    input('Press any key to end')