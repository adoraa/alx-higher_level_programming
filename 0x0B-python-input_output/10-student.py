#!/usr/bin/python3
"""
Defines a Student class.
"""


class Student:
    """
    Retrieves a dictionary representation.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list, optional): A list of strings representing
            the attributes to include.

        Returns:
            dict: The dictionary representation of the Student instance.
        """
        if attr is not None:
            out = {k: self.__dict__[k] for k in self.__dict__.keys() & attr}
            return out
        else:
            return self.__dict__
