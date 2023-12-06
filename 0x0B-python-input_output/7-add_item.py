#!/usr/bin/python3
"""Module"""


import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

arguments = sys.argv[1:]
js_list = [load_from_json_file("arg_item.json")]
for arg in arguments:
    js_list.append(arg)
js_list = save_to_json_file(js_list, "arg_item.json)
