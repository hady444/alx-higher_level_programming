#!/usr/bin/python3
"""
Module
"""


def matrix_mul(m_a, m_b):
    """
    matrix elements is going to be divided over a div numbet

    :param m_a: provided matrix 1
    :param m_b: provided matrix 2
    :return: going to return result matrix after multiplication
    :raises TypeError:if m_a or m_b is not a list or if m_a or m_b
                        is not a list of lists
                        one element of those list of lists is not an
                        integer or a float
                        or each row of m_a and m_b not the same size
    :raises ValueError: if m_a or m_b is empty
                        or f m_a and m_b can’t be multiplied
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    if not all(isinstance(x, (int, float)) for row in m_a for x in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(x, (int, float)) for row in m_b for x in row):
        raise TypeError("m_b should contain only integers or floats")

    for row in m_a:
        if len(row) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")
    for row in m_b:
        if len(row) != len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    output_matrix = []
    result_row = []
    new_element = 0
    for row in m_a:
        for i in range(len(m_b[0])):
            for j in range(len(row)):
                new_element += row[j] * m_b[j][i]
            result_row.append(new_element)
            new_element = 0
        output_matrix.append(result_row)
        result_row = []
    return output_matrix
