#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i, r = 0, 0
    while i < x:
        try:
            print("{:d}".format(my_list[i]), end="")
            r += 1
        except (TypeError, ValueError) as ex:
            pass
        i += 1
    print()
    return r
