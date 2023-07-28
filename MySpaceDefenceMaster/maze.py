import math
import random


def maze(dimension, max_tunnels, max_t_length):
    # Creates map grid and sets everything initially as unusable terrain
    grid = []
    for y in range(dimension):
        row = []
        for x in range(dimension):
            row.append('#')
        grid.append(row)

    # When choosing a path to clear these are the directions you can go. The order is up, down, left and right.
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    # Creates a starting point
    row = math.floor(random.random() * dimension)
    column = math.floor(random.random() * dimension)

    # Sets this to the last direction so that it doesn't walk back.
    lastD = [2, 2]
    randD = []

    while max_tunnels > 0:
        # sets randD to a random direction. Then checks if the random direction is the opposite of its last direction. If this is case, it picks new.
        randD = directions[math.floor(random.random() * len(directions))]
        while (randD[0] == -lastD[0] and randD[1] == -lastD[1]) or (randD[0] == lastD[0] and randD[1] == lastD[1]):
            randD = directions[math.floor(random.random() * len(directions))]

        # How many tiles the path clearer will move across.
        length = math.ceil(random.random() * max_t_length)
        # counter for the path length
        t_length = 0

        # As long as you haven't hit the edge of grid or tunnel length. Keep going.
        while t_length < length:
            if (row == 0 and randD[0] == -1) or \
               (column == 0 and randD[1] == -1) or \
               (row == (dimension - 1) and randD[0] == 1) or \
               (column == (dimension - 1) and randD[1] == 1):
                break

            else:
                grid[row][column] = '.'
                row += randD[0]
                column += randD[1]
                t_length += 1

        # makes sure you made a tunnel
        if t_length > 0:
            lastD = randD
            max_tunnels -= 1

    return grid
