#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        last = number % 10
    else:
        last = abs(number) % 10
    print("{}".format(last), end="")
    return last
def main():
    print_last_digit(98)
    print_last_digit(0)
    r = print_last_digit(-1024)
    print(r)
main()