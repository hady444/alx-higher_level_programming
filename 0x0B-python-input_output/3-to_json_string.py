#!/usr/bin/python3
"""Module"""


def to_json_string(my_obj):
    """ convert string to json
    Args:
        my_obj (str): string provided

    Return:
        Json representation of an object
    """
    import json
    return (json.dumps(my_obj))
