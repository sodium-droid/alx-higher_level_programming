#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    rom_dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    size = len(roman_string)
    for i in range(len(roman_string)):
        cur_val = rom_dic[roman_string[i]]
        nxt_val = rom_dic[roman_string[i + 1]] if i + 1 < size else 0
        if cur_val < nxt_val:
            result -= cur_val
        else:
            result += cur_val
    return result
