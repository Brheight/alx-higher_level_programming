#!/usr/bin/python3
"""file"""
def append_write(filename="", text=""):
    """
    Appends a string to the end of a text file (UTF8) and returns the number of characters added.

    Args:
        filename (str): The name of the text file to which the text will be appended.
        text (str): The text to be appended to the file.

    Returns:
        int: The number of characters added to the file.

    """
    with open(filename, mode='a', encoding='utf-8') as file:
        num_characters_added = file.write(text)
    
    return num_characters_added
