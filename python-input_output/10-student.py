#!/usr/bin/python3
'''class'''


class Student:
    '''method'''
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    '''function'''
    def to_json(self, attrs=None):
        '''validation'''
        if attrs is None:
            return self.__dict__
        else:
            new_dict = {}
            '''iterates the list'''
            for key, value in self.__dict__.items():
                if key in attrs:
                    new_dict[key] = value
            '''return'''
            return new_dict
