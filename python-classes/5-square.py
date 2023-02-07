#!/usr/bin/python3
'''a class called square is initialized'''


class Square:
    '''a private instance is made to an attribute with the name size'''
    def __init__(self, size=0):
        self.size = size
    '''private instance of the attribute is returned'''
    @property
    def get_size(self):
        return self.__size

    @get_size.setter
    def size(self, value):
        '''raise an error if the data type is incorrect'''
        if not isinstance(value, int):
            raise TypeError("size must be an intege")
        '''raise an error if the data is less that 0'''
        if value < 0:
            raise ValueError("size must be >= 0")
        '''is instantiated with the value'''
        self.__size = value
    '''returns the current square area'''
    def area(self):
        return self.__size * self.__size
    '''the square is printed according to size'''
    def my_print(self):
        '''if the size is equal to 0, an empty line is printed'''
        if self.__size == 0:
            print("")
        else:
            '''is iterated size times and then
            multiplied by the size to create the'''
            for i in range(self.__size):
                print("#" * self.__size)
