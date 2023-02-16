#!/usr/bin/python3
'''import'''
import json
'''function  creates an Object from a json'''


def load_from_json_file(filename):
    '''open json'''
    with open(filename, "r") as file:
        '''load json'''
        data = json.loads(file.read())
    '''return'''
    return data
