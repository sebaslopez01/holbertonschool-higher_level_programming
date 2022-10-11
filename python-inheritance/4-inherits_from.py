#!/usr/bin/python3

"""

This module defines a inherits_from function

"""


def inherits_from(obj: object, a_class: object):
    """
    Checks that the object is an instance of a class that inherited
    from the specified class

    Args:
        obj (:obj:`object`): Object to compare
        a_class (:obj:`object`): Class to compare

    Returns:
        True if the object is an instance of a class that inherited
        from the specified class,
        False otherwise
    """
    if type(obj) is a_class:
        return False
    return issubclass(type(obj), a_class)
