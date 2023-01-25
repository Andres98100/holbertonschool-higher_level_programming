#!/usr/bin/python3
for i in range(122, 97-1, -1):
    if i % 2 == 1:
        i -= 32
    elif i % 3 == 0:
        i
    print("{}".format(chr(i)), end="")
