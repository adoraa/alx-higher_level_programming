#!/usr/bin/python3
"""Class Square that defines a square."""


class Square:
    """
    Private instance attributes:
        - __size (float or int): The size of the square.

    Public instance methods:
        - def area(self): Returns the current square area.

    Properties:
        - size: Getter and setter for the size attribute.
    """
    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Args:
            size: The size of the square (default is 0).
        """
        self.size = size

    @property
    def size(self):
        """
        Getter method to retrieve the size of the square.

        Returns:
            float or int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method to set the size.

        Args:
            value: The value to set as the size.

        Raises:
            TypeError: If value ! a number.
            ValueError: If value < than 0.
        """
        if not isinstance(value, (float, int)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        prints the current square area.

        Returns:
            float or int: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """Equality operator"""
        return self.area() == other.area()

    def __ne__(self, other):
        """Inequality operator"""
        return self.area() != other.area()

    def __lt__(self, other):
        """Less than operator"""
        return self.area() < other.area()

    def __le__(self, other):
        """Less than or equal to operator"""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Greater than operator"""
        return self.area() > other.area()

    def __ge__(self, other):
        """Greater than or equal to operator"""
        return self.area() >= other.area()


if __name__ == "__main__":
    pass
