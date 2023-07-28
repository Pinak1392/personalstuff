"""
truncline, wrapline and wrapmultiline
Borrowed from https://www.pygame.org/wiki/TextWrapping?parent=CookBook
"""
import pygame
from itertools import chain
from color import *
from baseSprites import *
import math

#Gets the segment of the lines for scroll
def getSeg(lis, lines, midLine):
    hlines = math.floor(lines/2)

    leftOver1 = 0
    leftOver2 = 0
    
    if len(lis[midLine:]) < hlines + 1:
        end = len(lis)
        leftOver1 = hlines - len(lis[midLine:])
    else:
        end = midLine + hlines + 1
    
    if len(lis[:midLine]) < hlines:
        start = 0
        leftOver2 = hlines - len(lis[:midLine])
    else:
        start = midLine - hlines

    if end + leftOver2 > len(lis[midLine:]):
        end = len(lis)
    else:
        end += leftOver2

    if start - leftOver1 < 0:
        start = 0
    else:
        start -= leftOver1
    
    ret = lis[start:end]
    if len(ret) > lines:
        ret = ret[:-1]

    return ret

#I think I got annoyed of typing that if statement thing out
def inRange(a, num, b):
    if num < a:
        return a
    elif num >= b:
        return b
    else:
        return num
        

def truncline(text, font, maxwidth):
        real=len(text)       
        stext=text           
        l=font.size(text)[0]
        cut=0
        a=0                  
        done=1
        old = None
        while l > maxwidth:
            a=a+1
            n=text.rsplit(None, a)[0]
            if stext == n:
                cut += 1
                stext= n[:-cut]
            else:
                stext = n
            l=font.size(stext)[0]
            real=len(stext)               
            done=0                        
        return real, done, stext             
        
def wrapline(text, font, maxwidth): 
    done=0                      
    wrapped=[]                  
                               
    while not done:             
        nl, done, stext=truncline(text, font, maxwidth) 
        wrapped.append(stext)                  
        text=text[nl:]                                 
    return wrapped


def wrap_multi_line(text, font, maxwidth):
    """ returns text taking new lines into account.
    """
    lines = chain(*(wrapline(line, font, maxwidth) for line in text.splitlines()))
    return list(lines)

#This is the textbox
class Textinput(pygame.sprite.Sprite):
    def __init__(self, name, width, height, x, y, text='', size=20, color=BLACK, backg=WHITE):
        super().__init__()

        #The text + the null cursor marker
        self.text = text + '\x00'
        self.font = pygame.font.SysFont('TimesNewRoman', size)
        self.color = color
        #Stores cursor location
        self.cursor = len(self.text) - 1

        self.name = name

        self.image = pygame.Surface([width, height])
        self.image.fill(backg)
        self.backg = backg

        #Runbutton
        self.runButton = pygame.sprite.Group()
        self.runButton.add(Button('Run', 30, RED, width, height/5, 0, 4*height/5, True))

        self.width = width
        self.height = 4*height/5
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.lines = math.floor(self.height/self.font.get_height())

        self.active = False
        self.buttonOff = False

        self.textBlit()

    def textBlit(self):
        self.image.fill(self.backg)

        textLines = wrap_multi_line(self.text, self.font, self.width - 2)

        #Gets location of text cursor
        location = 0
        for i in range(len(textLines)):
            if '\x00' in textLines[i]:
                location = i
                break
        
        #Gets segment based on cursor position
        textLines = getSeg(textLines, self.lines, location)

        for i in range(len(textLines)):
            nlines = textLines[i]
            #Replaces the null marker with a | cursor looking character and also draws the text on screen
            if '\x00' in nlines:
                if self.active:
                    nlines = nlines.replace('\x00','|')
                else:
                    nlines = nlines.replace('\x00','')
            line = self.font.render(nlines, True, self.color)
            self.image.blit(line, (2, 2 + line.get_height() * i))
        
        #Draws the run button
        self.runButton.draw(self.image)

    #What types the letters out
    def keyPressed(self, event):
        if self.active:
            uni = event.unicode

            if event.key == pygame.K_LEFT:
                self.text = self.text.replace('\x00', '')
                self.cursor = max(0, self.cursor - 1)
                self.text = self.text[:self.cursor] + '\x00' + self.text[self.cursor:]
            elif event.key == pygame.K_RIGHT:
                self.text = self.text.replace('\x00', '')
                self.cursor = min(self.cursor + 1, len(self.text))
                self.text = self.text[:self.cursor] + '\x00' + self.text[self.cursor:]
            elif event.key == pygame.K_RETURN:
                self.text = self.text[:self.cursor] + '\n' + self.text[self.cursor:]
                self.cursor += 1
            elif event.key == pygame.K_TAB:
                self.text = self.text[:self.cursor] + '    ' + self.text[self.cursor:]
                self.cursor += 4
            elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[:max(0,self.cursor - 1)] + self.text[self.cursor:]
                self.cursor = max(0, self.cursor - 1)
            elif uni != '':
                self.text = self.text[:self.cursor] + uni + self.text[self.cursor:]
                self.cursor += 1

            self.textBlit()
            return [[self, self.name]]

    def clicked(self, pos):
        #Gets relative position of mouse
        pos = (pos[0] - self.rect.x, pos[1] - self.rect.y)
        #If the button is On
        if not self.buttonOff:
            #If we didnt click the button but only the textbox
            if len([s for s in self.runButton if s.rect.collidepoint(pos)]) < 1:
                #make text box active and update it
                self.active = True
                self.textBlit()
            else:
                #otherwise make the button say abort, deactivate the textbox and the button and return the code
                self.active = False
                self.buttonOff = True
                for i in self.runButton:
                    i.text = 'Abort'
                    i.update()
                self.textBlit()
                return [[self.retString(), 'code']]

        else:
            #If we click while the button is off, it means we have aborted running code so
            #we change button to say run and return abort exception cause we click this
            #button while the interpreter is running.
            if not len([s for s in self.runButton if s.rect.collidepoint(pos)]) < 1:
                self.buttonOff = False
                for i in self.runButton:
                    i.text = 'Run'
                    i.update()
                self.textBlit()
                return ['exception', 'Exception: User stopped program']

    #Deactivate text box when you click off it
    def notClicked(self, pos):
        self.active = False
        self.textBlit()

    #When returning the code, remove the null character
    def retString(self):
        return self.text.replace('\x00','')
    

if __name__ == "__main__":
    print(getSeg([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],8,0))