#!/usr/bin/python3
'''import'''
import json
'''function  creates an Object from a json'''


def load_from_json_file(filename):
    with open(filename, "r") as file:
        data = json.loads(file.read())
    return data