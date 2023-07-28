from baseSprites import *

#This is the top bar on the level
class TopBar(pygame.sprite.Sprite):
    def __init__(self, lvl, width, height, x, y, color=BLACK, backg=WHITE):
        super().__init__()
        self.font = pygame.font.SysFont('TimesNewRoman', height)
        self.color = color

        self.image = pygame.Surface([width, height])
        self.image.fill(backg)
        self.backg = backg

        self.width = width
        self.height = height
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        #The left and right buttons
        self.buttons = pygame.sprite.Group()
        self.buttons.add(Button('>', height, GREEN, self.width/10, height, (9*self.width)/10, 0, lvl + 1))
        if lvl > 1:
            self.buttons.add(Button('<', height, GREEN, self.width/10, height, 0, 0, lvl - 1))

        self.buttons.draw(self.image)

        text = self.font.render(f"Level {lvl}", True, color)
        text_rect = text.get_rect(center=(self.width/2, self.height/2))
        self.image.blit(text, text_rect)

        self.font = pygame.font.SysFont('TimesNewRoman', int((3*height)/4))

        if lvl > 1:
            text = self.font.render(f'Level {lvl - 1}', True, color)
            text_rect = text.get_rect(midleft=(self.width/10, self.height/2))
            self.image.blit(text, text_rect)

        text = self.font.render(f'Level {lvl + 1}', True, color)
        text_rect = text.get_rect(midright=((9*self.width)/10, self.height/2))
        self.image.blit(text, text_rect)
    
    def clicked(self, pos):
        #Gets relative position of mouse
        posx = pos[0] - self.rect.x
        posy = pos[1] - self.rect.y
        pos = (posx,posy)
        #Returns button values
        for i in [s for s in self.buttons if s.rect.collidepoint(pos)]:
            return i.returned

#A simple title thing
class Title(pygame.sprite.Sprite):
    def __init__(self, title, width, height, x, y, color=BLACK, backg=WHITE, size=None):
        super().__init__()
        if size:
            self.font = pygame.font.SysFont('TimesNewRoman', size)
        else:
            self.font = pygame.font.SysFont('TimesNewRoman', height)
        self.color = color

        self.image = pygame.Surface([width, height])
        self.image.fill(backg)
        self.backg = backg

        self.width = width
        self.height = height
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        text = self.font.render(title, True, color)
        text_rect = text.get_rect(center=(self.width/2, self.height/2))
        self.image.blit(text, text_rect)