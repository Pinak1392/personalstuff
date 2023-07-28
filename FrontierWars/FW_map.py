import maze
import math
import pygame
import random
import Pathfinder
import time
import Text as t
import Button
import playSound as play
import FW_Characters as char

class Map():
    #Creates map and sets sizes and creates entities list
    def __init__ (self, size, screen):
        self.gSize = 12
        self.cSize = 2*size/3
        self.entities = []
        self.screen = screen

    def createMap (self):
        stringAlpha = 'abcdefghijklmnopqrstuvwxyz'
        names = []
        for a in range(len(stringAlpha)):
            names.append(stringAlpha[a] + 'a')
            names.append(stringAlpha[a] + 'e')
            names.append(stringAlpha[a] + 'i')
            names.append(stringAlpha[a] + 'o')
            names.append(stringAlpha[a] + 'u')

        self.grid = maze.maze(18, 12, 30, 20, 4)
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                if self.grid[y][x] == 2:
                    self.grid[y][x] = 0
                    a = math.floor(random.random() * len(names))
                    b = math.floor(random.random() * len(names))
                    c = math.floor(random.random() * len(stringAlpha))
                    name = names[a] + names[b] + stringAlpha[c]
                    name = name[0].upper() + name[1:]
                    roster = [char.Archer(name, self.diff, x, y), char.Warrior(name, self.diff, x, y), char.Berserker(name, self.diff, x, y), char.Cavalry(name, self.diff, x, y)]
                    self.insert(roster[math.floor(random.random() * len(roster))])

    #Inserts an entity in to entities list
    def insert (self, character):
        self.entities.append(character)

    def SetDifficulty (self, difficulty):
        self.diff = difficulty

    #Draws the map
    def drawMap (self):
        self.screen.fill((0, 0, 0))
        for y in range(len(self.grid)):
            for x in range(len(self.grid[0])):
                if self.grid[y][x] == 1:
                    img = pygame.image.load('Mountain.jpg')
                else:
                    img = pygame.image.load('Grass.jpg')

                img = pygame.transform.scale(img, (math.floor(self.cSize/self.gSize), math.floor(self.cSize/self.gSize)))
                self.screen.blit(img, (x * (self.cSize/self.gSize), y * (self.cSize/self.gSize)))

        #Player drawing
        for i in self.entities:
            img = i.img
            img = pygame.transform.scale(img, (math.floor(self.cSize/self.gSize), math.floor(self.cSize/self.gSize)))
            self.screen.blit(img, (i.x * (self.cSize/self.gSize), i.y * (self.cSize/self.gSize)))

            #If they have moved, put a grey color on it.
            if i.moved:
                s = pygame.Surface((math.floor(self.cSize/self.gSize),math.floor(self.cSize/self.gSize)), pygame.SRCALPHA)
                s.fill((50,50,50,128))
                self.screen.blit(s, (i.x * (self.cSize/self.gSize), i.y * (self.cSize/self.gSize)))

        pygame.display.flip()

    #Creates the action menu
    def actionMenu (self):
        #Create buttons
        attack = Button.TextButton('Attack', 20, (255, 0, 0), 200, 50, 60, 580)
        item = Button.TextButton('Use Item', 20, (0, 200, 0), 200, 50, 280, 580)
        end = Button.TextButton('End Turn', 20, (0, 0, 255), 200, 50, 500, 580)
        mouse = Button.Button('none', 0, 0, 10, 10)
        menuSprites = pygame.sprite.Group()
        menuSprites.add(attack)
        menuSprites.add(item)
        menuSprites.add(end)
        menuSprites.draw(self.screen)
        pygame.display.flip()

        #Button click logic
        while True:
            for event in pygame.event.get():
                if pygame.MOUSEBUTTONDOWN == event.type:
                    pos = pygame.mouse.get_pos()
                    mouse.rect.x = pos[0]
                    mouse.rect.y = pos[1]

                    if pygame.sprite.collide_rect(mouse, attack):
                        return 'attack'

                    if pygame.sprite.collide_rect(mouse, item):
                        return 'item'

                    if pygame.sprite.collide_rect(mouse, end):
                        return 'end'

                elif pygame.QUIT == event.type:
                    pygame.quit()

    #Player turn
    def playerTurn (self):
        #Gets target
        i = self.getTarget()
        #If it is you player and it can move to square, move it there
        turn = self.movePlayer(i)
        #If you successfully moved to the square go to actions
        if turn:
            #actions
            while not i.moved:
                self.drawMap()
                #Show actions and get result
                choice = self.actionMenu()

                self.drawMap()
                #Attack someone if attack chosen
                if choice == 'attack':
                    #If attacking is successful, set their movability to false and stop combat music
                    if self.PlayerCombat(i):
                        i.moved = True
                        pygame.mixer.music.stop()

                #Bring up item menu if you have selected item
                elif choice == 'item':
                    item = self.useItem(i)
                    #If you have selected an item
                    if item:
                        #Bring up range for item use
                        self.validMove(i,'heal')
                        #select target
                        targ = self.getTarget()
                        #If you manage to select a target use item on the target if they are in range.
                        if targ:
                            if (abs(i.x - targ.x) + abs(i.y - targ.y)) <= 1:
                                message = i.use(targ, item)
                                if message:
                                    self.drawMap()
                                    #Draw message recieved from successful item usage
                                    t.text(self.screen, message, 60, 580, 20)
                                    time.sleep(1)
                                    #sets moved to true
                                    i.moved = True

                #if you selected end turn, set moved to true
                else:
                    i.moved = True

    #Menu for using an item
    def useItem (self, i):
        itemList = []
        buttons = []
        num = 0
        #Creates buttons based on what items the character has
        menuSprites = pygame.sprite.Group()
        mouse = Button.Button('none', 0, 0, 10, 10)
        for x in i.item:
            if i.item[x] > 0:
                itemList.append(x)
                buttons.append(Button.TextButton(x, 15, (0, 200, 0), 100, 50, 50 + (110 * math.floor(num/2)), 560 + (60*(num % 2))))
                menuSprites.add(buttons[-1])
                num += 1

        menuSprites.draw(self.screen)
        pygame.display.flip()

        #Sends back item name according to button pressed
        while True:
            for event in pygame.event.get():
                if pygame.MOUSEBUTTONDOWN == event.type:
                    pos = pygame.mouse.get_pos()
                    mouse.rect.x = pos[0]
                    mouse.rect.y = pos[1]

                    for b in range(len(buttons)):
                        if pygame.sprite.collide_rect(mouse, buttons[b]):
                            return itemList[b]

                    return False

                elif pygame.QUIT == event.type:
                    pygame.quit()


    def getTarget (self):
        #Checks if all players to see if the mouse is in them
        while True:
            for e in pygame.event.get():
                if pygame.MOUSEBUTTONDOWN == e.type:
                    for i in range(len(self.entities)):
                        mousePos = pygame.mouse.get_pos()
                        if (self.entities[i].x * (self.cSize/self.gSize)) <= mousePos[0] <= ((self.entities[i].x + 1)*(self.cSize/self.gSize)):
                            if (self.entities[i].y * (self.cSize/self.gSize)) <= mousePos[1] < ((self.entities[i].y + 1)*(self.cSize/self.gSize)):
                                    #If entity is clicked return the entity
                                    return self.entities[i]

                    #If no entity is clicked return false
                    return False

                if pygame.QUIT == e.type:
                    pygame.quit()

    #Shows squares you can do actions on
    def validMove (self, i, type):
        s = pygame.Surface((math.floor(self.cSize/self.gSize),math.floor(self.cSize/self.gSize)), pygame.SRCALPHA)
        if type == 'move':
            area = i.move
            s.fill((0,0,100,128))
        elif type == 'attack':
            area = i.range
            s.fill((100,0,0,128))
        elif type == 'heal':
            s.fill((0,100,0,128))
            area = 1

        for y in range((-1 * area),(area + 1)):
            for x in range((-1 * area),(area + 1)):
                if 0 < abs(x) + abs(y) <= area:
                    #adding transparent squares
                    movableSquare = True
                    if type == 'move':
                        if y + i.y >= 0 and x + i.x >= 0 and y + i.y < len(self.grid) and x + i.x < len(self.grid[0]):
                            #Uses path finder to see if you can move there
                            path = Pathfinder.astar(self.grid, (i.y,i.x), ((y + i.y),(x + i.x)))

                            if len(path) > (area + 1) or \
                               self.grid[y + i.y][x + i.x] == 1:
                                movableSquare = False

                            for e in self.entities:
                                if e.x == (x + i.x) and e.y == (y + i.y):
                                    movableSquare = False

                        else:
                            movableSquare = False

                    if movableSquare:
                        #Draws the squares
                        self.screen.blit(s, ((x + i.x) * (self.cSize/self.gSize), (y + i.y) * (self.cSize/self.gSize)))

                        pygame.display.flip()

    #Animation for moving an entity
    def moveEntity (self, i, endSquare):
        p = Pathfinder.astar(self.grid, (i.y,i.x), endSquare)
        self.drawMap()

        for a in p:
            if a[1] > i.x or a[1] < i.x:
                if a[1] > i.x:
                    c = 1
                    if i.flip:
                        i.img = pygame.transform.flip(i.img, True, False)
                        i.flip = False
                else:
                    c = -1
                    if not i.flip:
                        i.img = pygame.transform.flip(i.img, True, False)
                        i.flip = True

                #Slowly moves character image in the x directions
                for x in range((i.x*10), (a[1]*10) + c, c):
                    #Places grass behind to cover up tracks
                    img = pygame.image.load('Grass.jpg')
                    img = pygame.transform.scale(img, (math.floor(self.cSize/self.gSize), math.floor(self.cSize/self.gSize)))
                    self.screen.blit(img, (i.x * (self.cSize/self.gSize), i.y * (self.cSize/self.gSize)))
                    self.screen.blit(img, (a[1] * (self.cSize/self.gSize), a[0] * (self.cSize/self.gSize)))

                    #Places character image
                    img = i.img
                    img = pygame.transform.scale(img, (math.floor(self.cSize/self.gSize), math.floor(self.cSize/self.gSize)))
                    self.screen.blit(img, ((x/10) * (self.cSize/self.gSize), i.y * (self.cSize/self.gSize)))

                    pygame.display.flip()
                    time.sleep(0.01)


            if a[0] > i.y or a[0] < i.y:
                if a[0] > i.y:
                    c = 1
                else:
                    c = -1

                #Same as x for loop but moves in y direction
                for y in range((i.y*10), (a[0]*10) + c, c):
                    img = pygame.image.load('Grass.jpg')
                    img = pygame.transform.scale(img, (math.floor(self.cSize/self.gSize), math.floor(self.cSize/self.gSize)))
                    self.screen.blit(img, (i.x * (self.cSize/self.gSize), i.y * (self.cSize/self.gSize)))
                    self.screen.blit(img, (a[1] * (self.cSize/self.gSize), a[0] * (self.cSize/self.gSize)))

                    img = i.img
                    img = pygame.transform.scale(img, (math.floor(self.cSize/self.gSize), math.floor(self.cSize/self.gSize)))
                    self.screen.blit(img, (i.x * (self.cSize/self.gSize), (y/10) * (self.cSize/self.gSize)))

                    pygame.display.flip()
                    time.sleep(0.01)

            i.x = a[1]
            i.y = a[0]


    #Logic for moving own player
    def movePlayer (self, i):
        if i:
            #Shows stats of clicked entity
            self.validMove(i, 'move')
            t.text(self.screen, i.name, 80, 550, 30)
            t.text(self.screen, 'Hp: ' + str(i.hp), 90, 580, 20)
            t.text(self.screen, 'Atk: ' + str(i.atk), 90, 600, 20)
            t.text(self.screen, 'Def: ' + str(i.res), 90, 620, 20)
            t.text(self.screen, 'crit: ' + str(i.crit), 90, 640, 20)
            time.sleep(1)

            #If you clicked a playable character before, gives you ability to move it
            if i.player and not i.moved:
                while True:
                    for event in pygame.event.get():
                        if pygame.MOUSEBUTTONDOWN == event.type:
                            #When you click your mouse on a place, if you can move there, move your character there
                            nmousePos = pygame.mouse.get_pos()
                            nx = math.floor(nmousePos[0]/(self.cSize/self.gSize))
                            ny = math.floor(nmousePos[1]/(self.cSize/self.gSize))
                            if (abs(i.x - nx) + abs(i.y - ny)) <= i.move and self.grid[ny][nx] == 0:
                                if not(i.x == nx and i.y == ny):
                                    for pos in self.entities:
                                        if pos.x == nx and pos.y == ny:
                                            return False

                                #Animation for moving the character
                                self.moveEntity(i, (ny,nx))
                                return True

                            else:
                                #Return false to show that you didn't pick something that could move
                                return False

                        elif pygame.QUIT == event.type:
                            running = False
                            return False

        #Return false if you didn't chose a person to move
        return False

    #Animation to attack
    def attackAnim (self, i, e):
        if i.x > e.x:
            nx = i.x - 0.1
            if not i.flip:
                i.img = pygame.transform.flip(i.img, True, False)
                i.flip = True

        elif i.x < e.x:
            nx = i.x + 0.1
            #If its attacking to the right, flip image towards the right
            if i.flip:
                i.img = pygame.transform.flip(i.img, True, False)
                i.flip = False
        else:
            nx = i.x

        player = i.img
        #if i.__class__.__name__ == 'Archer':
        #    player = pygame.image.load(img[:-4] + 'Attack.png')
        player = pygame.transform.scale(player, (math.floor(self.cSize/self.gSize), math.floor(self.cSize/self.gSize)))

        if i.y > e.y:
            ny = i.y - 0.1
        elif i.y < e.y:
            ny = i.y + 0.1
        else:
            ny = i.y

        #Covers tracks
        img = pygame.image.load('Grass.jpg')
        img = pygame.transform.scale(img, (math.floor(self.cSize/self.gSize), math.floor(self.cSize/self.gSize)))
        self.screen.blit(img, (i.x * (self.cSize/self.gSize), i.y * (self.cSize/self.gSize)))

        #Moves character forward towards enemy slightly
        self.screen.blit(player, (nx * (self.cSize/self.gSize), ny * (self.cSize/self.gSize)))
        pygame.display.flip()
        time.sleep(0.05)

        #Makes enemy disappear for a short time
        img = pygame.image.load('Grass.jpg')
        img = pygame.transform.scale(img, (math.floor(self.cSize/self.gSize), math.floor(self.cSize/self.gSize)))
        self.screen.blit(img, (e.x * (self.cSize/self.gSize), e.y * (self.cSize/self.gSize)))
        pygame.display.flip()
        time.sleep(0.0001)

        #Reset map to original drawing
        self.drawMap()

    #Enemy Turn
    def enemyTurn (self):
        count = 0
        for e in self.entities:
            if not e.player:
                #Play enemy turn sound if no music is playing
                if not pygame.mixer.music.get_busy():
                    play.Sound('EnemyTurn.mp3', 1, -1)
                self.drawMap()
                #Shows valid spots for enemy
                self.validMove(e, 'move')
                time.sleep(0.8)
                self.drawMap()
                #If enemy has more than half hp or no vulnaries, attack
                if e.hp > (e.maxHp/2) or e.item['Vulnary'] <= 0:
                    #Moves enemy
                    self.enemyMove(e)
                    self.drawMap()
                    #Shows valid attacks spots for enemy
                    self.validMove(e, 'attack')
                    time.sleep(0.8)
                    #Enemy attack
                    self.EnemyAttack(e)
                else:
                    #Moves enemy
                    self.enemyMove(e, True)
                    self.drawMap()
                    #Show item validity
                    self.validMove(e, 'heal')
                    time.sleep(0.8)
                    #Use item and show its returned message
                    t.text(self.screen, e.use(e, 'Vulnary'), 60, 580, 20)
                    time.sleep(1)
                count += 1
        #Stop music after all enemy turns
        pygame.mixer.music.stop()

        #If no enemies left, show victory
        if count == 0:
            play.Sound('Victory.mp3', 1, -1)
            self.screen.fill((0,0,0))
            t.text(self.screen, 'YOU WIN', 200, 200, 50)
            t.text(self.screen, 'You have successfully completed Frontier Wars demo', 50, 400, 30)
            time.sleep(10)
            pygame.quit()

    #Enemy movement
    def enemyMove (self, e, low = False):
        if not low:
            closest = (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)

            #Finds a path to the closest player
            for i in self.entities:
                if i.player:
                    path = Pathfinder.astar(self.grid, (e.y, e.x), (i.y, i.x))
                    if  len(path) <= len(closest):
                        closest = path

            #Checks along its path for an empty spot which it can move to
            validPos = e.move
            while validPos > 0:
                if validPos > len(closest) - 1:
                    validPos -= 1
                    continue

                nx = closest[validPos][1]
                ny = closest[validPos][0]
                valid = True
                for x in self.entities:
                    if nx == x.x and ny == x.y:
                        valid = False
                        validPos -= 1

                if valid:
                    break

                validPos -= 1

            if validPos == len(closest) - 1:
                validPos -= 1

            #Moves it to new position if it has a new position to move to
            if closest != [] and closest != (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0) and validPos != 0:
                self.moveEntity(e, (ny,nx))

            else:
                movePos = (e.x, e.y, 500)
                for y in range((-1 * e.move),(e.move + 1)):
                    for x in range((-1 * e.move),(e.move + 1)):
                        if 0 < abs(x) + abs(y) <= e.move:
                            #adding transparent squares
                            movableSquare = True
                            if y + e.y >= 0 and x + e.x >= 0 and y + e.y < len(self.grid) and x + e.x < len(self.grid[0]):
                                #Uses path finder to see if you can move there
                                path = Pathfinder.astar(self.grid, (e.y,e.x), ((y + e.y),(x + e.x)))

                                if len(path) > (e.move + 1) or \
                                self.grid[y + e.y][x + e.x] == 1:
                                    movableSquare = False

                                for i in self.entities:
                                    if i.x == (x + e.x) and e.y == (y + e.y):
                                        movableSquare = False

                            else:
                                movableSquare = False

                            aAmount = 0
                            for i in self.entities:
                                if i.player:
                                    if abs((x + e.x) - i.x) <= i.range + i.move and abs((y + e.y) - i.y) <= i.range + i.move:
                                        aAmount += 1

                            if aAmount <= movePos[2]:
                                movePos = ((x + e.x), (y + e.y), aAmount)

                self.moveEntity(e, (movePos[1],movePos[0]))

        #Sets itself to moved
        e.moved = True

    #Enemy Attack logic
    def EnemyAttack (self, e):
        #Attacks first player in its range
        for i in self.entities:
            if i.player:
                if (abs(i.x - e.x) + abs(i.y - e.y)) <= e.range:
                    #Plays combat music
                    play.Sound('Attack.mp3', 0.8, -1)
                    #Draw translucent red square on player to attack
                    s = pygame.Surface((math.floor(self.cSize/self.gSize),math.floor(self.cSize/self.gSize)), pygame.SRCALPHA)
                    s.fill((100,0,0,128))
                    self.screen.blit(s, ((i.x) * (self.cSize/self.gSize), (i.y) * (self.cSize/self.gSize)))
                    pygame.display.flip()
                    time.sleep(0.8)

                    #Animates attack
                    self.attackAnim(e,i)

                    #Creates que for messages
                    textQue = []
                    result = e.attack(i)
                    #Adds to text que
                    textQue.append(e.name + ' has attacked ' + i.name)

                    if result[1] != '':
                        textQue.append(result[1])
                    if result[0][1] != '':
                        textQue.append(result[0][1])

                    #If person lived, you print damage and remaining hp for character out
                    if result[0][0] >= 0:
                        textQue.append(e.name + ' has attacked ' + i.name + ' for ' + str(result[0][0]) + ' damage. ' + i.name + ' has ' + str(i.hp) + 'hp left.')
                        #Print que out
                        t.text(self.screen, textQue, 80, 550, 20)

                        #If you are within range of your enemy, attack them back
                        if (abs(e.x - i.x) + abs(e.y - i.y)) <= i.range:
                            self.attackAnim(i,e)
                            #Reset text que
                            textQue = []
                            #The rest is the same as above but with switched roles
                            textQue.append(i.name + ' has attacked ' + e.name)
                            result = i.attack(e)

                            if result[1] != '':
                                textQue.append(result[1])
                            if result[0][1] != '':
                                textQue.append(result[0][1])

                            if result[0][0] >= 0:
                                textQue.append(i.name + ' has attacked ' + e.name + ' for ' + str(result[0][0]) + ' damage. ' + e.name + ' has ' + str(e.hp) + ' hp left.')
                                t.text(self.screen, textQue, 80, 550, 20)
                            else:
                                #Show kill message and rest of que and remove the dead character from list
                                textQue.append(i.name + ' has killed ' + e.name + '.')
                                t.text(self.screen, textQue, 80, 550, 20)
                                self.entities.remove(e)

                    else:
                        #Show kill message and remove the dead character from list
                        t.text(self.screen, e.name + ' has killed ' + i.name + '.', 80, 550, 20)
                        self.entities.remove(i)

                    time.sleep(1)
                    #Stop combat music
                    pygame.mixer.music.stop()
                    break

    #Player combat
    def PlayerCombat (self, i):
        self.validMove(i, 'attack')
        target = self.getTarget()
        #If you clicked a character and they are not a playe and within range, attack them.
        if target:
            if not target.player:
                if (abs(i.x - target.x) + abs(i.y - target.y)) <= i.range:
                    play.Sound('Attack.mp3', 0.8, -1)
                    self.attackAnim(i,target)
                    #The rest is same as enemy attack
                    result = i.attack(target)
                    textQue = []
                    textQue.append(i.name + ' has attacked ' + target.name)

                    if result[1] != '':
                        textQue.append(result[1])
                    if result[0][1] != '':
                        textQue.append(result[0][1])

                    if result[0][0] >= 0:
                        textQue.append(i.name + ' has attacked ' + target.name + ' for ' + str(result[0][0]) + ' damage. ' + target.name + ' has ' + str(target.hp) + ' hp left.')
                        t.text(self.screen, textQue, 80, 550, 20)
                        time.sleep(1)

                        if (abs(i.x - target.x) + abs(i.y - target.y)) <= target.range:
                            time.sleep(0.1)
                            self.attackAnim(target, i)
                            textQue = []
                            result = target.attack(i)
                            textQue.append(target.name + ' has attacked ' + i.name)

                            if result[1] != '':
                                textQue.append(result[1])
                            if result[0][1] != '':
                                textQue.append(result[0][1])

                            if result[0][0] >= 0:
                                textQue.append(target.name + ' has attacked ' + i.name + ' for ' + str(result[0][0]) + ' damage. ' + i.name + ' has ' + str(i.hp) + ' hp left.')
                                t.text(self.screen, textQue, 80, 550, 20)
                                time.sleep(1)
                                return True
                            else:
                                textQue.append(target.name + ' has killed ' + i.name + '.')
                                t.text(self.screen, textQue, 80, 550, 20)
                                self.entities.remove(i)
                                time.sleep(1)
                                return True

                        else:
                            return True

                    else:
                        t.text(self.screen, i.name + ' has killed ' + target.name + '.', 80, 550, 20)
                        self.entities.remove(target)
                        time.sleep(1)
                        return True

                else:
                    return False
            else:
                return False
        else:
            return False
