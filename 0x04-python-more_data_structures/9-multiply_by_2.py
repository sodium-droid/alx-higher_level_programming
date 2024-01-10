#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    keys = [x for x in a_dictionary.keys()]
    values = [x * 2 for x in a_dictionary.values()]
    new_dict = {key: value for key, value in zip(keys, values)}
    return new_dict
