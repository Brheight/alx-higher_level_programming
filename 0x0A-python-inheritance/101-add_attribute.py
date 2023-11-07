#!/usr/bin/python3
"""add attribute"""
def add_attribute(obj, attribute, value):
    """
    Adds a new attribute to an object if it's possible.

    Args:
        obj (object): The object to which the attribute should be added.
        attribute (str): The name of the new attribute.
        value (Any): The value to assign to the new attribute.

    Raises:
        TypeError: If the object can't have new attributes.

    Example:
        class MyClass():
            pass

        mc = MyClass()
        add_attribute(mc, "name", "John")
        print(mc.name)  # Output: John

        a = "My String"
        add_attribute(a, "name", "Bob")  # Raises TypeError
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)
