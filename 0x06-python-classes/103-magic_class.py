#!/usr/bin/python3
"""Python ByteCode replica"""

import math


class Magic:
    """Represents a circle."""

    def __init__(self, radius=0):
        """
        Initializes a new instance of the MagicClass class.

        Args:
            radius: The radius of the circle (default is 0).
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """
        Calculates the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculates the circumference of the circle.

        Returns:
            float: The circumference of the circle.
        """
        return 2 * math.pi * self.__radius


if __name__ == "__main__":
    m_circle = Magic(radius=5)

    print("Radius:", m_circle._Magic__radius)
    print("Area:", m_circle.area())
    print("Circumference:", m_circle.circumference())
