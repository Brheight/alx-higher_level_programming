#!/usr/bin/python3
"""same class"""
def is_same_class(obj, a_class):
    """
    Check if an object is exactly an instance of the specified class.

    Args:
        obj: The object to be checked.
        a_class: The class to compare with.

    Returns:
        True if the object is an instance of the specified class; otherwise, False.
    """
    return type(obj) is a_class
