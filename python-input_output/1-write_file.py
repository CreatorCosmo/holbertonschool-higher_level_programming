#!/usr/bin/python3
"""This module contains a function called write_file"""


def write_file(filename="", text=""):
    """write_file function that writes a string to a file

    Args:
        filename (str, optional): file name. Defaults to "".
        text (str, optional): string to write inside the file. Defaults to "".
    """
    with open(filename, "w", encoding="utf-8") as a_file:
        nb_characters = a_file.write(text)
        return nb_characters
