#!/usr/bin/python3
import json
"""json"""
def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    Args:
        filename (str): The name of the JSON file to be loaded.

    Returns:
        object: The Python object created from the JSON file.

    """
    with open(filename, mode='r', encoding='utf-8') as file:
        return json.load(file)
