#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if (idx > 0) and (idx < len(my_list)):
        my_list.pop(idx)
    return (my_list)