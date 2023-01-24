#!/usr/bin/python3
def uppercase(str):
    if str <= 97 and str > 122:
        str -= 32
    print("{}".format(str))
    return str
def main():
    uppercase("best")
    uppercase("Best School 98 Battery street")
main()