#!/usr/bin/python3
"""
    read_file used to read file
"""


def read_file(filename=""):
    """
    function that reads from a fie
    """
    with open("UTF8") as f:
        for line in f:
            print(line, end="")
