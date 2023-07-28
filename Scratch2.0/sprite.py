from baseSprites import *
import time
from copy import deepcopy

#sprite rotation
def rot_center(image, rect, angle):
    """rotate an image while keeping its center"""
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = rot_image.get_rect(center=rect.center)
    return rot_image,rot_rect

#A coloured block, button is the base class
class Block(Button):
    def __init__(self, color, x, y, sizeX, sizeY):
        super().__init__(None, 10, color, sizeX, sizeY, x, y)

#A image background block, ImageSprite is the base class
class ImgBlock(ImageSprite):
    def __init__(self, image, x, y, sizeX, sizeY):
        super().__init__(sizeX, sizeY, x, y, image)

#The class that governs the bot, base class is an Image Sprite
class Bot(ImageSprite):
    def __init__(self, image, x, y, sizeX, sizeY, level, screen, orientation):
        super().__init__(sizeX, sizeY, x, y, image)

        #Whether we are simulating or not
        self.sim = False
        #Initial x and y
        self.initx = x
        self.inity = y
        #self.o is the way a bot is facing, it is the navigator for the orientations list
        self.o = orientation
        self.inito = orientation
        #Level layout
        self.lvl = deepcopy(level)
        self.lvl0 = deepcopy(level)
        #The sizes
        self.sizeX = sizeX
        self.sizeY = sizeY
        #the directions it is facing.
        self.orientations = ['N','E','S','W']
        #So it can modify the bot on the screen
        self.screen = screen

        self.image, self.rect = rot_center(self.image, self.rect, -90 * self.o)
        #Sets initial direction of the robot
        self.initImg = self.image
        
        #Saves the block that the bot is on
        self.curBlock = 0

    def reset(self):
        self.o = deepcopy(self.inito)
        self.rect.x = self.initx
        self.rect.y = self.inity
        self.image = self.initImg
        self.lvl = deepcopy(self.lvl0)
    
    #Rotates the bot left
    def left(self, a):
        #Turns left as many times as you tell it to
        for i in range(a):
            #Loops around list
            if self.o > 0:
                self.o -= 1
            else:
                self.o = 3

            if not self.sim:
                #Uses rotation function to get new image
                self.image, self.rect = rot_center(self.image, self.rect, 90)
                
                # Clear the screen and set the screen background
                self.screen.fill(self.fill)
                
                #draw all the sprites
                self.curSprites.draw(self.screen)

                #update screen
                pygame.display.flip()
                time.sleep(0.5)

    #Turns bot right
    def right(self, a):
        #Turns right as many times as you tell it to,
        #everything here is the same as left function
        #but the degree of rotation is -90 and list
        #cycling is in the opposite direction.
        for i in range(a):
            if self.o < 3:
                self.o += 1
            else:
                self.o = 0

            if not self.sim:
                self.image, self.rect = rot_center(self.image, self.rect, -90)

                # Clear the screen and set the screen background
                self.screen.fill(self.fill)
                
                #draw all the sprites
                self.curSprites.draw(self.screen)

                #update screen
                pygame.display.flip()
                time.sleep(0.5)

    #Sensing function. Sees what is in front of it
    def see(self,a):
        try:
            #Allows capitalisation to be more lenient
            a = a.lower()

            #Holds what is looked for upon certain a input
            #e.g. if a is 'empty', bot will return true if
            #the square in front of it is 0 or a color block.
            #The letters are the color blocks.
            blockDict = {
                'wall': [1],
                'empty': [0, 'g', 'r', 'b', 'c', 'y', 'p'],
                'hazard': [4],
                'end': [3],
                'green':['g'],
                'red':['r'],
                'blue':['b'],
                'cyan':['c'],
                'yellow':['y'],
                'purple':['p'],
                'color':['r','g','b','c','y','p']
            }

            #The orientation determines what block is in front of the bot.
            #So depending on the orientation, we look at a different part of the list.
            if self.orientations[self.o] == 'N':
                #First we find where the bot is.
                for i in range(len(self.lvl)):
                    if 2 in self.lvl[i]:
                        for b in range(len(self.lvl[i])):
                            #Once we find the bot
                            if self.lvl[i][b] == 2:
                                #If on edge of the map, break out
                                if i - 1 < 0:
                                    break
                                #If the block is one of the valid blocks given by the input.
                                #Return True
                                if self.lvl[i-1][b] in blockDict[a]:
                                    return True

            #The rest is the same as the first except the block they look at around the bot is different.
            elif self.orientations[self.o] == 'E':
                for i in range(len(self.lvl)):
                    if 2 in self.lvl[i]:
                        for b in range(len(self.lvl[i])):
                            if self.lvl[i][b] == 2:
                                if b + 1 >= len(self.lvl[i]):
                                    break
                                if self.lvl[i][b+1] in blockDict[a]:
                                    return True
                
            elif self.orientations[self.o] == 'S':
                for i in range(len(self.lvl)):
                    if 2 in self.lvl[i]:
                        for b in range(len(self.lvl[i])):
                            if self.lvl[i][b] == 2:
                                if i + 1 >= len(self.lvl):
                                    break
                                if self.lvl[i+1][b] in blockDict[a]:
                                    return True
                
            elif self.orientations[self.o] == 'W':
                for i in range(len(self.lvl)):
                    if 2 in self.lvl[i]:
                        for b in range(len(self.lvl[i])):
                            if self.lvl[i][b] == 2:
                                if b - 1 < 0:
                                    break
                                if self.lvl[i][b-1] in blockDict[a]:
                                    return True

            #Return false when the block in front isn't the right block
            return False
        except:
            #If you get an invalid input, it returns error
            return ['err','Please provide see with (wall, empty, hazard, end or a valid color)']

    #This moves the bot
    def move(self,a):
        #This stops the bot from trying to move itself again
        done = False
        win = False
        dead = False

        #Move as many times as the input tells you to
        for i in range(a):
            #Changes the block you move to depending on your orientation
            if self.orientations[self.o] == 'N':
                #Find bot. Probs shoulda stored the info before. But, this is how it is now.
                for i in range(len(self.lvl)):
                    if 2 in self.lvl[i]:
                        for b in range(len(self.lvl[i])):
                            if self.lvl[i][b] == 2:
                                #If the block in front of you is the end or empty, you can move there.
                                if self.see('empty') or self.see('end'):
                                    if self.see('end'):
                                        win = True
                                    
                                    #Moves the sprite and changes its position in the list
                                    self.lvl[i][b] = self.curBlock
                                    self.curBlock = self.lvl[i-1][b]
                                    self.lvl[i-1][b] = 2
                                    if not self.sim:
                                        self.rect.y -= self.sizeY

                                    #Tell the program not to find the bot and move it anymore.
                                    done = True
                                    break
                    if done:
                        break

            #The next 3 are the same as the first. Just the block getting moved to is different
            elif self.orientations[self.o] == 'E':
                for i in range(len(self.lvl)):
                    if 2 in self.lvl[i]:
                        for b in range(len(self.lvl[i])):
                            if self.lvl[i][b] == 2:
                                if self.see('empty') or self.see('end'):
                                    if self.see('end'):
                                        win = True

                                    self.lvl[i][b] = self.curBlock
                                    self.curBlock = self.lvl[i][b+1]
                                    self.lvl[i][b+1] = 2
                                    if not self.sim:
                                        self.rect.x += self.sizeX

                                    done = True
                                    break
                    if done:
                        break
                
            elif self.orientations[self.o] == 'S':
                for i in range(len(self.lvl)):
                    if 2 in self.lvl[i]:
                        for b in range(len(self.lvl[i])):
                            if self.lvl[i][b] == 2:
                                if self.see('empty') or self.see('end'):
                                    if self.see('end'):
                                        win = True
                                    
                                    self.lvl[i][b] = self.curBlock
                                    self.curBlock = self.lvl[i+1][b]
                                    self.lvl[i+1][b] = 2
                                    if not self.sim:
                                        self.rect.y += self.sizeY

                                    done = True
                                    break
                    if done:
                        break
                
            elif self.orientations[self.o] == 'W':
                for i in range(len(self.lvl)):
                    if 2 in self.lvl[i]:
                        for b in range(len(self.lvl[i])):
                            if self.lvl[i][b] == 2:
                                if self.see('empty') or self.see('end'):
                                    if self.see('end'):
                                        win = True

                                    self.lvl[i][b] = self.curBlock
                                    self.curBlock = self.lvl[i][b-1]
                                    self.lvl[i][b-1] = 2
                                    if not self.sim:
                                        self.rect.x -= self.sizeX
                                    
                                    done = True
                                    break
                    if done:
                        break

            if not self.sim:
                # Clear the screen and set the screen background
                self.screen.fill(self.fill)
                
                #draw all the sprites
                self.curSprites.draw(self.screen)

                #update screen
                pygame.display.flip()
                time.sleep(0.3)

            done = False
            if win:
                return ['win']
            elif dead:
                return ['dead']