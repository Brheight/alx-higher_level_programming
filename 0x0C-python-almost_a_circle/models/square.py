#!/usr/bin/python3
""" Module containing the updated Square class """

from models.rectangle import Rectangle

class Square(Rectangle):
    """ Updated Square class, inherits from Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """ Constructor for Square class """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Getter for size """
        return self.width

    @size.setter
    def size(self, value):
        """ Setter for size """
        self.validate_non_negative_int("width", value)
        self.width = value
        self.height = value

    def __str__(self):
        """ Override __str__ method to return a formatted string """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    def to_dictionary(self):
        """ Method to return the dictionary representation of a Square """
        return {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
        }
