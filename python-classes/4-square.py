#!/usr/bin/python3
"""Defines a class Square with a private attribute size that has getter and setter.

This module provides an example of using property decorators to manage attribute access while enforcing validation.
"""

class Square:
    """A class that defines a square with a property `size` that can be safely accessed and modified.

    Attributes:
        size (int): The size of a side of the square, private and validated.
    """

    def __init__(self, size=0):
        """Initializes a new Square with a given size, defaulting to 0 if no size is given.

        Args:
            size (int): The initial size of the square, validated via the size setter.
        """
        self.size = size

    @property
    def size(self):
        """Retrieves the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square, with validation.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If the new size is not an integer.
            ValueError: If the new size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
