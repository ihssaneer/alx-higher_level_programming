#!/usr/bin/python3
""" This module contains a class Square."""


class Square:
    """
    This class Square that defines a square
    by private instance attribute: size and raise
    error if size is not int or < 0.
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
