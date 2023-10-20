#!/usr/bin/python3
"""'7-add_item' module"""
import json
import sys
import os.path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

with open('add_item.json', 'a+') as f:
    if f.read() != '':
        lst = load_from_json_file('add_item.json')
        lst.extend(sys.argv[1:])
        save_to_json_file(lst, 'add_item.json')
    else:
        lst = []
        lst.extend(sys.argv[1:])
        save_to_json_file(lst, 'add_item.json')
