#!/usr/bin/python3

"""

This module defines a read_file function

"""


def read_file(filename=""):
    """
    Reads a text file and prints it out

    Args:
        filename (:obj:`str`, optional): Filename to read
    """
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read())
