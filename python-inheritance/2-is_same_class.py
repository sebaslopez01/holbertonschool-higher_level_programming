#!/usr/bin/python3

"""

This module defines a is_same_class function

"""


def is_same_class(obj: object, a_class: object):
    """
    Checks that the object is exactly an instance of the specified class

    Args:
        obj (:obj:`object`): Object to compare
        a_class (:obj:`object`): Class to compare

    Returns:
        True if the object is exactly an instance of the class,
        False otherwise
    """
    return type(obj) is a_class
