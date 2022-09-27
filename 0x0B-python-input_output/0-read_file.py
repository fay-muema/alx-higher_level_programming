#!/usr/bin/python3
"""
    read_file used to read file
"""


def read_file(filename=""):
    """
    function that reads from a fie
    """
    with open(filename, 'r', encoding="UTF8") as f:
        read_data = f.read()
            print(read_data, end="")
