#!/usr/bin/python3

def text_indentation(text):
    """
    Prints the given text, adding two new lines after each '.', '?', or ':'.
    Removes spaces at the beginning or end of each resulting segment.

    Args:
        text (str): The text to be processed.

    Raises:
        TypeError: If the input is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        char = text[i]
        print(char, end='')
        if char in '.?:':
            print("\n\n", end='')
            # Move index forward to skip any space after the punctuation if it exists
            while i + 1 < len(text) and text[i + 1] == ' ':
                i += 1
        i += 1
