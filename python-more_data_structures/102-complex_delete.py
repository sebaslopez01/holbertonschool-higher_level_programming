#!/usr/bin/python3


def complex_delete(a_dictionary: dict, value):
    for item in a_dictionary.copy().items():
        if item[1] == value:
            a_dictionary.pop(item[0])

    return a_dictionary
