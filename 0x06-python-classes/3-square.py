#!/usr/bin/python3
"""This module contain the class Square."""


class Square:
    """
    This class Square that defines a square
    by private instance attribute: size, raise
    error if size is not int or < 0 and contain
    area methode.
    """
    def __init__(self, size=0):
        """Initialize a new Square.
        Args:
            size (int): The size of the new square.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Calculate the area of a square.
        """
        return self.__size * self.__size
