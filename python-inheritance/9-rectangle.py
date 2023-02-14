#!/usr/bin/python3
'''class basegeometry'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry
'''class rectangle inherits the class basegeometry'''


class Rectangle(BaseGeometry):
    '''method'''
    def __init__(self, width, height):
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)
    '''method'''
    def area(self):
        '''return area'''
        return self.__width * self.__height
    '''method'''
    def __str__(self):
        '''return print str'''
        return str("[Rectangle] {}/{}".format(self.__width, self.__height))
