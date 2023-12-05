#!/usr/bin/python3
"""Module"""


def load_from_json_file(filename):
    """
    creates an Object from a “JSON file”
    Args:
        filename (str): json file extention
    """
    import json
    return (json.load(filename))
