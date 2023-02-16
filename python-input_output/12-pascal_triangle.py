#!/usr/bin/python3
'''function crated a pascal triangle'''


def pascal_triangle(n):
    """validation"""
    if n <= 0:
        return []
    '''matriz x matriz'''
    triangle = [[1 for column in range(row)] for row in range(1, n + 1)]
    '''iterates'''
    for i in range(2, n):
        for j in range(1, i):
            triangle[i][j] = triangle[i - 1][j] + triangle[i - 1][j - 1]
    '''return'''
    return triangle
