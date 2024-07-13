#!/usr/bin/python3
"""Module containing BaseGeometry and Rectangle classes"""


class BaseGeometry:
    """BaseGeometry class with area and integer validation methods"""

    def area(self):
        """Raises an exception indicating area is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that the value is an integer and greater than 0

        Args:
            name (str): The name of the value
            value (int): The value to validate

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is not greater than 0
        """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
