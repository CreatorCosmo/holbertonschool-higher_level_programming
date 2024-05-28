#!/usr/bin/python3

"""This module contain a function called append_write"""


def append_write(filename="", text=""):
    """ function that appends a
    string at the end of a text file
    and returns the number of characters added

    Args:
        filename (str, optional): [description]. Defaults to "".
        text (str, optional): [description]. Defaults to "".
    """
    with open("{}".format(filename), "a", encoding="utf-8") as a_file:
        nb_characters_added = a_file.write(text)
        return nb_characters_added
