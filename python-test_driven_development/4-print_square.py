#!/usr/bin/python3
'''function print #'''


def print_square(size):
    '''validations'''
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    '''print #'''
    for i in range(size):
        print("#" * size)
