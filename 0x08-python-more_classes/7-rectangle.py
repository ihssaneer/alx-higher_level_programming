#!/usr/bin/python3
"""This module contain a Rectangle class"""


class Rectangle:
    """ This class define a class called Rectangle.
    Args:
        number_of_instances: number of created object.
        print_symbol : Symbol used to print rectangle.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """This methode intialize the class Rectangle
        Agrs:
            width (int) : the width of the rectangle.
            height (int) : the height of the rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1
        Rectangle.print_symbol

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

    def area(self):
        """Calculate the rectangle area."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate the rectangle perimeter."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        rec_shape = ""
        for _ in range(self.__height):
            for _ in range(self.__width):
                rec_shape += str(self.print_symbol)
            rec_shape += "\n"
        return (rec_shape.rstrip())

    def __repr__(self):
        """ return a string representation of the rectangle """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """ Print a message when an instance of Rectangle is deleted """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
