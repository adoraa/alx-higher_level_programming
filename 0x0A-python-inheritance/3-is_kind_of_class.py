#!/usr/bin/python3
"""Checks if an object is an instance of, or if the object is
   an instance of a class that inherited from
   """


def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of, or if the object is an
    instance of a class that inherited from, the class; otherwise False.
    """
    return isinstance(obj, a_class)
