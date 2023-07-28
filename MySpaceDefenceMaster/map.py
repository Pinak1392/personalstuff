#Creates a randomized map layout
import maze as m
#Imports math
import math
#Imports random
import random
#Imports in the Pathfinder so that enemies can walk towards the player
import Pathfinder


class map:
    #Creates the map
    def __init__(self, dimension, max_tunnels, max_t_length, enemies, difficulty, level):
        #The dimensions of the map
        self.dimension = dimension
        #Creates a randomized grid.
        self.grid = m.maze(dimension, max_tunnels, max_t_length)
        # stores enemy positions
        self.enpos = []

        #Changes the enemy ratios based on the difficulty
        if difficulty == 'm':
            # one levels below start player level
            one_lvlb = math.ceil(enemies / 5)
            # one levels above start player level
            no_lvl = math.ceil(enemies / 4)
            # two levels above start player level
            one_lvl = math.ceil(enemies / 4)
            # three levels above start player level
            two_lvl = math.ceil(enemies / 5)
            # four levels above start player level
            three_lvl = math.ceil(enemies / 10)
        elif difficulty == 'h':
            # one levels below start player level
            one_lvlb = math.ceil(enemies / 10)
            # no levels above start player level
            no_lvl = math.ceil((3 * enemies) / 10)
            # one levels above start player level
            one_lvl = math.ceil(enemies / 4)
            # two levels above start player level
            two_lvl = math.ceil(enemies / 4)
            # three levels above start player level
            three_lvl = math.ceil(enemies / 10)
        elif difficulty == 'l':
            # one levels below start player level
            one_lvlb = 0
            # no levels above start player level
            no_lvl = math.ceil(enemies / 4)
            # one levels above start player level
            one_lvl = math.ceil(enemies / 2)
            # two levels above start player level
            two_lvl = math.ceil(enemies / 8)
            # three levels above start player level
            three_lvl = math.ceil(enemies / 8)
        elif difficulty == 'g':
            # one levels below start player level
            one_lvlb = 0
            # no levels above start player level
            no_lvl = 0
            # one levels above start player level
            one_lvl = math.ceil(enemies / 2)
            # two levels above start player level
            two_lvl = math.ceil(enemies / 4)
            # three levels above start player level
            three_lvl = math.ceil(enemies / 4)
        else:
            # one levels below start player level
            one_lvlb = math.ceil(enemies / 4)
            # no levels above start player level
            no_lvl = math.ceil(enemies / 2)
            # one levels above start player level
            one_lvl = math.ceil(enemies / 8)
            # two levels above start player level
            two_lvl = math.ceil(enemies / 8)
            # three levels above start player level
            three_lvl = 0

        #While you haven't hit the maximum enemies. Place down enemies of a certain level.
        while enemies > 0:
            #If you have some one_lvlb enemies left to place, the next enemy placed will be a one_lvlb enemy.
            if one_lvlb > 0:
                '''Enemy level is set to 1 levels below the inputed player level. one_lvlb is also decreased by one.
                When one_lvlb hits 0. No more enemies which are 1 levels below the inputed player level can be placed.
                The same logic applies for the other levels aswell.'''
                enLvl = level - 1
                one_lvlb -= 1
            #If you have some no_lvl enemies left to place, the next enemy placed will be a no_lvl enemy.
            elif no_lvl > 0:
                enLvl = level
                no_lvl -= 1
            #If you have some two_lvl enemies left to place, the next enemy placed will be a two_lvl enemy.
            elif two_lvl > 0:
                enLvl = level + 2
                two_lvl -= 1
            #If you have some one_lvl enemies left to place, the next enemy placed will be a one_lvl enemy.
            elif one_lvl > 0:
                enLvl = level + 1
                one_lvl -= 1
            #If you have some three_lvl enemies left to place, the next enemy placed will be a three_lvl enemy.
            elif three_lvl > 0:
                enLvl = level + 3
                three_lvl -= 1


            # Randomly selects a spot on the map. Then checks if the spot is empty. If it is, it places enemy there. Otherwise it finds a new spot.
            while True:
                #Creates a new random spot on the map.
                row = math.floor(random.random() * dimension)
                column = math.floor(random.random() * dimension)

                empty = True
                #Checks if the spot is empty.
                if self.grid[row][column] == '.':
                    #Checks if an enemy is already on the spot.
                    for x in self.enpos:
                        if [row, column] in x:
                            empty = False

                    if empty:
                        #If the place is empty, it sets the enemies position there. And sets the enemies level to the level selected above.
                        self.enpos.append([[row, column], enLvl])
                        break

            #Decreases the amount enemies to place by one, because an enemy has been placed.
            enemies -= 1

        counter = 0
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                empty = True
                #Checks if it is a valid space to place something on.
                if self.grid[y][x] == '.':
                    #Checks if an enemy is there
                    for i in self.enpos:
                        if [y, x] in i:
                            #If an enemy is on the space, it is no longer empty.
                            empty = False

                    #The map is checked going left to right on all the rows from top to bottom.
                    if empty:
                        #In the first empty space on the map after the enemies have been placed. You place the player.
                        if counter == 0:
                            self.p = [y, x]

                        #In the tenth empty space on the map after the enemies have been placed. You place the shop.
                        if counter == 10:
                            self.spos = [y, x]

                        '''After you have encountered one empty space. You increase the counter by one
                        to signify that you have visited one more empty space'''
                        counter += 1

    #Moves the player on the map.
    def p_move(self, y, x):
        #If the player is made to move diagonally e.g. x=1 and y=1. Or told to stay still. Exit the function and return False.
        if (y > 0 and x > 0) or (y == x):
            return False

        #Sets the position it is on to empty.
        self.grid[self.p[0]][self.p[1]] = '.'

        #Set the x variable to the new player x position.
        x += self.p[1]
        #Checks if the new x is within the map bounds. If it isn't, return False.
        if x >= (self.dimension):
            return False
        elif x < 0:
            return False

        #Set the y variable to the new player y position.
        y += self.p[0]
        #Checks if the new y is within the map bounds. If it isn't, return False.
        if y >= (self.dimension):
            return False
        elif y < 0:
            return False

        #Checks if the player has moved on to a enemy.
        for i in self.enpos:
            if [y, x] in i:
                ''' If the player has moved on to an enemy. Get the enemy level and return the keyword enemy along with the enemy level.
                Also remove the enemy from the map, and move the player to the place you were moving the player too.'''
                enemylevel = i[1]
                self.enpos.remove(i)
                self.p = [y, x]
                return 'enemy' + str(enemylevel)

        #Checks if player has been moved on to a shop.
        if [y, x] == self.spos:
            #If the player moved on to the shop. Return the keword shop and move the player to the place you were moving them too.
            self.p = [y, x]
            return 'shop'

        #Checks if the player moves on to impassable terrain.
        if self.grid[y][x] == '#':
            #Return False and don't move player to the space you were moving it too, if the player moved on to invalid terrain.
            return False

        #Moves player to the space you were moving it to. And returns True.
        self.p = [y, x]
        return True

    #Moves the enemies.
    def enemyMove(self):
        #Stores the amount of enemies there are on a map.
        enNum = len(self.enpos)
        
        #Goes through the enemy positions.
        for i in range(enNum):
            '''Puts the enemy position through the pathfinder a star algorithm.
            It sends back a list of tuples which tells the coordinates that show the best path from the enemy to the player.
            The first and last coordinates are the position the enemy currently is on, and the position the player is on.
            It also sends back and empty list if it can't find a path to the player.'''
            enCoordinates = Pathfinder.astar(self.grid,tuple(self.enpos[i][0]),tuple(self.p))
            #If for some reason the Pathfinder spits out a list of less than 1 tuple. Don't tamper with that enemies position.
            if len(enCoordinates) > 1:
                #Gets that enemies current position.
                enY = self.enpos[i][0][0]
                enX = self.enpos[i][0][1]
                #Sets the enemies position place to an empty space.
                self.grid[enY][enX] = '.'
                #Gives the enemy a new position, according to the 2 tuple given by the a* algorithm
                self.enpos[i][0] = list(enCoordinates[1])
                '''Places a placeholder on the grid, in position of the enemy.
                This is to signify its place there so that other enemies won't be able to pathfind to that position.'''
                self.grid[enCoordinates[1][0]][enCoordinates[1][1]] = 'e'

                #Checks if the enemy has moved on to the player.
                if self.enpos[i][0] == self.p:
                    #If the enemy has moved on to the player. It changes the placeholder e to an empty space again.
                    self.grid[enCoordinates[1][0]][enCoordinates[1][1]] = '.'
                    #enemylevel gets the level of the enemy
                    enemylevel = self.enpos[i][1]
                    #The enemy is removed from the map
                    self.enpos.remove(self.enpos[i])
                    #The enemy's level is returned
                    return enemylevel

        #Since no enemy has encountered a player, return False.
        return False

    #This creates the map with all the enemies and player and shop on it. Then returns it.
    def update(self):
        ngrid = self.grid
        ngrid[self.spos[0]][self.spos[1]] = 's'
        for i in self.enpos:
            ngrid[i[0][0]][i[0][1]] = str(i[1])

        ngrid[self.p[0]][self.p[1]] = 'p'
        return ngrid
