#!/usr/bin/python3


def no_c(my_string: str):
    for i, c in enumerate(my_string):
        if c == 'c' or c == 'C':
            del my_string[i]
