import random as r
import pygame

#Creates the character class which stores all the data for character
class Character():
    def __init__(self, name, lvl, atk, res, crit, hp, move, range, x, y, img, player = False):
        self.name = name
        self.atk = atk
        self.res = res
        self.crit = crit
        self.maxHp = hp
        self.hp = hp
        self.move = move
        self.range = range
        self.x = x
        self.y = y
        self.player = player
        self.moved = False
        self.img = pygame.image.load(img)
        self.lvl = lvl
        self.item = {'Vulnary': 1}
        self.flip = True

    #Attacking logic
    def attack(self, target):
        #Roll for damage
        damage = r.randint(1, 10) * self.atk
        #Roll for crit
        c = r.randint(1, 100)
        text = ''
        if c <= self.crit:
            text = self.name + ' has landed a critical strike.'
            damage = 2*damage

        #Returns end damage
        return target.defend(damage), text

    #Defending logic
    def defend(self, damage):
        #Defense roll
        damage = damage - r.randint(1, 8) * self.res
        #Dodge roll
        dodge = r.randint(1,50)
        text = ''
        if dodge == 10 or damage < 0:
            damage = 0
            text = self.name + ' has dodged the attack.'

        self.hp = self.hp - damage

        if self.hp > 0:
            return damage, text
        else:
            return -1, text

    #Item use
    def use (self, target, item):
        if item == 'Vulnary':
            if self.item['Vulnary'] > 0:
                self.item['Vulnary'] -= 1
                #Heal for 50hp
                target.hp += 50
                #If you heal above max health, set hp to max
                if target.hp > target.maxHp:
                    target.hp = target.maxHp
                return target.name + ' has healed up to ' + str(target.hp) + ' hp.'

        return False

#Presets for character
class Warrior(Character):
    def __init__(self, name, lvl, x, y, ally = False):
        if ally:
            Character.__init__(self,name,lvl,1 + lvl,3 + lvl,10,100 + (lvl*10),1,1,x,y,'Warrior.png',ally)
        else:
            Character.__init__(self,name,lvl,1 + lvl,3 + lvl,10,100 + (lvl*10),1,1,x,y,'EnWarrior.png',ally)

class Archer(Character):
    def __init__(self, name, lvl, x, y, ally = False):
        if ally:
            Character.__init__(self,name,lvl,3 + lvl,1 + lvl,10,50 + (lvl*10),2,2,x,y,'Warrior.png',ally)
        else:
            Character.__init__(self,name,lvl,3 + lvl,1 + lvl,10,50 + (lvl*10),2,2,x,y,'EnWarrior.png',ally)

class Berserker(Character):
    def __init__(self, name, lvl, x, y, ally = False):
        if ally:
            Character.__init__(self,name,lvl,3 + lvl,1 + lvl,50,50,2,1,x,y,'Warrior.png',ally)
        else:
            Character.__init__(self,name,lvl,3 + lvl,1 + lvl,50,50,2,1,x,y,'EnWarrior.png',ally)

class Cavalry(Character):
    def __init__(self, name, lvl, x, y, ally = False):
        if ally:
            Character.__init__(self,name,lvl,1 + lvl,2 + lvl,20,100 + (lvl*10),3,1,x,y,'Warrior.png',ally)
        else:
            Character.__init__(self,name,lvl,1 + lvl,2 + lvl,20,100 + (lvl*10),3,1,x,y,'EnWarrior.png',ally)
