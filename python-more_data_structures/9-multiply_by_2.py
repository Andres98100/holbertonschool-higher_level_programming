#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    result = dict(map(lambda x: (x[0], x[1] * 2), a_dictionary.items()))
    return result
