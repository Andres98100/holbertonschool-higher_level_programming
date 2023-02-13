#!/usr/bin/python3
'''function print if the obj is a instance or a class that inherited'''


def inherits_from(obj, a_class):
    '''condition'''
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    else:
        '''return false or true'''
        return False
