#!/usr/bin/python3
"""This module contain the class Square."""


class Square:
    """
    This class Square that defines a square
    by private instance attribute: size, raise
    error if size is not int or < 0 and contain
    a getter, a setter and an area methode.
    """

    def __init__(self, size=0):
        """Initialize a new Square.
        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Return the size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size.
        Args:
            value (int) : the value to attribute to size.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculate the area of a square.
        """
        return self.__size * self.__size
