#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    print_iterable = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            print_iterable += 1
        except IndexError:
            break
    print("")
    return print_iterable
