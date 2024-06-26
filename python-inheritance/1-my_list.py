#!/usr/bin/python3
"""This module contain a class named mMyList"""


class MyList(list):
    """Mylist class that inherits list class
    that inherits list class

    Args:
        list (class): list class
    """
    def print_sorted(self):
        """print_sorted function that prints a list in sorted way"""
        print(sorted(self))
