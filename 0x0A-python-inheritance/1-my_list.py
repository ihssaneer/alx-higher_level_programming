#!/usr/bin/python3
""" This module containt Mylist class. """


class MyList(list):
    """ This class is an instance of list class. """

    def print_sorted(self):
        """ Prints the list, in ascending order. """
        list = sorted(self)
        print(list)
