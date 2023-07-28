import pygame
import math
import time
import FW_map as m
import FW_Characters as c
import MenuScreen
import playSound as play

#Initialise pygame
pygame.init()

#Initialise music
pygame.mixer.pre_init(44100,16,2,4096)

#Initialise font
pygame.font.init()

#Sets screen size
size = 775
screen = pygame.display.set_mode((size, size))

#Creates map
running = True
map = m.Map(size, screen)

#Player Characters
map.insert(c.Archer('Rob', 2, 0, 0, True))
map.insert(c.Cavalry('Bob', 2, 0, 2, True))
map.insert(c.Berserker('Dob', 2, 2, 2, True))
map.insert(c.Warrior('Nob', 2, 2, 0, True))

#Play theme
play.Sound('MainTheme.mp3', 1, -1)

#Show menu, if we select instructions go to instructions
if MenuScreen.Menu(screen,size):
    #Click sound
    play.Sound('Click.mp3', 0.3, 1)
    #Instructions screen
    MenuScreen.Instructions(screen,size)

play.Sound('Click.mp3', 0.3, 1)
#Difficulty screen and set difficulty to option picked
difficulty = MenuScreen.Difficulty(screen)
play.Sound('Click.mp3', 0.3, 1)
time.sleep(0.3)

#Create enemies according to difficulty
if difficulty == 'easy':
    map.SetDifficulty(1)

if difficulty == 'medium':
    map.SetDifficulty(2)

if difficulty == 'hard':
    map.SetDifficulty(3)

map.createMap()

#Stops music
pygame.mixer.music.stop()
while running:
    #Sets all characters to ready to move
    for p in map.entities:
        p.moved = False

    #Draw map
    map.drawMap()

    pTurn = True
    while pTurn:
        #If music isn't playing, play music
        if not pygame.mixer.music.get_busy():
            play.Sound('PlayerTurn.mp3', 1, -1)

        #Do player turn
        map.playerTurn()
        pTurn = False

        count = 0
        #If players can move, its players turn
        for p in map.entities:
            if p.moved == False and p.player == True:
                pTurn = True
            if p.player:
                count += 1

        #If you have no players, show lose screen
        if count == 0:
            pygame.mixer.music.stop()
            self.screen.fill((0,0,0))
            t.text(self.screen, 'YOU LOSE', 200, 200, 50)
            t.text(self.screen, 'You have successfully completed Frontier Wars demo', 50, 400, 30)
            time.sleep(5)
            pygame.quit()

        #Update map
        map.drawMap()

    #Stop music
    pygame.mixer.music.stop()

    #Do enemy turn
    map.enemyTurn()

    #Check for quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
