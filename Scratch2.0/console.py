import pygame
from pygame_textinput import *

class Console(pygame.sprite.Sprite):
    def __init__(self, width, height, x, y, text='', color=WHITE, backg=BLACK, size=20):
        super().__init__()

        self.text = text
        self.font = pygame.font.SysFont('TimesNewRoman', size)
        self.color = color

        self.image = pygame.Surface([width, height])
        self.image.fill(backg)
        self.backg = backg

        self.width = width
        self.height = height
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.lines = math.floor(self.height/self.font.get_height())

        self.active = False
        self.buttonOff = False

        self.textBlit()

    #Display the stuff
    def textBlit(self):
        self.image.fill(self.backg)
        textLines = wrap_multi_line(self.text, self.font, self.width - 8)

        #Scrolling part for console. If there isn't a given location it will always scroll to bottom.
        if 'location' not in self.__dict__:
            location = len(textLines) - 1
        else:
            location = self.location

        #Gets the scroll segment
        textLines = getSeg(textLines, self.lines, location)

        for i in range(len(textLines)):
            nlines = textLines[i]
            line = self.font.render(nlines, True, self.color)
            self.image.blit(line, (8, 2 + line.get_height() * i))

    #Updates the look
    def update(self, newLine):
        self.text += '\n' + newLine
        textLines = wrap_multi_line(self.text, self.font, self.width - 2)
        if len(textLines) > self.lines:
            self.text = self.text[len(textLines[0]) + 1:]

        self.textBlit()

#Modifications of console
class Tooltip(Console):
    def __init__ (self, tooltip, width, height, x, y):
        super().__init__(width, height, x, y, 'Objective\n' + tooltip, BLACK, WHITE)

#Basically a console with a scrollbar
class Help(Console):
    def __init__ (self, helpText, width, height, x, y, header=True):
        #Give it help tips header or not
        if header:
            super().__init__(width, height, x, y, 'Help tips\n' + helpText, BLACK, WHITE)
        else:
            super().__init__(width, height, x, y, helpText, BLACK, WHITE)
        #Decreases width and height to put in the scroll bar
        self.width = 9*width/10
        self.height = 9*height/10
        self.lines = math.floor(self.height/self.font.get_height())
        self.location = math.floor(self.lines/2)
        self.textBlit()
        #This is the scroll bar
        self.buttons = pygame.sprite.Group()
        self.buttons.add(Button('/\\', 30, RED, width/10 - 10, height/10, self.width + 10, 0, 'up'))
        self.buttons.add(Button('\/', 30, RED, width/10 - 10, height/10, self.width + 10, self.height, 'down'))
        self.buttons.add(Button('', 30, (140,140,120), width/10 - 10, height - ((2*height)/10), self.width + 10, height/10, False))
        self.buttons.draw(self.image)
    
    def clicked(self, pos):
        textLines = wrap_multi_line(self.text, self.font, self.width - 8)
        #Changes the position of the mouse in to the position with respect to the box
        posx = pos[0] - self.rect.x
        posy = pos[1] - self.rect.y
        pos = (posx,posy)
        for i in [s for s in self.buttons if s.rect.collidepoint(pos)]:
            if i.returned == 'up':
                #Location wont go higher if you hit max scroll
                self.location -= 1
                if self.location <= math.floor(self.lines/2):
                    self.location = math.floor(self.lines/2)
            
            elif i.returned == 'down':
                #Location wont go lower if you hit min scroll
                self.location += 1
                if self.location >= len(textLines) - math.floor(self.lines/2):
                    self.location = len(textLines) - math.floor(self.lines/2)

        self.textBlit()
        self.buttons.draw(self.image)