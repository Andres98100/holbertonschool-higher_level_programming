#!/usr/bin/python3
'''class'''


class Student:
    '''method'''
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    '''function'''
    def to_json(self):
        '''return'''
        return self.__dict__
