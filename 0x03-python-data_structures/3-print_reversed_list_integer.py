#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        exit(0)
    my_list.reverse()
    for x in my_list:
        print("{:d}".format(x))
