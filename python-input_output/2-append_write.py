#!/usr/bin/python3

"""

This module defines a append_file function

"""


def write_file(filename="", text=""):
    """
    Appends a string at the end of a text file

    Args:
        filename (:obj:`str`, optional): Filename to append to
        text (:obj:`str`, optional): Text to append to the file

    Returns:
        Number of characters added
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
