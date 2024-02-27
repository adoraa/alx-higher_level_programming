#!/usr/bin/python3
"""Rectangle module."""
import csv
from models.base import Base


class Rectangle(Base):
    """Rectangle class inherits from Base class."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize the Rectangle instance"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for x."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter for y."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area of the Rectangle."""
        return self.__width * self.__height

    def display(self):
        """Print the Rectangle instance with the character #."""
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """Return a string representation of the Rectangle."""
        origin = "{{{}/{}}}".format(self.__x, self.__y)
        wScale = "{{{}/{}}}".format(self.__width, self.__height)
        return ("[Rectangle] ({}) {} - {}".format(self.id, origin, wScale))

    def update(self, *args, **kwargs):
        """Update the Rectangle attributes."""
        if args:
            attributes = ['id', 'width', 'height', 'x', 'y']
            for attr, value in zip(attributes, args):
                setattr(self, attr, value)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of the Rectangle."""
        return {
            'id': self.id,
            'width': self.__width,
            'height': self.__height,
            'x': self.__x,
            'y': self.__y
        }

    def to_csv_row(self):
        """Convert object to CSV row."""
        return [self.id, self.width, self.height, self.x, self.y]

    @classmethod
    def from_csv_row(cls, row):
        """Create object from CSV row."""
        id, width, height, x, y = map(int, row)
        return cls(width, height, x, y, id)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        filename = "{}.csv".format(cls.__name__)
        with open(filename, "w") as file:
            csv_writer = csv.writer(file)
            for obj in list_objs:
                csv_writer.writerow(obj.to_csv_row())

    @classmethod
    def load_from_file_csv(cls):
        filename = "{}.csv".format(cls.__name__)
        try:
            with open(filename, "r") as file:
                csv_reader = csv.reader(file)
                list_objs = [cls.from_csv_row(row) for row in csv_reader]
                return list_objs
        except FileNotFoundError:
            return []
