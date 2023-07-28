import pygame
import Text as t

#Create a button
#Initialise as a pygame sprite
class Button (pygame.sprite.Sprite):
    def __init__(self, image, x, y, width, height):
    #Pass in the image of button, x, y and size

        # Call the parent class (Sprite) constructor
        super().__init__()

        # Load the image or create an invisible surface
        if image != 'none':
            self.image = pygame.image.load(image).convert()
            self.image = pygame.transform.scale(self.image, (width, height))

        else:
            self.image = pygame.Surface([width, height])
            self.image.fill((255,255,255))
            self.image.set_colorkey((255,255,255))

        # Fetch the rectangle object that has the dimensions of the image.
        # Then we set the x and y postitions
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

#Create text button
class TextButton (pygame.sprite.Sprite):
    def __init__(self, text, size, color, width, height, x, y):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        #Creates text
        self.font = pygame.font.SysFont("Sans", size)
        self.textsurface = self.font.render(text, 1, (255,255,255))

        #Creates box surface
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        w = self.textsurface.get_width()
        h = self.textsurface.get_height()

        #Puts the text on the sprite surface and centers it
        self.image.blit(self.textsurface, [width/2 - w/2, height/2 - h/2])

        #Sets position of the surface
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
