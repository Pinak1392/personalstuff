import pygame
import baseSprites
import sprite as obj
from color import *
from levels import *

# Initialize the game engine
pygame.init()
pygame.font.init()

#Governs rendering the level
def renderLVL(size, lvl, x0, y, screen):
    #Creates a group of sprites
    LVLsprites = pygame.sprite.Group()
    #Adds the background
    LVLsprites.add(obj.Block((100,150,50), x0, y, size[0], size[1]))
    #Gets the level map and orientation of bot for the inputed level
    a, orientation, valids, validations, challenge = eval(f'lvl_{lvl}')
    #Goes through level and creates the sprites and adds them to the sprite list based on the map layout.
    for i in a:
        x = x0
        for b in i:
            #Puts the right sprites in based on the value of the level layout list
            if b == 1:
                LVLsprites.add(obj.ImgBlock("sprites/Brick.png", x, y, size[0]/len(i), size[1]/len(a)))
            elif b == 2:
                #Save the bot sprite so we can add it later
                bot = obj.Bot("sprites/Bot.png", x, y, size[0]/len(i), size[1]/len(a), a, screen, orientation)
            elif b == 3:
                LVLsprites.add(obj.ImgBlock("sprites/End.png", x, y, size[0]/len(i), size[1]/len(a)))
            elif type(b) == str:
                #Puts in a specific color based on the value in the level layout
                colDict = {
                    'g':GREEN,
                    'r':RED,
                    'b':BLUE,
                    'c':CYAN,
                    'y':YELLOW,
                    'p':PURPLE
                }
                LVLsprites.add(obj.Block(colDict[b], x, y, size[0]/len(i), size[1]/len(a)))

            x += size[0]/len(i)
        y += size[1]/len(a)
    
    #Add bot in last to have be drawn last.
    LVLsprites.add(bot)

    #Return bot object and the level sprites
    return LVLsprites, bot, valids, validations, challenge
