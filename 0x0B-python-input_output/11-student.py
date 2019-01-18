#!/usr/bin/python3
import json
class Student:
    """
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        student_dict_str = json.dumps(self.__dict__)
        return json.loads(student_dict_str)
