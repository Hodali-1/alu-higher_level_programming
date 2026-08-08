#!/usr/bin/python3
"""Defines the Square class, a subclass of Rectangle."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square: a rectangle whose width equals its height."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a Square by reusing the Rectangle constructor."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """int: the length of a side; sets both width and height."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """Return [Square] (<id>) <x>/<y> - <size>."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """Assign attributes from positional args (id, size, x, y)."""
        if args:
            attrs = ["id", "size", "x", "y"]
            for attr, value in zip(attrs, args):
                setattr(self, attr, value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of the square."""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
