#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None:
        return None
    sorted_dict = {key: value for key, value in sorted(a_dictionary.items(), key=lambda item: item[1])}
    return list(sorted_dict.keys())[-1]
a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
best_key = best_score(a_dictionary)
print("Best score: {}".format(best_key))

best_key = best_score(None)
print("Best score: {}".format(best_key))
