#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """Returns the summation of two tuples"""
    if len(tuple_a) < 2 or len(tuple_b) < 2:
        if len(tuple_a) < 2:
            my_list = list(tuple_a)
            my_list.append(0)
            new_tuple = tuple(my_list)
            result = tuple(map(sum, zip(new_tuple, tuple_b)))
            return(str(result))
        else:
            my_list = list(tuple_b)
            my_list.append(0)
            new_tuple = tuple(my_list)
            if len(new_tuple) < 2:
                my_list = list(new_tuple)
                my_list.append(0)
                new_tuple = tuple(my_list)
            result = tuple(map(sum, zip(tuple_a, new_tuple)))
            return(str(result))
    elif len(tuple_a) > 2 or len(tuple_b) > 2:
        if len(tuple_a) > 2:
            new_tuple = tuple_a[:2]
            result = tuple(map(sum, zip(new_tuple, tuple_b)))
            return(str(result))
        else:
            new_tuple = tuple_b[:2]
            result = tuple(map(sum, zip(tuple_a, new_tuple)))
            return(str(result))
    else:
        result = tuple(map(sum, zip(tuple_a, tuple_b)))
        return(str(result))
