#!/usr/bin/python3
"""Module"""


def pascal_triangle(n):
    if n <= 0:
        return []
    tr = [[1]]
    for i in range(1, n):
        tr.append([])
        tr[i].append(1)
        for j in range(i-1):
            tr[i].append(tr[i-1][j] + tr[i-1][j+1])
        tr[i].append(1)
    return (tr)
