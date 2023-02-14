#!/usr/bin/python3
'''function read txt'''


def read_file(filename=""):
    '''statement'''
    with open(filename, encoding="utf-8") as file:
        '''read lines'''
        for line in file:
            print(line, end="")
    print()
