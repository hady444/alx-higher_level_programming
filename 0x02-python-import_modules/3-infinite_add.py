#!/usr/bin/python3
import sys
#if __name__ != "main":
#    exit()

argc = len(sys.argv)
i = 1
summ = 0
for arg in sys.argv:
    if i == 1:
        i += 1
        continue
    if arg == ' ':
        i += 1
        continue
    summ += int(arg)
    i += 1
print(summ)
