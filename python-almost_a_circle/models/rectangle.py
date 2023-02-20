#!/usr/bin/python3
'''import'''
from models.base import Base
'''class'''


class Rectangle(Base):
    '''method'''
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''return'''
        return self.__width

    @width.setter
    def width(self, value):
        '''validation'''
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        '''assignment'''
        self.__width = value

    @property
    def height(self):
        '''return'''
        return self.__height

    @height.setter
    def height(self, value):
        '''validation'''
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        '''assignment'''
        self.__height = value

    @property
    def x(self):
        '''return'''
        return self.__x

    @x.setter
    def x(self, value):
        '''validation'''
        if type(value) != int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        '''assignment'''
        self.__x = value

    @property
    def y(self):
        '''return'''
        return self.__y

    @y.setter
    def y(self, value):
        '''validation'''
        if type(value) != int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        '''assignment'''
        self.__y = value
