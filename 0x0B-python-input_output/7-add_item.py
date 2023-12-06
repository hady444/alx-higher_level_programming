#!/usr/bin/python3
"""Module"""

import os.path
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

arguments = sys.argv[1:]
try:
    js_list = load_from_json_file("add_item.json")
except:
    js_list = []
for arg in arguments:
    js_list.append(arg)
js_list = save_to_json_file(js_list, "add_item.json")
