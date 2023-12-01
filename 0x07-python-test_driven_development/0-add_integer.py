#!/usr/bin/python3
"""
Module
"""


def add_integer(a, b=98):
    """
    add_integer
    """
    if not isinstance(a, int) or not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) or not isinstance(b, float):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
