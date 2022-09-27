#!/usr/bin/python3
"""
    load_from_json_file - creates an Object from a “JSON file”
"""
import json


def load_from_json_file(filename):
    """
    function that creates an Object from a “JSON file”
    """
    with open(filename, "r", encoding="UTF8") as f:
        return json.load(f)
