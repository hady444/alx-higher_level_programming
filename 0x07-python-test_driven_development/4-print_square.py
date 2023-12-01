#!/usr/bin/python3
"""
Module
"""


def print_square(size):
    """function prits a square of #

    Args:
        size (int): the size length of the square
    Raises:
        TypeError: if size is not int or
                    (less than zero and float)
        ValueError: if less than zero only
    """
    if (isinstance(size, float) and size < 0) or not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size == 0:
        return
    if (size < 0):
        raise ValueError("size must be >= 0")
    my_result = []
    for _ in range(size):
        my_result.append(["#" * size])
    flattened_result = [str(item) for sublist in my_result for item in sublist]
    print('\n'.join(flattened_result))
