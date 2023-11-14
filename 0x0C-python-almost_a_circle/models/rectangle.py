#!/usr/bin/python3
""" Module containing the updated Rectangle class """

from models.base import Base

class Rectangle(Base):
    """ Updated Rectangle class, inherits from Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Constructor for Rectangle class """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Getter for width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter for width """
        self.validate_non_negative_int("width", value)
        self.__width = value

    @property
    def height(self):
        """ Getter for height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter for height """
        self.validate_non_negative_int("height", value)
        self.__height = value

    @property
    def x(self):
        """ Getter for x """
        return self.__x

    @x.setter
    def x(self, value):
        """ Setter for x """
        self.validate_non_negative_int("x", value)
        self.__x = value

    @property
    def y(self):
        """ Getter for y """
        return self.__y

    @y.setter
    def y(self, value):
        """ Setter for y """
        self.validate_non_negative_int("y", value)
        self.__y = value

    def area(self):
        """ Method to calculate the area of the Rectangle """
        return self.__width * self.__height

    def display(self):
        """ Method to display the Rectangle using '#' characters """
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """ Override __str__ method to return a formatted string """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def to_dictionary(self):
        """ Method to return the dictionary representation of a Rectangle """
        return {
            'id': self.id,
            'width': self.__width,
            'height': self.__height,
            'x': self.__x,
            'y': self.__y
        }

    def update(self, *args, **kwargs):
        """ Method to update attributes based on arguments """
        if args:
            attributes = ['id', 'width', 'height', 'x', 'y']
            for attr, value in zip(attributes, args):
                setattr(self, attr, value)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
