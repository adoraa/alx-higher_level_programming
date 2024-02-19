#!/usr/bin/python3
"""Creates a BaseGeometry class"""


class BaseGeometry:
    """Empty class representing base geometry."""

    def area(self):
        """
        Raises an exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates an integer value
        """
        if type (value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
