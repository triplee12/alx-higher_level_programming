#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """Print a list of integers in reverse order"""
    length = len(my_list)
    for i in range(int(length / 2)):
        temp = my_list[i]
        my_list[i] = my_list[length - i - 1]
        my_list[length - i - 1] = temp

    for j in range(len(my_list)):
        print("{:d}".format(my_list[j]))
