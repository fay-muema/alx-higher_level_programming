#!/usr/bin/python3
"""
    class Square
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    class Square that inherits from Rectangle
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
        return "[Square] {}/{}".format(self.__size, self.__size)
