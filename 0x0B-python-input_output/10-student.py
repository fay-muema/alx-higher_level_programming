#!/usr/bin/python3
"""
    class Student
"""


class Student:
    """
    class Student that defines a student by
    """

    def __init__(self, first_name, last_name, age):
        """
        intiatiates first name and last name
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        method that retrieves a dictionary representation
        """
        obj = self.__dict__.copy()
        if type(attrs) is list:

            for item in attrs:
                if type(item) is not str:
                    return obj
            a_list = {}

            for iatr in range(len(attrs)):
                for satr in obj:
                    if attrs[iatr] == satr:
                        a_list[satr] = obj[satr]
            return a_list

        return obj

