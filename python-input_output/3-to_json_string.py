#!/usr/bin/python3

"""

This module defines a to_json_string function

"""

import json


def to_json_string(my_obj):
    """
    Gets the JSON representation of an object

    Args:
        my_obj (:obj:`any`): Any type to object to convert to JSON format

    Returns:
        The JSON representation in string
    """
    return json.dumps(my_obj)
