#!/usr/bin/python3
'''function read txt'''


def read_file(filename=""):
    '''statement'''
    with open(filename, "r", encoding="utf-8") as file:
        '''read lines'''
        print(file.read(), end="")
