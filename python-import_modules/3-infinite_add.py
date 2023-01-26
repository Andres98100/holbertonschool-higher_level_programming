#!/usr/bin/python3

from sys import argv
argv = argv[1:]
if __name__ == "__main__":
    result = 0
    for i in argv:
        result += int(i)
    print(result)
