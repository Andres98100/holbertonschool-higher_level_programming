#!/usr/bin/python3
'''function write in a file txt'''


def write_file(filename="", text=""):
    '''statement'''
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)
    '''return'''
    return len(text)
