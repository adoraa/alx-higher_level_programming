#!/usr/bin/python3
"""Lists available attributes and methods of an object.
"""


def lookup(obj):
    """Returns the list of available attributes
    and methods of an object.

    Args:
        - obj: object
    """
    return [attr for attr in dir(obj)]
