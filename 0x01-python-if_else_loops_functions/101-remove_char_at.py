#!/usr/bin/python3
def remove_char_at(str, n):
    cp = ""
    for i, x in enumerate(str):
        if (i == n):
            continue
        cp += x
    return cp
