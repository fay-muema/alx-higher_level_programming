#!/usr/bin/python3
""" Class BaawGeomerty
"""


class BaseGeometry:
    """
    class that defines attributes of Geometric shapes
    """
    def area(self):
        """ Public instance that raises exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        method that validates value
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
