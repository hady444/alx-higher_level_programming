#!/usr/bin/python3
def uppercase(str):
    for i, c in enumerate(str):
        if ord(c) in (97, 123):
            print("{}".format(chr(ord(c) - (ord('a') - ord('A')))), end='')
        else:
            print("{}".format(c), end='')
