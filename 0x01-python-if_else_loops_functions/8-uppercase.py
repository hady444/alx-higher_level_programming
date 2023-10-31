#!/usr/bin/python3
def uppercase(str):
    str += '\n'
    for c in str:
        if ord(c) in range(97, 123):
            print("{}".format(chr(ord(c) - (ord('a') - ord('A')))), end='')
        else:
            print("{}".format(c), end='')
