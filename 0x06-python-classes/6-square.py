#!/usr/bin/python3
"""Class Square that defines a square."""


class Square:
    """
    Private instance attributes:
        - __size (int): Size of the square.
        - __position (tuple): Position of the square.

    Instantiation with optional size and optional position:
        - def __init__(self, size=0, position=(0, 0))

    Public instance methods:
        - def area(self): Returns the current square area.
        - def my_print(self): Prints the square with the # character.

    Properties:
        - size (int): Getter to retrieve the size.
                      Setter to set the size with type and value validation.
        - position (tuple): Getter to retrieve the position.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int, optional): The size of the square (default is 0).
            position (tuple, optional): The position of the square.
        """
        self.size = size
        self.position = position

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
            TypeError: If value ! an integer.
            ValueError: If value < than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """
        Getter method to retrieve the position.

        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method to set the position with type and value validation.

        Args:
            value: The value to set as the position.

        Raises:
            TypeError: If value ! a tuple of 2 positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        Returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with the character #.

        If size === 0, prints an empty line.
        Position is used by using space, ignore when position[1] > 0.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
