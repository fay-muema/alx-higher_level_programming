#!/usr/bin/python3
"""
     returns the dictionary description
"""


def class_to_json(obj):
    """
    function that returns the dictionary description
    with simple data structure
    """

    res = {}
    if hasattr(obj, "__dict__"):
        res = obj.__dict__.copy()
    return res
