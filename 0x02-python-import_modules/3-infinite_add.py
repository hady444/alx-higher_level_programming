#!/usr/bin/python3
import sys
if __name__ != "main":
    exit()

i = 1
summ = 0
for arg in sys.argv:
    if i != 1:
        summ += int(arg)
        continue
    i += 1
print("{:d}".format(summ))
