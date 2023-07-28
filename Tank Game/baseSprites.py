import pygame
from color import *
from matrix import *
import math

pygame.display.init()

#This is the button base function. If you click on it, it returns something.
#I use button aas a base for basically everything.
class Block (pygame.sprite.Sprite):
    def __init__(self, color, x, y, width, height):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        self.color = color
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        
        self.image = pygame.Surface((width, height))
        self.image.fill(color)

        #Sets position of the surface
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.pointCoords = [self.rect.topleft,self.rect.topright,self.rect.bottomright,self.rect.bottomleft]
        self.eq = []
        for i in range(1,len(self.pointCoords)):
            self.eq.append(lineEq(self.pointCoords[i-1],self.pointCoords[i]))
        self.eq.append(lineEq(self.pointCoords[0],self.pointCoords[-1]))


#Governs sprites with image backgrounds
class ImageSprite (pygame.sprite.Sprite):
    def __init__(self, width, height, x, y, image):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        #Creates box surface
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (math.floor(width), math.floor(height)))

        #Sets position of the surface
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y