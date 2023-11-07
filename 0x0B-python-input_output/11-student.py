#!/usr/bin/python3
"""file json"""
class Student:
    """
    Class that defines a student.

    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.

    Methods:
        to_json(self, attrs=None): Retrieves a dictionary representation of the Student instance.
        reload_from_json(self, json): Replaces all attributes of the Student instance from a given dictionary.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of the Student instance.

        Args:
            attrs (list of str): A list of attribute names to be included in the dictionary.
                If None, all attributes will be included.

        Returns:
            dict: A dictionary representation of the Student instance.
        """
        if attrs is None:
            return self.__dict__
        else:
            result = {}
            for attr in attrs:
                if hasattr(self, attr):
                    result[attr] = getattr(self, attr)
            return result

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance from a given dictionary.

        Args:
            json (dict): A dictionary containing attribute names and their corresponding values.
        """
        for key, value in json.items():
            setattr(self, key, value)
