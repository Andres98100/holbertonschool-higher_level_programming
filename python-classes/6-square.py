#!/usr/bin/python3
'''a class called square is initialized'''


class Square:
    '''a private instance is made to an attribute with the name size'''
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position
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
    '''private instance of the attribute is returned'''
    @property
    def get_position(self):
        return self.__position

    @get_position.setter
    def position(self, value):
        if not isinstance(value, tuple) or \
           not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        '''if the size is equal to 0, an empty line is printed'''
        if self.__size == 0:
            print("")
        else:
            '''the number of spaces sent to position 0 is printed'''
            '''is iterated size times and then
            multiplied by the size to create the square'''
            for i in range(self.__position[1]):
                    print("")
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
