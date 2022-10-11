#!/usr/bin/python3

"""

This module defines a loads_to_json_file function

"""

import json


def load_from_json_file(filename):
    """
    Creates an Object from a JSON file

    Args:
        filename (:obj:`str`): JSON file to read from

    Returns:
        Object readed
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.loads(f.read())
