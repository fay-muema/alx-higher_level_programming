#!/usr/bin/python3
"""
    class myInt
"""


class MyInt(int):
    """
    class that inherits from int
    """
    def __eq__(self, other):
        """
        method that returns
        """
        return int.__ne__(self, other)

    def __ne__(self, other):
        """
        method that returns check
        """
        return int.__eq__(self, other)
