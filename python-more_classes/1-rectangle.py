#!/usr/bin/python3
'''class'''


class Rectangle:
    '''method function'''
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
    '''decorator'''
    @property
    def get_width(self):
        '''return  attribute'''
        return self.__width
    '''decorator'''
    @get_width.setter
    def width(self, value):
        '''validation'''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        '''assign value'''
        self.__width = value
    '''decorator'''
    @property
    def get_height(self):
        '''return attribute'''
        return self.__height
    '''decorator'''
    @get_height.setter
    def height(self, value):
        '''validation'''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        '''assign value'''
        self.__height = value
