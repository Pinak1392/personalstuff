import math
import random


def maze(dw, dh, max_tunnels, max_t_length, enemies):
    # Creates map grid and sets everything initially as unusable terrain
    grid = []
    for y in range(dh):
        row = []
        for x in range(dw):
            row.append(1)
        grid.append(row)

    # When choosing a path to clear these are the directions you can go. The order is up, down, left and right.
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    # Creates a starting point
    row = math.floor(random.random() * dh)
    column = math.floor(random.random() * dw)

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
               (row == (dh - 1) and randD[0] == 1) or \
               (column == (dw - 1) and randD[1] == 1):
               #inside if loop
               break

            else:
                grid[row][column] = 0
                row += randD[0]
                column += randD[1]
                t_length += 1

        # makes sure you made a tunnel
        if t_length > 0:
            lastD = randD
            max_tunnels -= 1

    for y in range(3):
        for x in range(3):
            grid[y][x] = 1;

    maxEn = enemies
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            randEn = math.floor(random.random() * (15 - maxEn))
            if enemies > 0 and randEn == 1 and grid[y][x] == 0:
                grid[y][x] = 2
                enemies -= 1

    for y in range(3):
        for x in range(3):
            grid[y][x] = 0;

    return grid
