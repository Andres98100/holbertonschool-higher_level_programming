#!/usr/bin/python3
'''import class'''


Rectangle = __import__('9-rectangle').Rectangle
'''class'''


class Square(Rectangle):
    '''method'''
    def __init__(self, size):
        '''method super class'''
        super().__init__(size, size)
        '''validator'''
        self.__size = self.integer_validator("size", size)
