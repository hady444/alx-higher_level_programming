#!/usr/bin/python3
for i in range(10):
    j = i + 1
    while (j < 10):
        print("{:02d}".format(i * 10 + j), end=', ')
        j += 1
