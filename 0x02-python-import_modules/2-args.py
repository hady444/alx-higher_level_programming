#!/usr/bin/python3
import sys
if __name__ != "__main__":
    exit()

argc = len(sys.argv)
print("{:d}: argument".format(argc - 1), end='')
if argc == 1:
    print("s.")
elif argc == 2:
    print(":")
    print("{:d}: {}".format(1, sys.argv[1]))
else:
    print("s:")
    for i in range(1, argc):
        print("{:d}: {}".format(i, sys.argv[i]))
