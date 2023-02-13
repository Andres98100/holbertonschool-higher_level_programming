#!/usr/bin/python3
'''function print if is class or object'''


def is_kind_of_class(obj, a_class):
    '''conditional'''
    if not isinstance(obj, a_class):
        return False
    else:
        '''return false or true'''
        return True
