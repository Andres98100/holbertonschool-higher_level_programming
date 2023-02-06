#!/usr/bin/python3
'''a class called square is initialized'''


class Square:
    '''a private instance is made to an attribute with the name size'''
    def __init__(self, size=0):
        self.__size = size
    '''private instance of the attribute is returned'''
    @property
    def get_size(self):
        return self.__size

    @get_size.setter
    def size(self, value):
        '''raise an error if the data type is incorrect'''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        '''raise an error if the data is less that 0'''
        if value < 0:
            raise ValueError("size must be >= 0")
        '''is instantiated with the value'''
        self.__size = value
    '''returns the current square area'''
    def area(self):
        return self.__size * self.__size
