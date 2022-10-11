#!/usr/bin/python3

"""

This module defines a save_to_json_file function

"""

import json


def save_to_json_file(my_obj, filename: str):
    """
    Writes an Object to a text file

    Args:
        my_obj (:obj:`any`): Object to write
        filename (:obj:`str`): Filename to write to
    """
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(json.dumps(my_obj))
