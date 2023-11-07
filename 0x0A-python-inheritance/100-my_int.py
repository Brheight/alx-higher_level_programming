#!/usr/bin/python3
"""int"""
class MyInt(int):
    """
    A class representing a rebel integer that inverts the behavior of the == and != operators.

    This class inherits from the built-in int type.

    Methods:
        __eq__(self, other): Overrides the equality operator (==) to return the inverse of the parent class's inequality.
        __ne__(self, other): Overrides the inequality operator (!=) to return the inverse of the parent class's equality.

    Example:
        my_i = MyInt(3)
        print(my_i == 3)  # Output: False
        print(my_i != 3)  # Output: True
    """

    def __eq__(self, other):
        """
        Overrides the equality operator (==) to return the inverse of the parent class's inequality.

        Args:
            other (Any): The value to compare with.

        Returns:
            bool: True if not equal, False if equal.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Overrides the inequality operator (!=) to return the inverse of the parent class's equality.

        Args:
            other (Any): The value to compare with.

        Returns:
            bool: True if equal, False if not equal.
        """
        return super().__eq__(other)
