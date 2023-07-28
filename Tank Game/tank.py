from color import *
import pygame
import math
from baseSprites import *
from matrix import *

#sprite rotation
def rot_center(image, rect, angle):
    """rotate an image while keeping its center"""
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = rot_image.get_rect(center=rect.center)
    return rot_image,rot_rect

class Tank (ImageSprite):
    def __init__(self, x, y, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__(width, height, x, y, 'tank.jpg')
        self.width = width
        self.height = height
        self.rot = 0
        self.speed = 1
        self.col = (0,0)

        self.initImg = self.image

        #Sets position of the surface
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

        self.image, self.rect = rot_center(self.initImg, self.rect, self.rot - 90)
        self.pointCoords = [self.rect.topleft,self.rect.topright,self.rect.bottomright,self.rect.bottomleft]
        self.setEquations()

    def setEquations(self):
        self.eq = []
        for i in range(1,len(self.pointCoords)):
            self.eq.append(lineEq(self.pointCoords[i-1],self.pointCoords[i]))
        self.eq.append(lineEq(self.pointCoords[0],self.pointCoords[-1]))

    def rotation(self,degrees):
        for i in range(len(self.pointCoords)):
            self.pointCoords[i] = transform([translate(-self.rect.centerx,-self.rect.centery),rotate(degrees),translate(self.rect.centerx,self.rect.centery)],self.pointCoords[i])
        self.setEquations()


    #Rotates the tank left
    def left(self):
        self.rot += 2
        self.image, self.rect = rot_center(self.initImg, self.rect, self.rot - 90)
        self.rotation(2)
        if self.checkCollide():
            self.right()


    #Turns bot right
    def right(self):
        self.rot -= 2
        self.image, self.rect  = rot_center(self.initImg, self.rect, self.rot - 90)
        self.rotation(-2)
        if self.checkCollide():
            self.left()


    def back(self):
        sin = round(math.sin(math.radians(self.rot)), 2)
        cos = round(math.cos(math.radians(self.rot)), 2)

        self.rect.centerx += -self.speed * cos
        self.rect.centery += self.speed * sin

        for i in range(len(self.pointCoords)):
            self.pointCoords[i] = transform([translate(-self.speed * cos,self.speed * sin)],self.pointCoords[i])
        self.setEquations()
        if self.checkCollide():
            self.forward()


    def forward(self):
        sin = round(math.sin(math.radians(self.rot)), 2)
        cos = round(math.cos(math.radians(self.rot)), 2)

        self.rect.centerx += self.speed * cos
        self.rect.centery += -self.speed * sin
        for i in range(len(self.pointCoords)):
            self.pointCoords[i] = transform([translate(self.speed * cos,-self.speed * sin)],self.pointCoords[i])
        self.setEquations()
        if self.checkCollide():
            self.back()
        print(self.pointCoords)

    def checkCollide(self):
        for i in self.lvl:
            for a in i.eq:
                for b in self.eq:
                    if collision(a,b) and self != i:
                        return True


class Mark (Block):
    def __init__(self, x, y):
        # Call the parent class (Sprite) constructor
        super().__init__(RED, 5, 5, x, y)
        self.rect.centerx = x
        self.rect.centery = y

    def update(self, pos):
        self.rect.centerx = pos[0]
        self.rect.centery = pos[1]