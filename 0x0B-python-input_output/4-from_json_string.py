#!/usr/bin/python3
"""Module"""


def from_json_string(my_str):
    """ convert string to json
    Args:
        my_str (str): string provided

    Return:
        string representation of an object
    """
    import json
    return (json.loads(my_str))
