#!/usr/bin/python3
""" This module contain is_same_class class """


def is_same_class(obj, a_class):
    """ This class verify if an object is exactly
            an instance of the specified class. """
    if type(obj) is a_class:
        return (True)
    else:
        return (False)
