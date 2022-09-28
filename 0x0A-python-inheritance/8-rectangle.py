#!/usr/bin/python3
"""
    Class Retangke
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Classs Rectangle that inherits from BaseGeometry
    """

    def __init__(self, width, height):
        """ Method that instantiates width and height
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
