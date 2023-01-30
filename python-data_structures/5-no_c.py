#!/usr/bin/python3
def no_c(my_string):
    str_aux = ""
    for i in my_string:
        if i != 'c' and i != 'C':
            str_aux += i
    return str_aux
