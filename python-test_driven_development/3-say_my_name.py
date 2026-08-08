#!/usr/bin/python3
"""Provides a function that prints a person's full name.

This module demonstrates validating string arguments and using
a default value for an optional parameter.
"""


def say_my_name(first_name, last_name=""):
    """Print 'My name is <first_name> <last_name>'.

    Args:
        first_name (str): The person's first name.
        last_name (str): The person's last name. Defaults to "".
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
