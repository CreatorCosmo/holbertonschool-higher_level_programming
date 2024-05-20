#!/usr/bin/python3

def add_integer(a, b=98):
    """
Adds two integers or floats after converting them to integers.

Args:
    a (int or float): The first number to add. Must be an integer or a float. If its a float, it will be converted to an integer.
    b (int or float, optional): The second number to add, defaulting to 98. Must be an integer or float. If its a float, it will be converted to an integer.

Returns:
    int: The sum of a and b after converting them to integers.

Raises:
    TypeError: If either a or b is not an integer or float convertible to an integer.
    
    Examples:
        >>> add_integer(10, 20)
        30
        >>> add_integer(11.5, 21.5)
        32
        >>> add_integer(-12, 22.8)
        10
        >>> add_integer('a', 20)
        Traceback (most recent call last):
        ...
        TypeError: a must be an integer
        >>> add_integer(10, 'b')
        Traceback (most recent call last):
        ...
        TypeError: b must be an integer
    """
      
    if isinstance(a, float):
        a = int(a)
    elif not isinstance(a, int):
        raise TypeError('a must be an integer')

    if isinstance(b, float):
        b = int(b)
    elif not isinstance(b, int):
        raise TypeError('b must be an integer')
    return a + b