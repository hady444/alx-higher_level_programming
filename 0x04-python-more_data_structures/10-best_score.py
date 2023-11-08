#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None:
        return None
    sorted_dict = {key: value for key, value in sorted(a_dictionary.items(), key=lambda item: item[1])}
    return list(sorted_dict.keys())[-1]
