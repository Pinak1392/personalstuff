import random

gSize = 3
x = [' ' for a in range(gSize**2)]

def determineVictory (grid, player):
    for a in range(gSize):
        for b in range(gSize):
            if grid[3*b + a] != player:
                break
        
        else:
            return True

    for a in range(gSize):
        for b in range(gSize):
            if grid[3*a + b] != player:
                break
        
        else:
            return True

    for a in range(gSize):
        if grid[4*a] != player:
            break

    else:
        return True

    for a in range(gSize):
        if grid[3*a + gSize - 1 - a] != player:
            break

    else:
        return True

    return False


class TicAi:
    def __init__(self, player):
        self.player = player
        if player == 'X':
            self.other = 'O'
        else:
            self.other = 'X'
    
    def score(self, grid):
        grid = grid[:]
        score = [0 for i in grid]
        for i in range(50):
            s = self.randTrial(grid)
            for x in range(len(score)):
                score[x] += s[x]

        ind = 0
        for a in range(len(score)):
            if score[a] >= ind and grid[a] == ' ':
                ind = a

        grid[ind] = self.player
        return grid

    def randTrial(self, grid):
        grid = grid[:]
        curPlay = [self.player,self.other]
        while ' ' in grid:
            if determineVictory(grid,self.player):
                return [0 if i == ' ' else 1 if i == self.player else -1 for i in grid]
            elif determineVictory(grid, self.other):
                return [0 if i == ' ' else -1 if i == self.player else 1 for i in grid]

            choices = []
            for x in range(len(grid)):
                if grid[x] == ' ':
                    choices.append(x)

            grid[random.choice(choices)] = curPlay[0]

            curPlay.reverse()


        if determineVictory(grid,self.player):
            return [0 if i == ' ' else 1 if i == self.player else -1 for i in grid]
        elif determineVictory(grid, self.other):
            return [0 if i == ' ' else -1 if i == self.player else 1 for i in grid]
        else:
            return [0 for i in grid]

a = TicAi('X')
b = TicAi('O')
grid = [' ' for i in range(gSize**2)]

    
while ' ' in grid:
    grid = a.score(grid)

    li = []
    for i in range(0,len(grid), gSize):
        li.append(''.join(grid[i:i+gSize]).replace(' ','.').replace('',' '))

    print('\n'.join(li))

    if determineVictory(grid,'X'):
        break

    grid = b.score(grid)

    li = []
    for i in range(0,len(grid), gSize):
        li.append(''.join(grid[i:i+gSize]).replace(' ','.').replace('',' '))

    print('\n'.join(li))
    
    if determineVictory(grid,'O'):
        break