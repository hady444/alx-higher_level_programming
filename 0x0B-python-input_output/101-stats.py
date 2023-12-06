#!/usr/bin/python3
"""Module"""
from sys import stdin


def print_stats(file_size, status_code):
    print(f"File size: {file_size}")
    for key, val in sorted(status_code.items()):
        if val > 0:
            print("{:s}: {:d}".format(key, val))


status_code = {
            '200': 0,
            '301': 0,
            '400': 0,
            '401': 0,
            '403': 0,
            '404': 0,
            '405': 0,
            '500': 0
            }
file_size = 0
i = 0
try:
    for line in stdin:
        line = line.split()
        if len(line) >= 2:
            if line[-2] in status_code:
                status_code[line[-2]] += 1
            file_size += int(line[-1].split("\n")[0])
            if i % 10 == 0 and i != 0:
                print_stats(file_size, status_code)
        i += 1
    print_stats(file_size, status_code)
except KeyboardInterrupt as ex:
    print_stats(file_size, status_code)
