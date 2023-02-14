#!/usr/bin/python3
'''class'''


class BaseGeometry:
    '''method'''
    def area(self):
        '''exception'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''validation'''
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        return value
