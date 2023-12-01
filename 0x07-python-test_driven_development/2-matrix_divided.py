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
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")
    return [[round(x / div, 2) for x in row] for row in matrix]
