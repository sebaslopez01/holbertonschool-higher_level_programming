#!/usr/bin/python3


def multiply_by_2(a_dictionary: dict):
    new_dict = a_dictionary.copy()

    for item in new_dict.items():
        new_dict[item[0]] = item[1] * 2

    return new_dict
