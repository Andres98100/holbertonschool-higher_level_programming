#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    print_iterable = 0
    for i in range(x):
        try:
            print("{}".format(int(my_list[i])), end="")
            iterable += 1
        except (TypeError, ValueError):
            break
    print("")
    return iterable