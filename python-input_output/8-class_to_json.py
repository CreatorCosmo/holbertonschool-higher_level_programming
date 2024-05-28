#!/usr/bin/python3
"""This module contains a function called def class_to_json"""


def class_to_json(obj):
    """ function that return dict representation in json format

    Args:
        obj (class): is a class
    """
    return obj.__dict__
