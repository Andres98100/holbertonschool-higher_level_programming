#!/usr/bin/python3
'''function crated a pascal triangle'''


def pascal_triangle(n):
    """Represents a Pascal's triangle of n"""
    if n <= 0:
        return []
    triangle = [[1 for column in range(row)] for row in range(1, n + 1)]
    for i in range(2, n):
        for j in range(1, i):
            triangle[i][j] = triangle[i - 1][j] + triangle[i - 1][j - 1]
    return triangle