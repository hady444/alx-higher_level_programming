#!/usr/bin/python3
import sys
argc = len(sys.argv)
print("{:d}: argumnts".format(argc), end='')
if argc == 1:
    print(".")
else:
    print(":")
    for i in range(1, argc):
        print("{:d}: {}".format(i, sys.argv[i]))
