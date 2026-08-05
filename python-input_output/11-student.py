#!/usr/bin/python3
"""Defines a class Student that can serialize and reload itself."""


class Student:
    """Represent a student with a first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student instance.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary representation of this Student.

        Args:
            attrs (list): Optional list of attribute names to
                include. If not a valid list of strings, every
                attribute is included instead.

        Returns:
            dict: The selected (or all) instance attributes.
        """
        if (type(attrs) is list and
                all(type(a) is str for a in attrs)):
            return {k: v for k, v in self.__dict__.items()
                    if k in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace this Student's attributes from a dictionary.

        Args:
            json (dict): A dictionary of attribute names to values.
        """
        for key, value in json.items():
            setattr(self, key, value)
