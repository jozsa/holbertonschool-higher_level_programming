#!/usr/bin/python3


class Student:
    """Student instantiated with first_name, last_name, and age

    Attributes:
        first_name (str, required): first name of student
        last_name (str, required): last name of student
        age (int, required): age of student
    """
    def __init__(self, first_name, last_name, age):
        """Instantation of Student class with
        required first_name, last_name, and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns the dictionary version of self
        Optional argument attrs set to None by default
        """
        if type(attrs) is list:
            if all(type(i) is str for i in attrs):
                return {key: value for key, value in
                        self.__dict__.items() if key in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        self.__dict__ = json
