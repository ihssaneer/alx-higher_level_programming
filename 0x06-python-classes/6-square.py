#!/usr/bin/python3
"""This module contain the class Square."""


class Square:
    """
    This class Square that defines a square
    by private instance attribute: size, raise
    error if size is not int or < 0 and contain
    a getter, a setter and an area methode.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square.
        Args:
            size (int): The size of the new square.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Return the position.
        """
        return self.__position[]

    @position.setter
    def position(self, value):
        """Sets the position.
        Args:
            value (tuple) : the value to attribute to position.
        """
        if (type(value) is not tuple) or len(value) != 2 or\
            not all(isinstance(a, int) for a in value) or\
                not all(a >= 0 for a in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate the area of a square.
        """
        return self.__size * self.__size

    def my_print(self):
        """prints in stdout the square with the character #.
        """
        if self.__size == 0:
            print()
        else:
            for y in range(self.__position[1]):
                print()
            for x in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
