#!/usr/bin/python3
'''function add two integers'''


def add_integer(a, b=98):
    '''checks whether a is an integer or a float'''
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    '''checks whether b is an integer or a float'''
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    '''return the add'''
    return int(a) + int(b)
