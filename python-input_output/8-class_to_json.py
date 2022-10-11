#!/usr/bin/python3

"""

This module defines a class_to_json function

"""


def class_to_json(obj: object):
    """
    Gets the dictionary description for JSON serialization of an object

    Args:
        obj (:obj:`object`): An instance of a Class

    Returns:
        The dictionary description
    """
    return obj.__dict__
