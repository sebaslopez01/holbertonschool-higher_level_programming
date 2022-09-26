#!/usr/bin/python3


def roman_to_int(roman_string: str) -> int:
    if not isinstance(roman_string, str):
        return 0

    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    return sum(map(lambda x: roman_dict.get(x, 0), roman_string))
