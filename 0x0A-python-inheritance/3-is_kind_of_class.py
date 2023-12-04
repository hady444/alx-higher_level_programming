#!/usr/bin/python3
"""
is object from this class
"""


def is_kind_of_class(obj, a_class):
    """check if object from provided class

    Args:
        obj: object passed
        a_class: class
    Return:
        True if in
        False if out
    """
    return (isinstance(obj, a_class))
