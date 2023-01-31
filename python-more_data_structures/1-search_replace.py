#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list[:]
    for i in range(len(my_list)):
        if search == new_list[i]:
            new_list[i] = replace
    return new_list
