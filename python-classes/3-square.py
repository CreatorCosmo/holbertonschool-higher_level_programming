#!/usr/bin/python3
"""Defines a class Square with a method to calculate its area.

This module provides a simple example of adding functionality to a class with attribute validation.
"""

class Square:
    """A class that defines a square with private instance attribute `size` and a method to compute its area.

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

    def area(self):
        """Returns the area of the square.

        Returns:
            int: The area calculated as size squared.
        """
        return self.__size ** 2
