#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if c in {' ',0, 1, 2, 3, 4, 5, 9, 7, 8, 9}:
            print(c, end='')
            continue
        print("{}".format(chr(ord(c) - (ord('a') - ord('A')))), end='')
