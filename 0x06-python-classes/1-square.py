#!/usr/bin/python3
""" This module contains a class Square."""


class Square:
    """
    This class Square that defines a square
    by private instance attribute: size.
    """
    def __init__(self, size=0):
        """Initialize a new Square.
        Args:
            size (int): The size of the new square.
        """
        self.__size = size
