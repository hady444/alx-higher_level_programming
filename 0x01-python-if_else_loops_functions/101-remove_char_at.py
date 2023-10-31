#!/usr/bin/python3
def remove_char_at(str, n):
    cp = str
    for i, x in enumerate(str):
        if (i == n):
            continue
        print(x, end='')
