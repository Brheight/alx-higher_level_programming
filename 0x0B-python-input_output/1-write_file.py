#!/usr/bin/python3
"""files"""
def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and returns the number of characters written.

    Args:
        filename (str): The name of the text file to be written.
        text (str): The text to be written to the file.

    Returns:
        int: The number of characters written to the file.

    """
    with open(filename, mode='w', encoding='utf-8') as file:
        num_characters = file.write(text)
    
    return num_characters
