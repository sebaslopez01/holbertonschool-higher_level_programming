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

    for i in range(1, n + 1):
        temp_lst = [1]
        c = 1
        for j in range(1, i + 1):
            c = c * (i - j) // j
            if c != 0:
                temp_lst.append(c)
        lst.append(temp_lst)

    return lst
