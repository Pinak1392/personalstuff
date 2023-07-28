import pygame
from color import *
import baseSprites as obj
from tank import *

# Initialize the game engine
pygame.init()
pygame.font.init()

#Governs rendering the level
def renderLVL(size, lvl, screen):
    #Creates a group of sprites
    LVLsprites = pygame.sprite.Group()
    #Goes through level and creates the sprites and adds them to the sprite list based on the map layout.
    y = 0
    for i in lvl:
        x = 0
        for b in i:
            #Puts the right sprites in based on the value of the level layout list
            if b == 1:
                LVLsprites.add(obj.Block(BROWN, x, y, size[0]/len(i), size[1]/len(lvl)))
            if b == 2:
                tank = Tank(x + (size[0]/(2 * len(i))), y + (size[1]/(2 * len(lvl))), size[0]/(2 * len(i)), size[1]/(2 * len(lvl)))
                LVLsprites.add(tank)
            
            x += size[0]/len(i)
        y += size[1]/len(lvl)

    tank.lvl = LVLsprites

    #Return bot object and the level sprites
    return LVLsprites, tank
