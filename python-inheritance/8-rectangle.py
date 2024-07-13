#!/usr/bin/python3

'''creating a class '''


class BaseGeometry:
    # instance method
    ''' instance method'''
    def __init__(self):
        '''initialize class '''
        pass

    def area(self):
        '''raises an exception'''
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        '''validates value '''
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

"""class rectangle"""


class Rectangle(BaseGeometry):
    """creates rectangle class"""
    def __init__(self, width, height):
        """initializes rectangle"""
        super().__init__()  # Initialize base class (BaseGeometry)
        self.__width = 0  # Initialize private attribute __width
        self.__height = 0  # Initialize private attribute __height
        self.integer_validator("width", width)  # Validate width
        self.integer_validator("height", height)  # Validate height
        self.__width = width  # Assign validated width to private attribute __width
        self.__height = height  # Assign validated height to private attribute __height
