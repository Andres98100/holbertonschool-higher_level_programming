#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        self.__size = size
    @property
    def get_size(self):
        return self.__size
    @get_size.setter
    def size(self, value):
        if not isinstance(value, int):
            print("size must be an intege")
        if value < 0:
            print("size must be >= 0")
        self.__size = value
    def area(self):
        return self.__size 
    