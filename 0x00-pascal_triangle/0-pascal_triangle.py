#!/usr/bin/python3
""" Pascal Triangle """


def pascal_triangle(n):
    """ Algorithm that returns a list
    containing pascal triangle
    Args:
        n specifies the number of rows
    Return: List
    """
    if (n <= 0):
        return ([])
    else:
        data = [[] for i in range(n)]
        for i in range(n):
            for j in range(i+1):
                if (j == 0 or j == i):
                    data[i].append(1)
                else:
                    data[i].append(data[i-1][j] + data[i-1][j-1])
        return data
