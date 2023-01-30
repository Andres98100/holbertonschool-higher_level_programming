#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0 and idx > my_list:
        return my_list
    my_list[idx] = element
    return my_list
