#!/usr/bin/python3
def roman_to_int(roman_string):
    number = 0 
    Romans = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D': 500, 'M':1000}
    for i, N in enumerate(roman_string):
        if N in Romans.keys():
            if i != 0:
                prev = roman_string[i - 1]
                if Romans.get(N) > Romans.get(prev):
                    number += (Romans.get(N) - (2 * Romans.get(prev)))
                    continue
            number += Romans.get(N)
        else:
            return None
    return number
