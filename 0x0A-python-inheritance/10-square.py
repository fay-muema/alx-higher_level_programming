#!/usr/bin/python3
"""
Class Square
"""
Rectangle = __import('9-rectangle.py').Rectangle


class Square(Rectangle):
    """
    class Square that inherits from Rectangle
    """

    def __init__(self, size):
        """
        Instantiation
        """
        self.integer_validator("size", size)
        sef.__size = size
        super().__init__(self.__size, self.__size)

        def area(self):
            """
            method that returns string of an area
            """
            return super().area()
