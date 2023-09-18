#!/usr/bin/python3
"""
this just a python code of class base and id
"""
import json


class Base:
    """
        this is a class with base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
            manages id attribute in all the clasess I will create
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
            Returns the JSON string Representation of the list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
    @classmethod
    def save_to_file(cls, list_objs):
        """
            Write the JSON string representation of the list_objs to a file
        """
        if list_objs is None:
            list_objs = []

        class_name = cls.__name__

        filename = f"{class_name}.json"

        list_dicts = [obj.to_dictionary() for obj in list_objs]

        json_string = cls.to_json_string(list_dicts)

        with open(filename, 'w' ) as f:
            f.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """
            Returns the list of dictionaries represented by json_string
        """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
            Returns an instance with all attributes already set.
        """
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)

        dummy_instance.update(**dictionary)

        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """
            Returns a list of instance from a Json file
        """
        class_name = cls.__name__

        filename = f"{class_name}.json"

        try:
            with open(filename, 'r') as f:
                json_string = f.read()
                list_dicts = cls.from_json_string(json_string)
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []
