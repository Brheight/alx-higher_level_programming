#!/usr/bin/python3
"""square"""
Rectangle = __import__('9-rectangle').Rectangle
class Square(Rectangle):
    """
    A class representing a square that inherits from Rectangle.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size):
        """
        Initializes a Square instance with a given size.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than or equal to 0.
        """
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """
        Return a string representation of the square.

        Returns:
            str: A string in the format "[Square] <size>/<size>"
        """
        return f"[Square] {self.__size}/{self.__size}"
