import pygame
import text as t
from color import *
import math

pygame.display.init()

#This is the button base function. If you click on it, it returns something.
#I use button aas a base for basically everything.
class Button (pygame.sprite.Sprite):
    def __init__(self, text, size, color, width, height, x, y, returned = None, textFill=WHITE):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        self.text = text
        self.size = size
        self.color = color
        self.width = width
        self.height = height
        self.textFill = textFill
        self.x = x
        self.y = y

        #Creates text, if you have an inputed text
        if text:
            self.font = pygame.font.SysFont("Sans", size)
            self.textsurface = self.font.render(text, 1, textFill)

        #Creates box surface. If you have a color, fill in the surface with that color.
        #Otherwise, give a transparent background.
        self.image = pygame.Surface((width, height))
        if color != None:
            self.image.fill(color)
        else:
            self.image = pygame.Surface([width,height], pygame.SRCALPHA, 32)
            self.image = self.image.convert_alpha()
        
        #Put text on surface if you have an inputed text
        if self.text:
            w = self.textsurface.get_width()
            h = self.textsurface.get_height()

            #Puts the text on the sprite surface and centers it
            self.image.blit(self.textsurface, [width/2 - w/2, height/2 - h/2])

        #Sets position of the surface
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        #What to return when clicked
        self.returned = returned

    def clicked(self, pos):
        if self.returned is None:
            return ('trash', 'dump')
        else:
            return self.returned

    def update(self):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        #Creates text, if you have an inputed text
        if self.text:
            self.font = pygame.font.SysFont("Sans", self.size)
            self.textsurface = self.font.render(self.text, 1, self.textFill)

        #Creates box surface. If you have a color, fill in the surface with that color.
        #Otherwise, give a transparent background.
        self.image = pygame.Surface((self.width, self.height))
        if self.color != None:
            self.image.fill(self.color)
        else:
            self.image = pygame.Surface([self.width,self.height], pygame.SRCALPHA, 32)
            self.image = self.image.convert_alpha()
        
        #Put text on surface if you have an inputed text
        if self.text:
            w = self.textsurface.get_width()
            h = self.textsurface.get_height()

            #Puts the text on the sprite surface and centers it
            self.image.blit(self.textsurface, [self.width/2 - w/2, self.height/2 - h/2])

        #Sets position of the surface
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        #What to return when clicked
        self.returned = self.returned

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