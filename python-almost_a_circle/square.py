#!/usr/bin/python3

# File: python-almost_a_circle/square.py

from rectangle import Rectangle

class Square(Rectangle):
    """
    A class used to represent a Square, inheriting from Rectangle.

    Attributes
    ----------
    side_length : int
        The length of each side of the square.
    """

    def __init__(self, side_length):
        """
        Parameters
        ----------
        side_length : int
            The length of each side of the square.
        """
        super().__init__(side_length, side_length)
