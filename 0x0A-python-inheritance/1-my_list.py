#!/usr/bin/python3
"""list"""

class MyList(list):
    """
    A custom list class that inherits from the built-in list class.
    """

    def print_sorted(self):
        """
        Print the list, sorted in ascending order.
        """
        print(sorted(self))
