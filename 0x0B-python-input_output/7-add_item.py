#!/usr/bin/python3
import sys
import os
"""json"""
# Import the functions using __import__
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

def add_args_to_list_and_save(args):
    # Initialize an empty list
    my_list = []

    # Check if the file exists and load the existing list if it does
    if os.path.exists("add_item.json"):
        my_list = load_from_json_file("add_item.json")

    # Extend the list with the command-line arguments
    my_list.extend(args)

    # Save the updated list to "add_item.json"
    save_to_json_file(my_list, "add_item.json")

if __name__ == "__main__":
    # Remove the script name (argv[0]) from the list of arguments
    args = sys.argv[1:]
    add_args_to_list_and_save(args)
