#!/usr/bin/python3
def weight_average(my_list=[]):
    numenator, denomenator = 0, 0
    for i in my_list:
        numenator += i[0] * i[1]
        denomenator += i[1]
    return numenator / denomenator
