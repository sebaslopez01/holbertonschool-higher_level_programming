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

    count = 0

    for i, char in enumerate(roman_string):
        if i > 0:
            if char == 'V' and roman_string[i - 1] == 'I':
                count += 3
                continue
            elif char == 'X' and roman_string[i - 1] == 'I':
                count += 8
                continue
        count += roman_dict.get(char, 0)

    return count
