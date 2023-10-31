#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if c == ' ':
            print(" ")
            continue
        print("{}".format(chr(ord(c) - (ord('a') - ord('A')))), end='')
