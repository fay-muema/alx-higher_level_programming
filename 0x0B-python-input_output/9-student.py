#!/usr/bin/python3
"""
    defines a student
"""


class Student:
    """
    class that defines a student
    """

    def __init__(self, first_name, last_name, age):
        """
        initializing
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

        def to_json(self):
            """
            method that returns directory
            """
            return self.__dict__.copy()
