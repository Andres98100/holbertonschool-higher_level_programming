#!/usr/bin/python3
'''import'''
import json
'''function write in a jason'''


def save_to_json_file(my_obj, filename):
    '''statement'''
    with open(filename, "w") as file:
        '''json'''
        file.write(json.dumps(my_obj))
