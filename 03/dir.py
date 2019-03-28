import os
import sys

def print_all_files(path):
    current_files = os.listdir(path)
    for file_name in current_files:
        full_file_name = os.path.join(path, file_name)
        print(full_file_name)
 
        if os.path.isdir(full_file_name):
            next_level_files = print_all_files(full_file_name)

def test():
    path = r"E:\_teach\_course\2018-2019第2学期\Python数据处理编程\exercise"
    print_all_files(path)

def main():
    if len(sys.argv) == 1:
        path = os.path.dirname(os.path.abspath(__file__))
        print_all_files(path)
    else: 
        for path in sys.argv[1:]:
            if os.path.isabs(path):
                print_all_files(path)
            else:
                abspath = os.path.join(os.path.dirname(os.path.abspath(__file__)),path)
                print_all_files(path)


if __name__ == "__main__":
    # test()
    main()
