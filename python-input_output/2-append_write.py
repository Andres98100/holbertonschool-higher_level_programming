#!/usr/bin/python3
'''function append text a in file txt'''


def append_write(filename="", text=""):
    '''statement'''
    with open(filename, "a", encoding="utf-8") as file:
        file.write(text)
    '''return'''
    return len(text)
