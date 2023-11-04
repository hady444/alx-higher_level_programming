#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for l in matrix:
        for e in l:
            print("{:d}".format(e), end=' ')
        print("$")
