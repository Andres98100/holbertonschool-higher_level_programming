#!/usr/bin/python3
'''a class called square is initialized'''


class Square:
    '''a private instance is made to an attribute with the name size'''
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position
    '''private instance of the attribute is returned'''
    @property
    def size(self):
        return self._size
    '''raise an error if the data type is incorrect'''
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        '''raise an error if the data is less that 0'''
        if value < 0:
            raise ValueError("size must be >= 0")
        '''is instantiated with the value'''
        self._size = value
    '''private instance of the attribute is returned'''
    @property
    def position(self):
        return self._position
    '''raise an error if the data type is incorrect'''
    @position.setter
    def position(self, value):
        '''validates that position is a tuple and is a positive integer'''
        if not isinstance(value, tuple) or len(value) != 2 or \
           not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        '''is instantiated with the value'''
        self._position = value
    '''returns the current square area'''
    def area(self):
        return self._size * self._size
    '''the square is printed according to size '''
    def my_print(self):
        '''if the size is equal to 0, an empty line is printed'''
        if self._size == 0:
            print("")
        else:
            '''the number of spaces sent to position 0 is printed'''
            '''is iterated size times and then
            multiplied by the size to create the square'''
            for i in range(self._position[1]):
                    print("")
            for i in range(self._size):
                print(" " * self._position[0] + "#" * self._size)
