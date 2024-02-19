#!/usr/bin/python3
"""Defines a class Square"""


class BaseGeometry:
    """Base class representing base geometry"""

    def area(self):
        """Raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates an integer value
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Class representing a rectangle"""

    def __init__(self, width, height):
        """Instantiates a rectangle"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculates the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Returns the formatted rectangle description"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
