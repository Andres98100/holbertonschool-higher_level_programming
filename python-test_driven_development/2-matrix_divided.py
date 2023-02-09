#!/usr/bin/python3
'''function divided elements of the matrix'''


def matrix_divided(matrix, div):
    aux = len(matrix[0])
    '''it is validated that the matrix is int or float and that div is not zero.'''
    if not all(list(map(lambda x: all(list(map(lambda num: 
        isinstance(num, (int, float)), x))), matrix))):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    elif not all(list(map(lambda x: len(x) == aux, matrix))):
        raise TypeError("Each row of the matrix must have the same size")
    elif not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    result = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return result
