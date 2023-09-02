#!/usr/bin/python3
""" Island perimeter task """


def island_perimeter(grid):
    """Method that calculates the island
    perimeter
    """

    rows = len(grid)
    columns = len(grid[0])
    perimeter = 0
    connections = 0

    # iterate through the list items in each row
    # Check if any item is 1, increment the perimeter by 1
    for row in range(rows):
        for column in range(columns):
            if grid[row][column] == 1:
                perimeter += 4
                # check if there's a connection on the top and left
                if row != 0 and grid[row - 1][column] == 1:
                    connections += 1
                if column != 0 and grid[row][column - 1] == 1:
                    connections += 1

    return perimeter - (connections * 2)
