#!/usr/bin/python3
"""Square module."""
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
