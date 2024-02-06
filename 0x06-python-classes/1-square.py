#!/usr/bin/python3
class Square:
    """
    Class Square that defines a square.

    Private instance attribute:
        - size: Size of the square.

    Instantiation with size (no type/value verification).
    """
    def __init__(self, size):
        self.__size = size
