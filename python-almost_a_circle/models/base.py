#!/usr/bin/python3
'''import'''
import json
import os.path
'''class'''


class Base:
    '''private attribute'''
    __nb_objects = 0
    '''method constructor'''
    def __init__(self, id=None):
        '''conditional'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''validation'''
        if list_objs is None:
            list_objs = []
        '''variable'''
        filename = cls.__name__ + ".json"
        new_list = []
        '''open json'''
        with open(filename, "w") as file:
            '''iterates list_objs'''
            for i in list_objs:
                new_list.append(i.to_dictionary())
            '''write in the file json'''
            data = Base.to_json_string(new_list)
            file.write(data)

    @staticmethod
    def from_json_string(json_string):
        '''validation'''
        if json_string is None or len(json_string) == 0:
            return []
        '''return'''
        return json.loads(json_string)
