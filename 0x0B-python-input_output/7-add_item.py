#!/usr/bin/python3
"""
Script that adds all arguments to a Python list and saves them to a file.
"""
from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"

my_list = []
try:
    my_list = load_from_json_file(filename)
except Exception:
    save_to_json_file(my_list, filename)

argc = len(argv)

if argc > 1:
    for i in range(1, argc):
        my_list.append(argv[i])
    save_to_json_file(my_list, filename)
