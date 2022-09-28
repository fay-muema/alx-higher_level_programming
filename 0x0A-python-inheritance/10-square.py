#!/usr/bin/python3
"""
    Class Square
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    class Square that inherits from Rectangle
    """

    def __init__(self, size):
        """
        method for Instantiation 
        """
        self.integer_validator("size", size)
        sef.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """
        method that returns string of an area
        """
        return super().area()
