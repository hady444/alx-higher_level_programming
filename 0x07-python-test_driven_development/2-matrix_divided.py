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
    if (not all(isinstance(row, list) for row in matrix) or
        not all(isinstance(val, (int, float)) for row in matrix for val in row) or
        len(matrix) == 0 or
        any(len(row) == 0 for row in matrix)):
        raise TypeError(em)
    row_len = len(matrix[0])
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    row = []
    for ls in matrix:
        if row_len != len(ls):
            raise TypeError("Each row of the matrix must have the same size")
        for x in ls:
            row.append(format(x / div, '.2f'))
        result.append(row)
        row = []
    return result
