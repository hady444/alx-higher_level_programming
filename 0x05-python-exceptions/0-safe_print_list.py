#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    r = 0
    for i in my_list[:x]:
        try:
            print("{}".format(i), end="")
            r += 1
        except (ValueError, TypeError) as e:
            continue
    print()
    return (r)
