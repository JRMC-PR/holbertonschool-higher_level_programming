#!/usr/bin/python3
class Rectangle:
    """Rectangle class"""

    def __init__(self, width=0, height=0):
        """__init__ method.
        Args:
            width (int): integer width
            height (int): integer height
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """width: returns width
        Args:
            width (int): integer width
        Returns:
            rectangle width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """width setter
        Args:
            width (int): integer width
        Returns:
            rectangle width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height: returns height
        Args:
            height (int): integer height
        Returns:
            rectangle height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """height setter
        Args:
            height (int): integer height
        Returns:
            rectangle height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise TypeError("height must be >= 0")
        self.__height = value