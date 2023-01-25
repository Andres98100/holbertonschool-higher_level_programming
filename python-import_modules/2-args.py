#!/usr/bin/python3
import sys
argv = sys.argv[1:]
if len(argv) == 0:
    print("{} arguments.".format(argv))
else:
    print("{} arguments.".format(argv))
    for i, arg in enumerate(argv, 1):
        print(i, ":", arg)
