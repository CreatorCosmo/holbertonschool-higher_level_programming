#!/usr/bin/python3

def say_my_name(first_name, last_name=""):
    """
    Prints the full name in the format "My name is <first name> <last name>".

    Args:
        first_name (str): The first name of the person.
        last_name (str): The last name of the person; defaults to an empty string.

    Raises:
        TypeError: If either first_name or last_name are not strings.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
