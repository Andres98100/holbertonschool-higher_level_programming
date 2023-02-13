#!/usr/bin/python3
'''function print if the obj is a instance or a class that inherited'''


def inherits_from(obj, a_class):
    '''condition'''
    if not isinstance(obj, a_class) and not issubclass(a_class):
        return False
    else:
        '''return false or true'''
        return True