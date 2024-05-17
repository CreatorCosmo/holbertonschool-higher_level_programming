#!/usr/bin/python3
"""Defines a class Square with a private instance attribute.

This module demonstrates the definition of a private instance attribute in a class.
"""

class Square:
    """A class that defines a square with a private instance attribute `size`.

    Attributes:
        size (int): The size of a side of the square.
    """

    def __init__(self, size):
        """Initializes a new Square with a given size.

        Args:
            size (int): The size of the square, no type/value verification is done.
        """
        self.__size = size
