#!/usr/bin/python3
def find_dimensions(lst):
    if not isinstance(lst, list):
        return 0
    if not lst:
        return 1
    inner_dimension = find_dimensions(lst[0])
    return inner_dimension + 1

def matrix_divided(matrix, div):
    result = []
    if find_dimensions(matrix) != 2:
        raise TypeError("matrix must be a matrix (list of lists) " +\
                "of integers/floats")
    l = len(matrix[0])
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    row = []
    for ls in matrix:
        if l != len(ls):
            raise TypeError("Each row of the matrix must have the same size")
        for x in ls:
            if not isinstance(x, int) and not isinstance(x, float):
                raise TypeError("matrix must be a matrix (list of lists) " +\
                        "of integers/floats")
            row.append(format(x/ div, '.2f'))
        result.append(row)
        row = []
    return result
