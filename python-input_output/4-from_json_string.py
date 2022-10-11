#!/usr/bin/python3

"""

This module defines a from_json_string function

"""

import json


def from_json_string(my_str: str):
    """
    Gets an object represented by a JSON string

    Args:
        my_str (:obj:`str`): JSON string

    Returns:
        An object
    """
    return json.loads(my_str)
