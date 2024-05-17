#!/usr/bin/python3
"""Defines a class Square that validates an attribute.

This module demonstrates how to handle exceptions for attribute validation in a class definition.
"""

class Square:
    """A class that defines a square with private instance attribute `size`.

    Attributes:
        size (int): The size of a side of the square, validated to be an integer and non-negative.
    """

    def __init__(self, size=0):
        """Initializes a new Square with a given size, defaulting to 0 if no size is given.

        Args:
            size (int): The size of the square, validated to be an integer and non-negative.

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
