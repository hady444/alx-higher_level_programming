#!/usr/bin/python3
def islower(c):
    if ord(c) in (97, 123):
        print(f"{c} is lower")
    elif ord(c) in (65, 91):
        print(f"{c} is upper")
