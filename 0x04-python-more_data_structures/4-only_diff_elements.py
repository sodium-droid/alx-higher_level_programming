#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    complete = set_1.union(set_2)
    return [value for value in complete if value not in set_1 & set_2]
