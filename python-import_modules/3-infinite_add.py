#!/usr/bin/python3

from sys import argv
argv = argv[1:]
if __name__ == "__main__":
    for result in argv:
        result += int(argv)
    print(result)
