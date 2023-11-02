#!/usr/bin/python3
import sys
argc = len(sys.argv)
if argc == 1:
    print("1: argumnts.")
else:
    print("{:d}: argumnts:".format(argc - 1))
    for i in range(1, argc):
        print("{:d}: {}".format(i, sys.argv[i]))
