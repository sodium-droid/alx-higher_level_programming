#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    max = 0
    for i in my_list:
        if int(i) > max:
            max = int(i)
    return max
