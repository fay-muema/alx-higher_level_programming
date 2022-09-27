#!/usr/bin/python3
"""
    save_to_json_file - used  writes an Object to a text file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    function that writes an Object to a text file,
    using a JSON representation
    """
    with open(filename, 'w', encoding="UTF8") as f:
        json.dump(my_obj, f)
