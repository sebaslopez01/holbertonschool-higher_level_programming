#!/usr/bin/python3

"""
This module defines add_integer function
"""


def add_integer(a, b=98):
    """ Adds to integers

    Args:
        a (:obj:`int`): First number to add
        b (:obj:`int`, optional): Second number to add

    Return:
        The two number added
    """
    if not isinstance(a, int) or not isinstance(a, float):
        raise TypeError('a must be an integer')
    if not isinstance(b, int) or not isinstance(b, float):
        raise TypeError('b must be an integer')

    return int(a) + int(b)
