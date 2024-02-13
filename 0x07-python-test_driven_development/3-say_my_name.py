#!/usr/bin/python3
"""Prints a formatted string with the first and last name."""


def say_my_name(first_name, last_name=""):
    """
    Args:
    first_name (str): The first name.
    last_name (str): The last name. Defaults to an empty string.

    Raises:
    TypeError: If first_name or last_name is not a string.
    """
    err = "first_name must be a string or last_name must be a string"
    if not isinstance(first_name, str) or not isinstance(last_name, str):
        raise TypeError(f"{err}")

    full_name = first_name + " " + last_name
    print("My name is {}".format(full_name))
