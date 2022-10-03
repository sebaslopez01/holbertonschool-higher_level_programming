#!/usr/bin/python3

"""
This module defines say_my_name function
"""


def say_my_name(first_name, last_name=''):
    """ Prints My name is <first_name> <last_name>

    Args:
        first_name (:obj:`str`): First name to print
        last_name (:obj:`str`, optional): Last anme to print
    """
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')

    print(f'My name is {first_name} {last_name}')
