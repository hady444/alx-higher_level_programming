#!/usr/bin/python3
def search_replace(my_list, search, replace):
    r = lambda x: replace if x == search else x
    return list(map(r, my_list))
