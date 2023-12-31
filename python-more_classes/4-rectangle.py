#!/usr/bin/python3
"""Class to define a rectangle"""


class Rectangle:
    """Rectangle: defines a rectangle"""

    def __init__(self, width=0, height=0):
        """__init__: initializes a rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """width: gets the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """width: sets the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height: gets the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """height: sets the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """area: returns the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """perimeter: returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """__str__: prints the rectangle with the character #"""
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.__width] * self.__height)

    def __repr__(self):
        """__repr__: returns the representation of the rectangle"""
        return f"Rectangle({self.__width}, {self.__height})"
