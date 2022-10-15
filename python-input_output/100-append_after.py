#!/usr/bin/python3

"""

This module defines a append_after function

"""


def append_after(filename='', search_string='', new_string=''):
    """
    Inserts a line of text to a file, after each line
    containing a specific string

    Args:
        filename (:obj:`str`, optional): Filename to insert string
        search_string (:obj:`str`, optional): String to search for
        new_string (:obj:`str`, optional): String to insert to the file
    """

    with open(filename, 'r', encoding='utf-8') as f:
        data_lines = f.readlines()

        for count, line in enumerate(data_lines):
            if search_string in line:
                if len(data_lines) == count + 1:
                    data_lines.append(new_string)
                    break
                else:
                    data_lines.insert(count + 1, new_string)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(''.join(data_lines))
