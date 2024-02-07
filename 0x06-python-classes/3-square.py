#!/usr/bin/python3
"""Class Square that defines a square."""


class Square:
    """
    Private instance attribute:
        - __size (int): Size of the square.

    Instantiation with optional size:
        - def __init__(self, size=0)
            - size: The size of the square (default is 0).

    Public instance method:
        - def area(self): Returns the current square area.
    """
    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int, optional): The size of the square (default is 0).
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
