#!/usr/bin/python3
def uppercase(str):
    upper = ""
    for char in str:
        char_ord = ord(char)
        if ord(char) >= 97 and ord(char) <= 122:
            upper += chr(char_ord - 32)
        else:
            upper += char
    print("{}".format(upper))
