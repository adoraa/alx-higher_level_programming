#!/usr/bin/python3
"""Checks if an attribute can be added to an object"""


def add_attribute(obj, attribute, value):
    """Adds a new attribute to an object if possible."""
    if hasattr(obj, "__dict__") or hasattr(obj, "__slots__"):
        setattr(obj, attribute, value)
    else:
        raise TypeError("can't add new attribute")
