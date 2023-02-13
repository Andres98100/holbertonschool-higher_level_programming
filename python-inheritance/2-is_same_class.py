#!/usr/bin/python3
'''function return true or false'''


def is_same_class(obj, a_class):
    '''variable flag'''
    flag = False
    '''conditional'''
    if isinstance(obj, a_class):
        flag = True
    '''return false or true'''
    return flag
