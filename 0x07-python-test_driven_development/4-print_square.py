#!/usr/bin/python3
def print_square(size):
    """
    Print a square made of # characters.

    Args:
        size (int): The size (length) of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0 or a float (not an integer).

    Returns:
        None
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
