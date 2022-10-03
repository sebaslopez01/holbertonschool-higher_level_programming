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

    for char in text:
        print(char, end='')

        if char == '.' or char == '?' or char == ':':
            print()
            print()
