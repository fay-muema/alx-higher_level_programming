#!/usr/bin/python3
"""
    class myint
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    class MyInt that inherits from int
    """
    def __init__(self, size):
        """
        method that intiatiate
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """
        method that returns a string
        """
        return super().area()

    def __str__(self):
        """
        method that returns printable string
        """
