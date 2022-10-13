#!/usr/bin/python3

"""

This module defines a add_attribute function

"""


def add_attribute(obj: object, attr_name: str, attr_value):
    """
    Adds a new attribute to an object if it's possible

    Args:
        obj (:obj:`object`): Object to add the attribute
        attr_name (:obj:`str`): Attribute name
        attr_value (:obj:`any`): Attribute value
    """
    if not isinstance(obj, object):
        raise TypeError("can't add new attribute")

    obj.__dict__[attr_name] = attr_value
