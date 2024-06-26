#!/usr/bin/python3
"""This module contains a fuction called is_name_class"""


def is_same_class(obj, a_class):
    """Determines if an object type is the same
    as the a_class

    Args:
        obj (instance): is an object
        a_class (class): is a class
    """
    return(type(obj) == a_class)