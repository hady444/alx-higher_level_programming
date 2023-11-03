#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    m = my_list[0]
    i = -1
    while i < (len(my_list) - 1):
        i += 1
        if m < my_list[i]:
            m = my_list[i]
    return m
