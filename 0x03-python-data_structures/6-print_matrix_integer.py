#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """Print a matrix of integers"""
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print("{}".format(matrix[i][j]), sep='', end=" ")
        print(sep=' ')
