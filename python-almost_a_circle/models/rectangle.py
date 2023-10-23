#!/usr/bin/python3
""" Rectangle class """
from models.base import Base as B


class Rectangle(B):
    __width = 0
    __heigth = 0
    __x = 0
    __y = 0

    def __init__(self, width, height, x=0, y=0, id=None):
        """ init method for rectangle class
        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
            x (int): x position of the rectangle
            y (int): y position of the rectangle
            id (int): id of the rectangle
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
    """artgument getters"""
    @property
    def width(self):
        """ width getter """
        return self.__width

    @property
    def height(self):
        """ height getter """
        return self.__height

    @property
    def x(self):
        """ x getter """
        return self.__x

    @property
    def y(self):
        """ y getter """
        return self.__y
    """Argument setters """
    @width.setter
    def width(self, value):
        """ width setter
        Args:
            value (int): value to set
        """
        self.__width = value

    @height.setter
    def height(self, value):
        """ height setter
        Args:
            value (int): value to set
        """
        self.__height = value

    @x.setter
    def x(self, value):
        """ x setter
        Args:
            value (int): value to set
        """
        self.__x = value

    @y.setter
    def y(self, value):
        """ y setter
        Args:
            value (int): value to set
        """
        self.__y = value
