#!/usr/bin/python3
import sys
if __name__ != "__main__":
    exit()

argc = len(sys.argv)
if argc == 1:
    print("0: argumnts.")
else:
    print("{:d}: argumnts:".format(argc - 1))
    for i in range(1, argc):
        print("{:d}: {}".format(i, sys.argv[i]))
