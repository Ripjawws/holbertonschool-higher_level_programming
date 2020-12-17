#!/usr/bin/python3
def roman_to_int(roman_string):
    Roman_dict = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9,
                  'X': 10, 'XL': 40, 'L': 50, 'XC': 90,
                  'C': 100, 'CD': 400, 'D': 500, 'DM': 900,
                  'M': 1000}
    result = 0
    i = 0
    if roman_string is not None and type(roman_string) is str:
        while i < len(roman_string):
            if Roman_dict.get(roman_string[i: i+2]) is not None:
                result += Roman_dict.get(roman_string[i: i+2])
                i = i + 2
            else:
                result += Roman_dict.get(roman_string[i])
                i += 1
    return result
