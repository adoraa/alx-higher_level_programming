#!/usr/bin/python3
"""Class Square that defines a square."""


class Square:
    """
    Private instance attribute:
        - __size (int): Size of the square.

    Instantiation with optional size:
        - def __init__(self, size=0)
            - size: The size of the square (default is 0).

    Public instance methods:
        - def area(self): Returns the current square area.
        - def my_print(self): Prints the square with the # character.

    Properties:
        - size (int): Getter to retrieve the size.
                      Setter to set the size with type and value validation.
    """
    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int, optional): The size of the square (default is 0).
        """
        self.size = size

    @property
    def size(self):
        """
        Getter method to retrieve the size.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method to set the size with type and value validation.

        Args:
            value: The value to set as the size.

        Raises:
            TypeError: If value != an integer.
            ValueError: If value is < 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with the # character.

        If size is equal to 0, prints an empty line.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
