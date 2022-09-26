#!/usr/bin/python3

def update_dictionary(a_dictionary: dict, key: str, value):
    new_dict = a_dictionary.copy()

    new_dict[key] = value

    return new_dict
