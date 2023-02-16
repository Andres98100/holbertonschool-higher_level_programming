#!/usr/bin/python3
'''import'''
import sys
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
'''function add list'''



def add_list():
    '''variables'''
    args = sys.argv
    my_list = []
    filename = "add_item.json"
    '''open json'''
    with open(filename, 'r') as f:
        '''my list'''
        my_list = []
        '''add my list'''
        my_list.extend(args[1:])
        '''save in the json'''
        save_to_json_file(my_list, filename)
        load_from_json_file(filename)
'''function'''
add_list()
