#!/usr/bin/python3
"""
This module provides a function add_integer that adds two integers.

The function takes two parameters, 'a' and 'b'. Both parameters must be
either integers or floats. If they are floats, they will be converted
to integers before addition. The function is designed to handle type
errors and ensures that the inputs provided are of valid types.
"""
def add_integer(a, b=98):
    """
Args:
    a (int or float): The first number to add. Must be an integer or a float. If its a float, it will be converted to an integer.
    b (int or float, optional): The second number to add, defaulting to 98. Must be an integer or float. If its a float, it will be converted to an integer.

Returns:
    int: The sum of a and b after converting them to integers.

Raises:
    TypeError: If either a or b is not an integer or float convertible to an integer.

    """
      
      
    if isinstance(a, float):
        a = int(a)
    elif not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')

    if isinstance(b, float):
        b = int(b)
    elif not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')
    return a + b
