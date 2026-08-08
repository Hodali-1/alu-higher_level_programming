#!/usr/bin/python3
"""Defines the Base model class for all other classes in this project."""
import json


class Base:
    """Manages the ``id`` attribute for all derived classes."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a Base, assigning or auto-generating an id."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of a list of dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON representation of list_objs to <Class>.json."""
        filename = "{}.json".format(cls.__name__)
        with open(filename, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                dicts = [obj.to_dictionary() for obj in list_objs]
                f.write(cls.to_json_string(dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return the list represented by a JSON string ([] if empty)."""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes set from dictionary."""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls()
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of instances loaded from <Class>.json."""
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, "r") as f:
                dicts = cls.from_json_string(f.read())
                return [cls.create(**d) for d in dicts]
        except IOError:
            return []
