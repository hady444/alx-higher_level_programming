#!/usr/bin/python3
"""
Module
"""


def matrix_divided(matrix, div):
    """
    matrix elements is going to be divided over a div numbet

    :param matrix: provided matrix
    :param div: number to divide over
    :return: going to return result matrix after division
    :raises TypeError: if the matrix is empty or none or contain no
    int or float elements or div is neither not int or float
    :raises ZeroDivisionError: if div = 0
    """
    result = []
    em = "matrix must be a matrix (list of lists) of integers/floats"
    if not matrix:
        raise TypeError(em)
    if not isinstance(matrix, list):
        raise TypeError(em)
    for lists in matrix:
        if not isinstance(lists, list):
            raise TypeError(em)
        for item in lists:
            if not isinstance(item, int) and not isinstance(item, float):
                raise TypeError(em)
    for lists in matrix:
        if len(lists) == 0:
            raise TypeError(em)
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    row = []
    row_len = len(matrix[0])
    for ls in matrix:
        if row_len != len(ls):
            raise TypeError("Each row of the matrix must have the same size")
        for x in ls:
            row.append(round(x / div, 2))
        result.append(row)
        row = []
    return result
