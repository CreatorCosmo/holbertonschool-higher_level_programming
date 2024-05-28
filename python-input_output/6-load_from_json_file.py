#!/usr/bin/python3
"""This module contain a function called load_from_json:file"""

import json


def load_from_json_file(filename):
    """ function that load a json file

    Args:
        filename (json): json file
    """
    with open(filename, encoding="utf-8") as a_file:
        return json.loads(a_file.read())
