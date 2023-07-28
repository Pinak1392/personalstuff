import pygame
import time

#Creates text
def text(screen, text, x, y, size):
    pygame.font.init()

    #If its a line of text just print it out at position
    if type(text) == str:
        myfont = pygame.font.SysFont('Sans', size)
        textsurface = myfont.render(text, False, (255, 255, 255))
        screen.blit(textsurface,(x,y))
        pygame.display.flip()
    else:
        #Otherwise if its a list, print them out one below the other with delays
        for i in range(len(text)):
            myfont = pygame.font.SysFont('Sans', size)
            textsurface = myfont.render(text[i], False, (255, 255, 255))
            screen.blit(textsurface,(x,(y + i * size)))
            pygame.display.flip()
            time.sleep(1)
