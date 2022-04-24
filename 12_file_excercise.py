# Write a Python program to read an entire text file.

def read_file(file_name):
    with open(file_name, 'r') as _file:
        print(_file.read())

read_file('work.txt')