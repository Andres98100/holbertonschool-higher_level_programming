#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position
    @property
    def get_size(self):
        return self.__size
    @get_size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    @property
    def get_position(self):
        return self.__position
    @get_position.setter
    def position(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__position = value
    def area(self):
        return self.__size * self.__size
    def my_print(self):
        if self.__size < 0:
            print("")
        else:
            for i in range(self.__size):
                print("_" * self.__position[0] + "#" * self.__size)
