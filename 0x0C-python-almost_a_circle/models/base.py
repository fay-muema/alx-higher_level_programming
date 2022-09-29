#!/usr/bin/python3
"""
    class Base
"""
import json
import csv
import os.path


class Base:
    """ Class Base """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        class constructor
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ List to JSON string """
        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Save object in a file """
        filename = "{}.json".format(cls.__name__)
        list_dic = []

        if not list_objs:
            pass
        else:
            for i in range(len(list_objs)):
                list_dic.append(list_objs[i].to_dictionary())

        lists = cls.to_json_string(list_dic)

        with open(filename, 'w') as f:
            f.write(lists)

        @staticmethod
        def from_json_string(json_string):
            """ JSON string to dictionary """
            if not json_string:
                return []
            return json.loads(json_string)

        @classmethod
        def create(cls, **dictionary):
            """ Create an instance """
            if cls.__name__ == "Rectangle":
                new = cls(10, 10)
            else:
                new = cls(10)
            new.update(**dictionary)
            return new
