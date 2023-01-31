#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = list(set(my_list))
    result = 0
    for i in range(len(new_list)):
        result += new_list[i]
    return result
