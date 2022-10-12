#!/usr/bin/python3

"""
This module defines a pascal_triangle function
"""


def pascal_triangle(n: int):
    """
    Creates a list of lists of integers representing
    the Pascal's triangle of n

    Args:
        n (:obj:`int`): The size of the Pascal's triangle

    Returns:
        A list of list of integers
    """
    lst = []

    if n <= 0:
        return lst

    for i in range(n):
        lst.append(list(map(int, ' '.join(str(11 ** i)).split())))

    return lst
