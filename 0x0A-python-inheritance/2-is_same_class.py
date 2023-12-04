#!/usr/bin/python3
"""
is object from this class
"""


def is_same_class(obj, a_class):
    """check if object from provided class

    Args:
        obj: object passed
        a_class: class
    Return:
        True if in
        False if out
    """
    return (type(obj) == a_class))
