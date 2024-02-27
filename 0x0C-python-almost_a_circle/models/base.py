#!/usr/bin/python3
"""Base module."""
import json


class Base:
    """Base class for managing id attribute."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the Base instance with an optional id."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries."""
        if not list_dictionaries or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file."""
        if list_objs is None:
            list_objs = []
        filename = "{}.json".format(cls.__name__)
        j_str = cls.to_json_string([obj.to_dictionary() for obj in list_objs])
        with open(filename, "w") as file:
            file.write(j_str)

    @staticmethod
    def from_json_string(json_string):
        """Return the list of the JSON string representation json_string."""
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set."""
        dummy_instance = cls(1, 1)
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Return a list of instances from a file."""
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, "r") as file:
                json_string = file.read()
                list_dicts = cls.from_json_string(json_string)
                list_instances = [cls.create(**d) for d in list_dicts]
                return list_instances
        except FileNotFoundError:
            return []
