#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    k = sorted(a_dictionary.keys())
    for i in k:
        print("{}: {}".format(i, a_dictionary.get(i)))
