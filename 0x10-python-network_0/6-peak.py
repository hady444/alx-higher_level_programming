#!/usr/bin/python3
"""Module"""


def find_peak(list_of_integers):
    """finds a peak in a list of unsorted integers"""
    if not list_of_integers:
        return None
    length = len(list_of_integers)
    if length == 1:
        return list_of_integers[0]
    else:
        if list_of_integers[-1] >= list_of_integers[-2]:
            return list_of_integers[-1]
        elif list_of_integers[0] >= list_of_integers[1]:
            return list_of_integers[0]
        else:
            for i in range(1, length - 1):
                if (list_of_integers[i] >= list_of_integers[i + 1] and
                        list_of_integers[i] >= list_of_integers[i - 1]):
                    return list_of_integers[i]
        return list_of_integers[0]
