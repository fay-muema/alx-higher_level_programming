#!/usr/bin/python3
""" write_file - writes line to a file
"""


def write_file(filename="", text=""):
    """
    function that writes string to the file
    """
    with open(filename, 'w', encoding="UTF8") as f:
        return f.write(text)
