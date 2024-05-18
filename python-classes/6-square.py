#!/usr/bin/python3
"""Defines a class Square with properties for size and position, and methods to calculate its area and print its graphical representation.

This module enhances the Square class by adding positioning capabilities for visual representation.
"""

class Square:
    """A class that defines a square with properties `size` and `position` and methods to calculate its area and print itself.

    Attributes:
        size (int): The size of a side of the square, private and validated.
        position (tuple): The position offset of the square when printed, validated to be a tuple of 2 positive integers.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new Square with given size and position, defaulting to 0 and (0,0) if not provided.

        Args:
            size (int): The initial size of the square, validated via the size setter.
            position (tuple): The initial position of the square, validated via the position setter.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Retrieves the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the square, with validation.

        Args:
            value (tuple): The new position of the square.

        Raises:
            TypeError: If the position is not a tuple of 2 positive integers.
        """
        if not (isinstance(value, tuple) and len(value) == 2 and all(isinstance(num, int) and num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Prints in stdout the square with the character '#'.

        Prints spaces and newlines based on the `position` attribute before each line of hashes.
        If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print("")
        else:
            print("\n" * self.__position[1], end="")
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
