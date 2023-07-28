import pygame
from scenes import *
from levelScreen import levelScreen

# Initialize the game engine
pygame.init()
pygame.font.init()

# Set the height and width of the screen
size = [1260, 740]
screen = pygame.display.set_mode(size)

#Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

#Background
fill = (100,200,100)

#The starting set of sprites to use
cursprites = scenes['menu']['cursprites']

while not done:
    # Clear the screen and set the screen background
    screen.fill(fill)

    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop

    levelScreen(screen, 1)

    #update screen
    pygame.display.flip()
 
# Be IDLE friendly
pygame.quit()