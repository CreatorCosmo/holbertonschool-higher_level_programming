#!/usr/bin/python3
"""Module to find the max integer in a list."""

def max_integer(lst=[]):
    """Function to find and return the max integer in a list of integers.
       If the list is empty, the function returns None.
       If the input is not a list, it raises a TypeError.
    """
    if not isinstance(lst, list):  # Correct use of the built-in `list` type
        raise TypeError("Input must be a list")
    
    if len(lst) == 0:
        return None
    
    result = lst[0]
    for item in lst[1:]:  # More Pythonic loop
        if item > result:
            result = item
    return result
