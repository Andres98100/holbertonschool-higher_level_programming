#!/usr/bin/python3
'''class'''


class Base:
    '''private attribute'''
    __nb_objects = 0
    '''method constructor'''
    def __init__(self, id=None):
        '''conditional'''
        if not id is None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
