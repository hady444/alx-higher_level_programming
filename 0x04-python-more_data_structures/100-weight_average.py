#!/usr/bin/python3
def weight_average(my_list=[]):
    numenator, denomenator, avg = 0, 0, 0
    if my_list:
        for i in my_list:
            numenator += i[0] * i[1]
            denomenator += i[1]
        avg = numenator / denomenator
    return avg
