#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """Modify or replace element at a given index with a given element"""
    if idx < 0:
        return(my_list)
    elif idx > len(my_list):
        return(my_list)
    else:
        my_list[idx] = element
        return(my_list)
