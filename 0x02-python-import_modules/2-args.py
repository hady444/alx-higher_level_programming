#!/usr/bin/python3
import sys
if __name__ != "__main__":
    exit()

argc = len(sys.argv)
arg_S = "{:d}: argument".format(argc - 1)
if argc == 1:
    arg_S += "s."
elif argc == 2:
    arg_S += ":"
else:
    arg_S += "s:"
print(arg_S)
for i in range(1, argc):
    print("{:d}: {}".format(i, sys.argv[i]))
