#!/usr/bin/python3
def uppercase(str):
    for c in str[0:-1]:
        print("{}".format(chr(ord(c) - (ord('a') - ord('A')))), end='')
    print("{}".format(chr(ord(str[-1]) - (ord('a') - ord('A')))))
