#!/usr/bin/python3
"""This is a class BaseGeometry"""


def integer_validator(value):
    """Defines the integer validator"""
    if not isinstance(value, int):
        raise TypeError("{name} must be an integer")
    if value <= 0:
        raise ValueError("{name} must be greater than 0")


class BaseGeometry:
    """Define the Geometry"""
    def area(self):
        """Defines the area of the Geometry"""
        raise Exception("area() is not implemented")

