#!/usr/bin/python3
'''function print first name and last name'''


def say_my_name(first_name, last_name=""):
    '''validations'''
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    '''return the first name and last name'''
    return print("My name is {} {}".format(first_name, last_name))
