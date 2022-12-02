#!/usr/bin/python3

def no_c(my_string):
    """Remove character 'c' and 'C' from a string"""
    new_string = ""
    for i in my_string:
        if i == "c" or i == "C":
            continue
        else:
            new_string += i
    my_string = new_string
    return(my_string)
