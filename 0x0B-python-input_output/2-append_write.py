#!/usr/bin/python3
"""
    append_write - appends a string at the end of the line
"""


def append_write(filename="", text=""):
    """
    Function that appends strings to te file
    """
    with open(filename, 'a', encoding="UTF8") as f:
        return f.write(text)
