#!/usr/bin/python3
def no_c(my_string):
    my_string = list(my_string)
    for i, letter in enumerate(my_string):
        if letter == 'c':
            my_string.pop(i)
    return (''.join(my_string))
