#!/usr/bin/python3
'''function return true or false'''


def is_same_class(obj, a_class):
    '''variable flag'''
    flag = True
    '''conditional'''
    if not isinstance(obj, a_class):
        flag = False
    '''return false or true'''
    return flag
