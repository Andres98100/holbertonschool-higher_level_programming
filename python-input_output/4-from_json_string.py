#!/usr/bin/python3
'''import'''
import json
'''function returns an object represented by a JSON'''


def from_json_string(my_str):
    '''return'''
    return json.loads(my_str)
