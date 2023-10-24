#!/usr/bin/python3

class Square:
    """
    This is the Square class.

    The Square class represents a square shape.

    Attributes:
        __size (int): The private size of the square.

    Args:
        size (int): The size of the square.

    """
    def __init__(self, size):
        """
        Initializes a new Square instance with the given size.

        Args:
            size (int): The size of the square.

        """
        self.__size = size
