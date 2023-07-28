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
fill = scenes['menu']['fill']

#The starting set of sprites to use
cursprites = scenes['menu']['cursprites']

while not done:
    # Clear the screen and set the screen background
    screen.fill(fill)

    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()

            # get a list of all sprites that are under the mouse cursor
            clicked_sprites = [s for s in cursprites if s.rect.collidepoint(pos)]
            #Activate the clicked sprites clicked function
            for clickedThings in clicked_sprites:
                if 'clicked' in dir(clickedThings):
                    if clickedThings.clicked(pos):
                        #If integer is outputed, play that level
                        if type(clickedThings.clicked(pos)) == int:
                            playing = True
                            out = clickedThings.clicked(pos)
                            while playing:
                                #Keep playing levels until you cant anymore. So if invalid level comes out or the person closes.
                                try:
                                    out = levelScreen(screen, out)
                                except:
                                    playing = False
                        else:
                            for output in clickedThings.clicked(pos):
                                #Changes screen based on output of button
                                exec(f"{output[1]} = scenes['{output[0]}']['{output[1]}']")

    #draw all the sprites
    cursprites.draw(screen)

    #update screen
    pygame.display.flip()
 
# Be IDLE friendly
pygame.quit()