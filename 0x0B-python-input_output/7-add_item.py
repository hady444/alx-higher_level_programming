#!/usr/bin/python3
"""Module"""
from os import path
import json
from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


pairs = []
if os.path.exists("add_item.json")
prev_content = load_from_json_file("add_item.json")
for index in argv[1:]:
    pairs.append(index)
save_to_json_file(pairs, "add_item.json")
