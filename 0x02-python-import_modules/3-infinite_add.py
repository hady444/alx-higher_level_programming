#!/usr/bin/python3
import sys

import sys
if __name__ != "__main__":
    exit()

i = 1
summ = 0
for arg in sys.argv:
    if i != 1:
        summ += int(arg)
        continue
    i += 1
print(summ)
