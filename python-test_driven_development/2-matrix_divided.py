#!/usr/bin/python3
'''function divided elements of the matrix'''


def matrix_divided(matrix, div):
    '''variable auxiliar'''
    aux = len(matrix[0])
    '''matrix is int or float'''
    if not all(list(map(lambda x: all(list(map(lambda num:
               isinstance(num, (int, float)), x))), matrix))):
        '''error of the matrix'''
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")
    elif not all(list(map(lambda x: len(x) == aux, matrix))):
        '''not it same size'''
        raise TypeError("Each row of the matrix must have the same size")
    elif not isinstance(div, (int, float)):
        '''div not is int or float'''
        raise TypeError("div must be a number")
    elif div == 0:
        '''div is zero'''
        raise ZeroDivisionError("division by zero")
    '''operation matrix'''
    result = list(map(lambda x: list(map(lambda y:
                  round(y / div, 2), x)), matrix))
    '''return the result'''
    return result
