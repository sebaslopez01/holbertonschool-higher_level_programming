#!/usr/bin/python3

"""

This module defines a write_file function

"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file

    Args:
        filename (:obj:`str`, optional): Filename to write to
        text (:obj:`str`, optional): Text to write to the file

    Returns:
        Number of characters written
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
