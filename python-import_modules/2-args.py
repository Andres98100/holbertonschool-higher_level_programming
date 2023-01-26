#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    argv = argv[1:]
    if len(argv) == 0:
        print("{} arguments.".format(len(argv)))
    else:
        if len(argv) == 1:
            print("{} argument:".format(len(argv)))
        else:
            print("{} arguments:".format(len(argv)))
        for i, arg in enumerate(argv, 1):
            print("{}: {}".format(i, arg))
