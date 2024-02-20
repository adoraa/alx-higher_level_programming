#!/usr/bin/python3
"""
Defines a function to write a string to a text file (UTF8)
and returns the number of characters written.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and
    returns the number of characters written.

    Args:
        filename (str): The name of the file.
        text (str): The text to write to the file

    Returns:
        int: The number of characters written
    """
    with open(filename, 'w', encoding='utf-8') as file:
        chars_written = file.write(text)
    return chars_written
