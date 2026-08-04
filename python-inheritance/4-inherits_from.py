#!/usr/bin/python3
"""Defines a function checking strict subclass inheritance."""


def inherits_from(obj, a_class):
    """Return True if obj's class is a subclass of a_class.

    Returns False if obj's exact type is a_class itself.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
