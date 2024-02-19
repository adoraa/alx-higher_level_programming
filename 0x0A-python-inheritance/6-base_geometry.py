#!/usr/bin/python3
"""Creates a class"""


class BaseGeometry:
    """Empty class representing base geometry."""

    def area(self):
        """Raises an exception with the message 'area() is not implemented'."""
        raise Exception("area() is not implemented")
