#!/usr/bin/python3
'''
an empty class is initialized
'''
class Square:
    def __init__(self, size):
        self.__size = size
    def get_size(self):
        return self.__size
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    def area(self):
        return self.__size * self.__size