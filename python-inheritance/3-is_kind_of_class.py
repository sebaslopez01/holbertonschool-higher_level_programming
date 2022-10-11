#!/usr/bin/python3

"""

This module defines a is_kind_of_class function

"""


def is_kind_class(obj: object, a_class: object):
    """
    Checks that the object is an instance of the specified class

    Args:
        obj (:obj:`object`): Object to compare
        a_class (:obj:`object`): Class to compare

    Returns:
        True if the object is an instance of the class,
        False otherwise
    """
    return isinstance(obj, a_class)
