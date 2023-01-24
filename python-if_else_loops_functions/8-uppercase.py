#!/usr/bin/python3
def uppercase(str):
    if str <= 97 and str > 122:
        str -= 32
    print("{}".format(str))
    return str
