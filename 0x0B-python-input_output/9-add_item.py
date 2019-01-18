#!/usr/bin/python3
import json
from sys import argv
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

try:
    py_list = load_from_json_file('add_item.json')
except FileNotFoundError:
    py_list = []
py_list.extend(argv[1:])
save_to_json_file(py_list, 'add_item.json')
