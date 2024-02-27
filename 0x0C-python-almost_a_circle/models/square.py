#!/usr/bin/python3
"""Square module."""
import csv
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class inherits from Rectangle class."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize the Square instance with size, x, y, and id."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return a string representation of the Square."""
        origin = "{{{}/{}}}".format(self.x, self.y)
        return "[Square] ({}) {} - {}".format(self.id, origin, self.width)

    @property
    def size(self):
        """Getter for size."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the Square attributes."""
        attributes = ['id', 'size', 'x', 'y']
        if args:
            for attr, value in zip(attributes, args):
                setattr(self, attr, value)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of the Square."""
        return {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
        }

    def to_csv_row(self):
        """Convert object to CSV row."""
        return [self.id, self.width, self.x, self.y]

    @classmethod
    def from_csv_row(cls, row):
        """Create object from CSV row."""
        id, size, x, y = map(int, row)
        return cls(size, x, y, id)

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
