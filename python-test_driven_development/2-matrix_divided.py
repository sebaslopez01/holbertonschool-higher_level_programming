#!/usr/bin/python3

"""
This module defines matrix_divided function
"""


def matrix_divided(matrix, div):
    """ Divides all elementws of a matrix

    Args:
        matrix (:obj:`list` of `list` of `int`): List of lists
        of integers or floats
        div (:obj:`int`): Number to divide all numbers

    Return:
        The new matrix
    """
    if not isinstance(matrix, list):
        raise TypeError(
            'matrix must be a matrix (list of lists) of integers/floats')
    for row in matrix:
        if not isinstance(row, list) or \
            not all([isinstance(col, int) for col in row]) \
                and not all([isinstance(col, float) for col in row]):
            raise TypeError(
                'matrix must be a matrix (list of lists) of integers/floats')

    row_len = len(matrix[0])
    for row in matrix:
        if len(row) != row_len:
            raise TypeError('Each row of the matrix must have the same size')

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')

    return list(map(lambda x: list(map(lambda y:
                                       round(y / div, 2), x)), matrix))
