#!/usr/bin/python3
'''import'''
import json
'''function'''



def save_to_json_file(my_obj, filename):
    with open(filename, "w") as file:
        return json.dumps(my_obj)
