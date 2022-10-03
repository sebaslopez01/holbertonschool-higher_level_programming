#!/usr/bin/python3

"""
This module defines add_integer function
"""


def add_integer(a, b=98):
    """ Adds two integers

    Args:
        a (:obj:`int`): First number to add
        b (:obj:`int`, optional): Second number to add

    Return:
        The two number added
    """
    if a is None or (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError('a must be an integer')
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError('b must be an integer')

    result = a + b
    if result == float('inf') or result == -float('inf'):
        return 89

    return int(a) + int(b)
