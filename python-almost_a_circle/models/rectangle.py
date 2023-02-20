#!/usr/bin/python3
'''import'''
Base = __import__('base').Base
'''class'''


class Rectangle(Base):
    '''method'''
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
    '''decorators'''
    @property
    def width(self):
        '''return'''
        return self.__width
    '''decorators'''
    @width.setter
    def width(self, value):
        '''assignment'''
        self.__width = value
    '''decorators'''
    @property
    def height(self):
        '''return'''
        return self.__height
    '''decorators'''
    @height.setter
    def height(self, value):
        '''assignment'''
        self.__height = value
    '''decorators'''
    @property
    def x(self):
        '''return'''
        return self.__x
    '''decorators'''
    @x.setter
    def x(self, value):
        '''assignment'''
        self.__x = value
    '''decorators'''
    @property
    def y(self):
        '''return'''
        return self.__y
    '''decorators'''
    @width.setter
    def width(self, value):
        '''assignment'''
        self.__y = value