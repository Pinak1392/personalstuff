import pygame
import math
import time
import Button

#Menu Graphics
def Menu (screen, size):
    #Menu
    img = pygame.image.load('StartBackground.jpg')
    img = pygame.transform.scale(img, (size, size))
    screen.blit(img, (0,0))
    img = pygame.image.load('Logo.png')
    img = pygame.transform.scale(img, (400, 300))
    screen.blit(img, (200,100))
    start = Button.Button('Start.jpg', 150, 500, 200, 50)
    instruct = Button.Button('Instruction.jpg', 450, 500, 200, 50)
    mouse = Button.Button('none', 0, 0, 20, 20)
    menuSprites = pygame.sprite.Group()
    menuSprites.add(start)
    menuSprites.add(instruct)
    menuSprites.draw(screen)
    pygame.display.flip()

    #Logic for button clicks
    while True:
        for event in pygame.event.get():
            if pygame.MOUSEBUTTONDOWN == event.type:
                pos = pygame.mouse.get_pos()
                mouse.rect.x = pos[0]
                mouse.rect.y = pos[1]

                if pygame.sprite.collide_rect(mouse, start):
                    return False

                if pygame.sprite.collide_rect(mouse, instruct):
                    return True

            elif pygame.QUIT == event.type:
                pygame.quit()

#Graphics for intructions
def Instructions (screen, size):
    img = pygame.image.load('Instructions.jpg')
    img = pygame.transform.scale(img, (size, size))
    screen.blit(img, (0,0))
    pygame.display.flip()
    #Logic for scene change
    while True:
        for event in pygame.event.get():
            if pygame.MOUSEBUTTONDOWN == event.type:
                return True

            elif pygame.QUIT == event.type:
                pygame.quit()

#Graphics for Difficulty
def Difficulty (screen):
    screen.fill((0,0,0))
    easy = Button.TextButton('Easy', 25, (0,200,0), 350, 100, 200, 150)
    medium = Button.TextButton('Medium', 25, (200,200,0), 350, 100, 200, 350)
    hard = Button.TextButton('Hard', 25, (255,0,0), 350, 100, 200, 550)
    mouse = Button.Button('none', 0, 0, 10, 10)
    menuSprites = pygame.sprite.Group()
    menuSprites.add(easy)
    menuSprites.add(medium)
    menuSprites.add(hard)
    menuSprites.draw(screen)
    pygame.display.flip()

    #Button click logic for the difficulty menu
    while True:
        for event in pygame.event.get():
            if pygame.MOUSEBUTTONDOWN == event.type:
                pos = pygame.mouse.get_pos()
                mouse.rect.x = pos[0]
                mouse.rect.y = pos[1]

                if pygame.sprite.collide_rect(mouse, easy):
                    return 'easy'

                if pygame.sprite.collide_rect(mouse, medium):
                    return 'medium'

                if pygame.sprite.collide_rect(mouse, hard):
                    return 'hard'

            elif pygame.QUIT == event.type:
                pygame.quit()
