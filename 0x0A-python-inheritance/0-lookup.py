#!/usr/bin/python3
"""Look up method
"""


def lookup(obj):
    """returns the list of available attributes and methods of an object

    Args:
        obj: object passed

    Returns:
        list: a list of available attributes and methods of an object
    """
    return (dir(obj))
