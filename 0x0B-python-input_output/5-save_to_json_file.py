#!/usr/bin/python3
"""Module"""


def save_to_json_file(my_obj, filename):
    """
    writes an Object to a text file, using a JSON representation.
    Args:
        my_obj (str): string passed
        filename (str): json file extention to save to
    """
    import json
    with open(filename, mode="r") as f:
        f.write(json.dumbs(my_obj))
