#!/usr/bin/python3
"""file"""
def class_to_json(obj):
    """
    Returns a dictionary representation of an object for JSON serialization.

    Args:
        obj: An instance of a class with serializable attributes.

    Returns:
        dict: A dictionary representation of the object.
    """
    if hasattr(obj, "__dict__"):
        return obj.__dict__
    return obj
