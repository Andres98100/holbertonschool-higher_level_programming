#!/usr/bin/python3
'''import'''
import sys
import os.path

'''import json'''
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

'''variable'''
args = sys.argv
filename = 'add_item.json'
'''function'''


def add_list():
    '''variable'''
    obj_list = []
    '''validation'''
    with open(filename, "a") as file:
        pass
    if os.stat(filename).st_size == 0:
        obj_list
    elif os.path.exists(filename):
        obj_list = load_from_json_file(filename)
    '''add args'''
    obj_list.extend(args[1:])
    '''save list'''
    save_to_json_file(obj_list, filename)
'''function'''
if __name__ == "__main__":
    add_list()
