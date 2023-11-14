#!/usr/bin/python3
""" Module containing the updated Base class """

import json
import csv
import turtle

class Base:
    """ Updated Base class """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Constructor for Base class """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def validate_non_negative_int(name, value):
        """ Static method to validate if a value is a non-negative integer """
        if not isinstance(value, int) or value < 0:
            raise ValueError("{} must be a non-negative integer".format(name))

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Static method to convert a list of dictionaries to a JSON string """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Class method to save instances to a file in JSON format """
        filename = cls.__name__ + ".json"
        json_list = []
        if list_objs is not None:
            for obj in list_objs:
                json_list.append(obj.to_dictionary())
        with open(filename, mode="w", encoding="utf-8") as file:
            file.write(cls.to_json_string(json_list))

    @staticmethod
    def from_json_string(json_string):
        """ Static method to convert a JSON string to a list of dictionaries """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Class method to create an instance with attributes set from a dictionary """
        dummy_instance = cls(1, 1)  # Create a dummy instance
        dummy_instance.update(**dictionary)  # Update attributes using the dictionary
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """ Class method to load instances from a file in JSON format """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, mode="r", encoding="utf-8") as file:
                json_data = file.read()
                list_dicts = cls.from_json_string(json_data)
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []
            
    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Class method to save instances to a CSV file """
        filename = cls.__name__ + ".csv"
        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            csv_writer = csv.writer(file)
            if cls.__name__ == "Rectangle":
                for obj in list_objs:
                    csv_writer.writerow([obj.id, obj.width, obj.height, obj.x, obj.y])
            elif cls.__name__ == "Square":
                for obj in list_objs:
                    csv_writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """ Class method to load instances from a CSV file """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, mode="r", newline="", encoding="utf-8") as file:
                csv_reader = csv.reader(file)
                if cls.__name__ == "Rectangle":
                    return [cls.create(id=int(row[0]), width=int(row[1]), height=int(row[2]), x=int(row[3]), y=int(row[4])) for row in csv_reader]
                elif cls.__name__ == "Square":
                    return [cls.create(id=int(row[0]), size=int(row[1]), x=int(row[2]), y=int(row[3])) for row in csv_reader]
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        window = turtle.Screen()
        window.bgcolor("white")

        pen = turtle.Turtle()
        pen.shape("turtle")
        pen.color("black")
        pen.speed(2)

        for rectangle in list_rectangles:
            pen.penup()
            pen.goto(rectangle.x, rectangle.y)
            pen.pendown()
            for _ in range(2):
                pen.forward(rectangle.width)
                pen.left(90)
                pen.forward(rectangle.height)
                pen.left(90)

        for square in list_squares:
            pen.penup()
            pen.goto(square.x, square.y)
            pen.pendown()
            for _ in range(4):
                pen.forward(square.size)
                pen.left(90)

        window.exitonclick()
