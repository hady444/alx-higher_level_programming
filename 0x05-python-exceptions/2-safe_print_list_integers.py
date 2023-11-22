#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    r = 0
    for i in my_list[:x]:
        if isinstance(i, int):
            try:
                print("{:d}".format(i), end="")
                r += 1
            except (TypeError, ValueError) as ex:
                continue
    print()
    return r
