#!/usr/bin/python3
import json


class Base:
    """class Base to update id number of new instances

    Attributes:
        id (any type, optional): id number to instantiate
        new object with
        __nb_objects: Class attribute to instantiate object
        id number if not given
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Instantiates object with id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def reset_nb_objects():
        """Resets __nb_objects to 0 for testing purposes"""
        Base.__nb_objects = 0

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of
        list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes JSON string representation
        of list_objs to a file"""
        if list_objs is None:
            json_string = "[]"
        else:
            json_string = cls.to_json_string([obj.to_dictionary()
                                              for obj in list_objs])
        with open(cls.__name__ + '.json', mode='w+',
                  encoding='utf-8') as a_file:
            a_file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list represented by json_string"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes set"""
        new = cls(42, 42, 42)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """Loads and creates class instances
        from .json files and returns a list
        of created instances"""
        try:
            with open(cls.__name__ + '.json', mode='r+',
                      encoding='utf-8') as json_file:
                json_string = json_file.read()
            json_list = Base.from_json_string(json_string)
            instance_list = []
            for a_dict in json_list:
                instance_list.append(cls.create(**a_dict))
            return instance_list
        except FileNotFoundError:
            return []
