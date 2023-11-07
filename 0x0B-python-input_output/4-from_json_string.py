#!/usr/bin/python3
import json
"""file"""
def from_json_string(my_str):
    """
    Parses a JSON string and returns the corresponding Python data structure.

    Args:
        my_str (str): The JSON string to be parsed.

    Returns:
        object: The Python data structure represented by the JSON string.

    """
    return json.loads(my_str)
