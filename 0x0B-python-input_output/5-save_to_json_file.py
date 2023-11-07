#!/usr/bin/python3
import json
"""file"""
def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using a JSON representation.

    Args:
        my_obj: The Python object to be saved to the file.
        filename (str): The name of the text file to which the object will be saved.

    Returns:
        None

    """
    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(my_obj, file)
