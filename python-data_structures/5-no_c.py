#!/usr/bin/python3


def no_c(my_string: str):
    new_string = ''
    for c in my_string:
        if c != 'c' or c != 'C':
            new_string += c

    return new_string
