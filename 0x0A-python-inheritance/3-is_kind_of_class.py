#!/usr/bin/python3
""" This module contain the function : is_kind_of_class """


def is_kind_of_class(obj, a_class):
    """ This function verify if an object is an instance of, or an instance
            of a class that inherited from, the specified class.
        obj : the object whose type/class needs to be checked.
        a_class : the class against which the type of the object is checked.
        Return : True in success and Flase in failure. """
    return isinstance(obj, a_class)
