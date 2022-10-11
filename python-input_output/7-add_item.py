#!/usr/bin/python3

import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

"""

This module adds all arguments to a Python list and
then save them

"""


def main():
    """
    Adds all arguments to a Python list and
    then save them
    """
    obj = load_from_json_file('add_item.json')
    obj += sys.argv[1:]
    save_to_json_file(obj, 'add_item.json')


main()
