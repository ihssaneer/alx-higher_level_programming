#!/usr/bin/python3
""" This module contain is_same_class function """


def is_same_class(obj, a_class):
    """ This function verify if an object is exactly
            an instance of the specified class. """
    if type(obj) is a_class:
        return (True)
    else:
        return (False)
