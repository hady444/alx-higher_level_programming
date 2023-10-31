#!/usr/bin/python3
for i in range(9):
    j = i + 1
    while (j < 10):
        if i * 10 + j == 89:
            print(89)
            break
        print("{:02d}".format(i * 10 + j), end=', ')
        j += 1
