#!/usr/bin/python3

"""
This module defines say_my_name function
"""


def print_square(size: int):
    """ Prints a square with the character #

    Args:
        size (:obj:`int`): Size length of the square
    """
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')

    for _ in range(size):
        print('#' * size, sep='')
