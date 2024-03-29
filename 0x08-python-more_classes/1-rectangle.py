#!/usr/bin/python3
"""This module contain a Rectangle class"""


class Rectangle:
    """ This class define a class called Rectangle. """

    def __init__(self, width=0, height=0):
        """This methode intialize the class Rectangle
        Agrs:
            width (int) : the width of the rectangle.
            height (int) : the height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """This methode returns the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """This methode attribute a value to the width.
        Args:
            value (int) : the value to attribute to width.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """This methode returns the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """This methode attribute a value to the height.
        Args:
            value (int) : the value to attribute to height.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
