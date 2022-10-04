#!/usr/bin/python3

"""
This module defines text_indentation function
"""


def text_indentation(text: str):
    """ Prints a text with 2 new line after each . ? and :

    Args:
        text (:obj:`str`): Text to modify
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')

    new_str = ''

    for char in text:
        new_str += char

        if char == '.' or char == '?' or char == ':':
            print(new_str.strip())
            print()
            new_str = ''

    print(new_str.strip())
