#!/usr/bin/python3
'''function divided elements of the matrix'''


def matrix_divided(matrix, div):
    '''validates that the lists of the array are int or float'''
    if not all(list(map(lambda x: isinstance(x, int) and (x, float), matrix))):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    aux = len(matrix[0])
    '''it is validated that the size of the lists are the same'''
    if not all(list(map(lambda x: len(x) == aux, matrix))):
        raise TypeError("Each row of the matrix must have the same size")
    '''validates that div is int or float'''
    if not isinstance(div, int) and isinstance(div, float):
        raise TypeError("div must be a number")
    '''div different to zero'''
    if div == 0:
        raise ZeroDivisionError("division by zero")
    result = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return result
