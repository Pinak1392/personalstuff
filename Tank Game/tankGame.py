import pygame
from renderLvl import *
from tank import *

# Initialize the game engine
pygame.init()

# Set the height and width of the screen
size = [1200, 700]
screen = pygame.display.set_mode(size)
fill = (100,255,100)
done = False

lvl = [
       [0,1,1,0,1,0,0,0,1,0,0,0],
       [2,0,1,0,1,0,1,0,1,1,0,0],
       [0,0,0,0,1,0,0,0,0,0,0,1],
       [0,1,0,0,0,0,1,1,1,0,0,1],
       [0,1,1,0,0,1,1,1,1,0,0,1],
       [0,1,0,0,0,1,1,1,0,0,1,1],
       [0,0,0,1,0,0,0,0,0,0,0,0]
      ]
lvlSprites, tank = renderLVL(size, lvl, screen)

while not done:
    # Clear the screen and set the screen background
    screen.fill(fill)
    keys = pygame.key.get_pressed()  #checking pressed keys
    if keys[pygame.K_LEFT]:
        tank.left()
    if keys[pygame.K_RIGHT]:
        tank.right()
    if keys[pygame.K_UP]:
        tank.forward()
    if keys[pygame.K_DOWN]:
        tank.back()
    if keys[pygame.K_a]:
        print(pygame.mouse.get_pos())

    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop

    lvlSprites.draw(screen)

    #update screen
    pygame.display.flip()
 
# Be IDLE friendly
pygame.quit()