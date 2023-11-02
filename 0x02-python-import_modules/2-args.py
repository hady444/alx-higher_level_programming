#!/usr/bin/python3
import sys
if __name__ != "__main__":
    exit()

argc = len(sys.argv)
print("{:d}: argumnts".format(argc - 1), end='')
if argc == 1:
    print(".")
else:
    print(":")
    for i in range(1, argc):
        print("{:d}: {}".format(i, sys.argv[i]))
