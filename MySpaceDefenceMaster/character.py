#!/usr/local/bin/python3
"""
rpg.py - entry point for the RPG Game

Written by Bruce Fuda for Intermediate Programming
Python RPG Assignment 2015
Modified with permission by Edwin Griffin for
Intermediate Programming Object-Oriented Assignment 2018
"""

# import required Python modules
import time
import random

######
# Define the attributes and methods available to all characters in the Character
# Superclass. All characters will be able to access these abilities.
# Note: All classes should inherit the 'object' class.
######


class Character:
    """ Defines the attributes and methods of the base Character class """

    def __init__(self, char_name, app, lvl):
        """ Parent constructor - called before child constructors """
        self.attack_mod = 1.0
        self.defense_mod = 1.0
        self.name = char_name
        self.shield = 0
        self.max_shield = 50
        self.app = app
        self.xp = 0
        self.lvl = lvl
        self.gold = 0
        self.inv = [['Medikit', 0], ['Adrenaline Shot', 0], ['Pheonix Down', 0]]
        self.taunt = False

    def __str__(self):
        """ string representation of character """
        return str("You are " + self.name + " the " + self.__class__.__name__)

    def move(self, player):
        """
        Defines any actions that will be attempted before individual
        character AI kicks in - applies to all children
        """
        move_complete = False
        # makes all Ai use medkit at less than 50 hp
        if self.health < 50 and self.inv[0][1] > 0:
            # also sets stance at defensive
            self.set_stance('d')
            self.use_medikit()
            move_complete = True
        return move_complete

#### Character Attacking Actions ####
    # Sets stance
    def set_stance(self, stance_choice):
        """ sets the fighting stance based on given parameter """

        # Is a percentage thing. E.g. attack is 30% better at cost of %40 defence in 'a' stance
        if stance_choice == "a":
            self.attack_mod = 1.3
            self.defense_mod = 0.6
            self.app.write(self.name + " chose aggressive stance.")

        elif stance_choice == "d":
            self.attack_mod = 0.6
            self.defense_mod = 1.2
            self.app.write(self.name + " chose defensive stance.")

        else:
            self.attack_mod = 1.0
            self.defense_mod = 1.0
            self.app.write(self.name + " chose balanced stance.")
        self.app.write("")

    def attack_enemy(self, target):
        ''' Attacks the targeted enemy. Accepts a Character object as the parameter (enemy
        to be targeted). Returns True if target killed, False if still alive.'''

        # Picks a number from 1 to 15 inclusive. This number is the base for the attack.
        roll = random.randint(0, 15)
        hit = int(roll * self.attack_mod * self.attack)
        self.app.write(self.name + " attacks " + target.name + ".")
        time.sleep(1)

        # Picks number from 1 to 100 inclusive. If the number is greater than 89. Hit damage is doubled.
        crit_roll = random.randint(1, 100)
        if crit_roll >= 90:
            hit = hit * 2
            self.app.write(
                self.name + " scores a critical hit! Double damage inflicted!!")
            time.sleep(1)

        #If the crit roll is less than 6, then it is a counter and the damage is inflicted to you.
        elif crit_roll < 6:
            self.app.write(target.name + " has countered the attack!!")
            #Remembers the old target
            old_t = target
            #Sets target to yourself
            target = self
            time.sleep(1)

        # Checks if target was killed or not.
        kill = target.defend_attack(hit)
        time.sleep(1)

        # If kill is true write that they have been killed.
        if kill:
            if self != target:
                self.app.write(self.name + " has killed " + target.name + ".")
                self.app.write("")
                time.sleep(1)
                return True

            #If you are the target
            else:
                #Write that the old targets name has killed you
                self.app.write(old_t.name + " has killed you.")
                self.app.write("")
                time.sleep(1)
                #Returns false so that this won't be counted as a kill.
                return False
        else:
            return False

    def defend_attack(self, att_damage):
        ''' Defends an attack from the enemy. Accepts the "hit" score of the attacking enemy as
        a parameter. Returns True is character dies, False if still alive.'''

        # defend roll
        roll = random.randint(1, 15)
        block = int(roll * self.defense_mod * self.defense)

        # Roll for dodge - must roll a 10 (10% chance)
        dodge_roll = random.randint(1, 20)
        if dodge_roll == 20:
            self.app.write(self.name + " successfully dodges the attack!")
            block = att_damage
            time.sleep(1)

        # Calculate damage from attack
        damage = att_damage - block
        if damage < 0:
            damage = 0

        # If character has a shield, shield is depleted, not health
        if self.shield > 0:
            # Shield absorbs all damage if shield is greater than damage
            if damage <= self.shield:
                self.app.write(self.name + "'s shield absorbs " +
                               str(damage) + " damage.")
                time.sleep(1)
                self.shield = self.shield - damage
                damage = 0
            # Otherwise some damage will be sustained and shield will be depleted
            elif damage != 0:
                self.app.write(self.name + "'s shield absorbs " +
                               str(self.shield) + " damage.")
                time.sleep(1)
                damage = damage - self.shield
                self.shield = 0

        # Reduce health
        self.app.write(self.name + " suffers " + str(damage) + " damage!")
        self.health = self.health - damage
        time.sleep(1)

        # Check to see if dead or not
        if self.health <= 0:
            self.health = 0
            self.app.write(self.name + " is dead!")
            self.app.write("")
            time.sleep(1)
            return True
        else:
            self.app.write(self.name + " has " +
                           str(self.health) + " hit points left")
            self.app.write("")
            time.sleep(1)
            return False

#### Character Ability Actions ####

    def valid_ability(self, choice):
        ''' Checks to see if the ability being used is a valid ability i.e. can be used by
        that race and the character has enough adrenaline '''

        valid = False

        # Determine this character's race
        # This is a built-in property we can use to work out the
        # class name of the object (i.e. their race)
        race = self.__class__.__name__

        # Only Ethereal or Psionic can use throw.
        if choice == 1:
            if race in ["Ethereal", "Psionic"] and self.adrenaline >= 10:
                valid = True
        # Only humans can use shield.
        elif choice == 2 and self.adrenaline >= 20 and race not in ["Zerg", "Ethereal", "Muton", "Floater", "Sectoid"]:
            valid = True
        # Only Zerg can use the two evolution moves.
        elif choice == 3 and self.adrenaline >= 20 and race in ["Zerg"]:
            valid = True
        elif choice == 4 and self.adrenaline >= 20 and race in ["Zerg"]:
            valid = True
        elif choice == 5 and self.adrenaline >= 20 and race in ["Support"]:
            valid = True
        elif choice == 6 and self.adrenaline >= 20 and race in ["Heavy"]:
            valid = True

        return valid

    def use_ability(self, choice, target=False):
        ''' Uses the ability chosen by the character. Requires 2 parameters - the ability
        being used and the target of the ability (if applicable). '''

        kill = False

        # Checks if you have selected a valid ability.
        if choice == 1:
            # uses throw on target.
            kill = self.throw(target)
        elif choice == 2:
            # Just uses the ability.
            self.engage_shield()
        elif choice == 3:
            self.buffAtack()
        elif choice == 4:
            self.buffDef()
        elif choice == 5:
            self.heal(target)
        elif choice == 6:
            self.tauntEn()
        else:
            self.app.write("Invalid ability choice. Ability failed!")
            self.app.write("")

        # returns whether ability was used or not.
        return kill

    # defines throw ability
    def throw(self, target):
        # Subtracts adrenaline by 10
        self.adrenaline -= 10
        self.app.write(self.name + " throws " +
                       target.name + " through the air!")
        time.sleep(1)

        # the damage on throw is defined by a characters mind and an int roll. The defense for the ability is based on the enemies resistance and an int roll.
        roll = random.randint(5, 15)
        defense_roll = random.randint(1, 10)
        damage = int(roll * self.mind) - int(defense_roll * target.resistance)
        if damage < 0:
            damage = 0

        # shield blocking out the damage of the throw.
        if target.shield > 0:
            if damage <= target.shield:
                self.app.write(
                    target.name + "'s shield absorbs " + str(damage) + " damage.")
                time.sleep(1)
                target.shield = target.shield - damage
                damage = 0
            elif damage != 0:
                self.app.write(target.name + "'s shield absorbs " +
                               str(target.shield) + " damage.")
                time.sleep(1)
                damage = damage - target.shield
                target.shield = 0

        self.app.write(target.name + " takes " + str(damage) + " damage.")
        self.app.write("")
        time.sleep(1)
        target.health = target.health - damage

        # Sends message is target is killed.
        if target.health <= 0:
            target.health = 0
            self.app.write(target.name + " is dead!")
            self.app.write("")
            time.sleep(1)
            return True

        # Otherwise it sends the usual "Target has X hitpoints left."
        else:
            self.app.write(target.name + " has " + str(target.health) + " hit points left")
            self.app.write("")
            time.sleep(1)
            return False

    def heal(self, target):
        # Subtracts adrenaline by 10
        self.adrenaline -= 20
        self.app.write(self.name + " heals " + target.name)
        time.sleep(1)

        # the heal on heal is defined by a characters mind and a random int roll inbetween 5 and 15.
        roll = random.randint(5, 15)
        healing = int(roll * self.mind)

        self.app.write(target.name + " heals for " + str(healing) + " health.")
        self.app.write("")
        time.sleep(1)
        target.health = target.health + healing

        #If the target is overhealed, they are just healed to their max hp.
        if target.health > target.max_health:
            target.health = target.max_health

        self.app.write(target.name + " now has " + str(target.health) + " hit points")
        self.app.write("")
        time.sleep(1)

    # Shield ability
    def engage_shield(self):
        # Subtracts adrenaline by 20
        self.adrenaline -= 20
        self.app.write(self.name + " engages a personal shield!")
        time.sleep(1)
        if self.shield <= self.max_shield:
            self.shield = self.max_shield
        self.app.write(self.name + " is shielded from the next " +
                       str(self.shield) + " damage.")
        self.app.write("")
        time.sleep(1)

    # Attack buff
    def buffAtack(self):
        # Subtract adrenaline by 20
        self.adrenaline -= 20
        # message to show the ability being used.
        self.app.write(self.name + " evolves and gains more strength!")
        time.sleep(1)
        # buffs attacks
        self.attack += 1
        self.app.write(self.name + " gets more damage for later turns.")
        self.app.write("")
        time.sleep(1)

    # Defense buff
    def buffDef(self):
        # Subtract adrenaline by 20
        self.adrenaline -= 20
        # message to show the ability being used.
        self.app.write(self.name + " evolves and gains stronger armor!")
        time.sleep(1)
        # buffs defense
        self.defense += 1
        self.app.write(self.name + " gets more defense for later turns.")
        self.app.write("")
        time.sleep(1)

    # A target disruption move
    def tauntEn(self):
        # Subtract adrenaline by 20
        self.adrenaline -= 20
        # message to show the ability being used.
        self.app.write(self.name + " taunts the enemy")
        time.sleep(1)
        self.app.write("Enemies will target " + self.name + " next turn.")
        self.app.write("")
        self.taunt = True
        time.sleep(1)

#### Character Item Actions ####

    # medkit logic
    def use_medikit(self):
        """
        Uses a medikit if the player has one. Returns True if has medikit,
        false if hasn't
        """
        # if character has medkit use it
        if self.inv[0][1] >= 1:
            self.inv[0][1] -= 1
            self.health += 250
            # stops hp from going over max hp.
            if self.health > self.max_health:
                self.health = self.max_health
            # message to show medkit being used
            self.app.write(self.name + " uses a medikit!")
            time.sleep(1)
            self.app.write(self.name + " has " +
                           str(self.health) + " hit points.")
            self.app.write("")
            time.sleep(1)
            return True
        else:
            # if you have no medkits, you cant use them.
            self.app.write("You have no medikits left!")
            self.app.write("")
            return False

    def use_adshot(self):
        """
        Uses an adrenaline shot if the player has one. Returns True if has medikit,
        false if hasn't
        """
        # if character has adrenaline shot use it
        if self.inv[1][1] >= 1:
            self.inv[1][1] -= 1
            self.adrenaline += 100
            # stops adrenaline from going over max adrenaline.
            if self.adrenaline > self.max_adrenaline:
                self.adrenaline = self.max_adrenaline
            # message to show adrenaline shot being used
            self.app.write(self.name + " uses an adrenaline shot!")
            time.sleep(1)
            self.app.write(self.name + " has " + str(self.adrenaline) + " adrenaline.")
            self.app.write("")
            time.sleep(1)
            return True
        else:
            # if you have no adrenaline shots, you cant use them.
            self.app.write("You have no adrenaline shots left!")
            self.app.write("")
            return False

    def use_pd(self, target):
        """
        Uses a pheonix down on the target if the player has one. Returns True if has pheonix down,
        false if hasn't
        """
        # if character has pheonix down use it
        if self.inv[2][1] >= 1:
            self.inv[2][1] -= 1
            target.health = target.max_health
            # message to show pheonix down being used
            self.app.write(self.name + " uses a pheonix down!")
            time.sleep(1)
            #Shows message that the player has revived the target.
            self.app.write(self.name + " has revived " + target.name + ".")
            self.app.write("")
            time.sleep(1)
            return True
        else:
            # if you have no pheonix down, you cant use them.
            self.app.write("You have no pheonix downs left!")
            self.app.write("")
            return False

#### Miscellaneous Character Actions ####

    def reset(self):
        ''' Resets the character to its initial state '''
        #if the character is dead, their health won't be reset
        dead = False
        if self.health <= 0:
            dead = True
        self.res()
        if dead:
            self.health = 0
        self.shield = 0

    def print_status(self):
        ''' Prints the current status of the character '''
        self.app.write(self.name + ' the ' +
                       self.__class__.__name__ + "'s Status:")
        time.sleep(0.5)

        health_bar = "Health: "
        health_bar += "|"
        i = 0
        while i <= self.max_health:
            if i <= self.health:
                health_bar += "#"
            else:
                health_bar += " "
            i += 25
        health_bar += "| " + str(self.health) + " hp (" + \
            str(int(self.health * 100 / self.max_health)) + "%)"
        self.app.write(health_bar)
        time.sleep(0.5)

        if self.max_adrenaline > 0:
            adrenaline_bar = "Adrenaline: "
            adrenaline_bar += "|"
            i = 0
            while i <= self.max_adrenaline:
                if i <= self.adrenaline:
                    adrenaline_bar += "*"
                else:
                    adrenaline_bar += " "
                i += 10
            adrenaline_bar += "| " + str(self.adrenaline) + " ap (" + str(
                int(self.adrenaline * 100 / self.max_adrenaline)) + "%)"
            self.app.write(adrenaline_bar)
            time.sleep(0.5)

        if self.shield > 0:
            shield_bar = "Shield: "
            shield_bar += "|"
            i = 0
            while i <= 100:
                if i <= self.shield:
                    shield_bar += "o"
                else:
                    shield_bar += " "
                i += 10
            shield_bar += "| " + \
                str(self.shield) + " sp (" + \
                str(int(self.shield * 100 / self.max_shield)) + "%)"
            self.app.write(shield_bar)
            time.sleep(0.5)

        self.app.write("Items")
        for x in self.inv:
            self.app.write(x[0] + ": " + str(x[1]))
        self.app.write("")
        time.sleep(0.5)

######
# Define the attributes specific to each of the Character Subclasses.
# This identifies the differences between each race.
######

# creates assault class.


class Assault(Character):
    '''Defines the attributes of an Assault Weapons Soldier in the game. Inherits the constructor and methods
    of the Character class. All the res functions define how it's' reset. '''
    # Constructor for Assault class

    def __init__(self, char_name, app, lvl):
        Character.__init__(self, char_name, app, lvl)
        self.res()
        self.inv[0][1] += 1

    def res(self):
        self.max_health = 250 + (self.lvl * 10)
        self.max_adrenaline = 40 + (self.lvl * 10)
        self.attack = 5 + self.lvl
        self.defense = 4 + self.lvl
        self.mind = 5
        self.resistance = 6 + int((self.lvl / 2) - 0.5)
        self.health = self.max_health
        self.adrenaline = self.max_adrenaline

    def move(self, player):
        """ Defines the AI for the Assault class """
        # Uses medkit if below 50hp
        move_complete = Character.move(self, player)

        # if you didn't use medkit, do whats below.
        if not move_complete:
            # if at 75% hp or more. Go attack stance.
            if self.health * 100 / self.max_health > 75:
                self.set_stance('a')

            # If at 30% hp or more. Set stance to balanced.
            elif self.health * 100 / self.max_health > 30:
                self.set_stance('b')

            # Or defence stance in any other situation
            else:
                self.set_stance('d')

            # If no shield and have enough adrenaline. Use shield ability.
            if self.shield == 0 and self.adrenaline >= 20:
                self.use_ability(2)
            # Otherwise just attack player.
            else:
                return self.attack_enemy(player)
        return False


class Heavy(Character):
    '''Defines the attributes of a Heavy Weapons Soldier in the game. Inherits the constructor and methods
    of the Character class '''

    # Constructor for Heavy class
    def __init__(self, char_name, app, lvl):
        Character.__init__(self, char_name, app, lvl)
        self.res()
        self.inv[0][1] += 1

    def res(self):
        self.max_health = 300 + (self.lvl * 10)
        self.max_adrenaline = 30 + (self.lvl * 10)
        self.attack = 3 + int((self.lvl / 2) - 0.5)
        self.defense = 7 + self.lvl
        self.mind = 2
        self.resistance = 3 + int((self.lvl / 2) - 0.5)
        self.health = self.max_health
        self.adrenaline = self.max_adrenaline

    def move(self, player):
        """ Defines the AI for the Heavy class """
        move_complete = Character.move(self, player)
        # Always go full agro for heavy. Attack everytime, attacking stance.
        if not move_complete:
            self.set_stance('d')
            return self.attack_enemy(player)
        return False


class Sniper(Character):
    '''Defines the attributes of a Sniper in the game. Inherits the constructor and methods
    of the Character class '''

    # Constructor for Sniper class
    def __init__(self, char_name, app, lvl):
        Character.__init__(self, char_name, app, lvl)
        self.res()
        self.inv[0][1] += 1

    def res(self):
        self.max_health = 150 + (self.lvl * 10)
        self.max_adrenaline = 60 + (self.lvl * 10)
        self.attack = 8 + self.lvl
        self.defense = 3 + int((self.lvl / 2) - 0.5)
        self.mind = 8
        self.resistance = 8 + self.lvl
        self.health = self.max_health
        self.adrenaline = self.max_adrenaline

    def move(self, player):
        """ Defines the AI for the Sniper class """
        move_complete = Character.move(self, player)
        if not move_complete:
            # Always be defensive. If you don't have shield and have adrenaline, shield yourself. If you don't shield, attack.
            self.set_stance('a')
            if self.shield == 0 and self.adrenaline >= 20:
                self.use_ability(2)
            else:
                return self.attack_enemy(player)
        return False


class Support(Character):
    '''Defines the attributes of a Support Soldier in the game. Inherits the constructor and methods
    of the Character class '''

    # Constructor for Support class
    def __init__(self, char_name, app, lvl):
        Character.__init__(self, char_name, app, lvl)
        self.res()
        self.inv[0][1] += 1
        self.inv[1][1] += 1

    def res(self):
        self.max_health = 150 + (self.lvl * 10)
        self.max_adrenaline = 60 + (self.lvl * 10)
        self.attack = 2 + int((self.lvl / 2) - 0.5)
        self.defense = 2 + int((self.lvl / 2) - 0.5)
        self.mind = 8
        self.resistance = 8 + self.lvl
        self.health = self.max_health
        self.adrenaline = self.max_adrenaline

    def move(self, player):
        """ Defines the AI for the Support class """
        move_complete = Character.move(self, player)
        if not move_complete:
            # always defensive
            self.set_stance('d')
            # Support soldiers shield if they don't have one
            if self.shield == 0 and self.adrenaline >= 20:
                self.use_ability(2)
            else:
                return self.attack_enemy(player)
        return False


class Floater(Character):
    '''Defines the attributes of a Floater in the game. Inherits the constructor and methods
    of the Character class '''

    # Constructor for Floater class
    def __init__(self, char_name, app, lvl):
        Character.__init__(self, char_name, app, lvl)
        self.res()
        self.inv[0][1] += 1

    def res(self):
        self.max_health = 200 + (self.lvl * 10)
        self.max_adrenaline = 40 + (self.lvl * 10)
        self.attack = 5 + self.lvl
        self.defense = 4 + self.lvl
        self.mind = 5
        self.resistance = 7 + int((self.lvl / 2) - 0.5)
        self.health = self.max_health
        self.adrenaline = self.max_adrenaline

    def move(self, player):
        """ Defines the AI for the Floater class """
        # Uses medkit if below 50hp
        move_complete = Character.move(self, player)

        # if you didn't use medkit, do whats below.
        if not move_complete:
            # if at 75% hp or more. Go attack stance.
            if self.health * 100 / self.max_health > 75:
                self.set_stance('a')

            # If at 30% hp or more. Set stance to balanced.
            elif self.health * 100 / self.max_health > 30:
                self.set_stance('b')

            # Or defence stance in any other situation
            else:
                self.set_stance('d')

            # Otherwise just attack player.
            return self.attack_enemy(player)
        return False


class Sectoid(Character):
    '''Defines the attributes of a Sectoid in the game. Inherits the constructor and methods
    of the Character class '''

    # Constructor for Sectoid class
    def __init__(self, char_name, app, lvl):
        Character.__init__(self, char_name, app, lvl)
        self.res()

    def res(self):
        self.max_health = 150 + (self.lvl * 10)
        self.max_adrenaline = 0 + (self.lvl * 10)
        self.attack = 6 + self.lvl
        self.defense = 5 + self.lvl
        self.mind = 2
        self.resistance = 3 + int((self.lvl / 2) - 0.5)
        self.health = self.max_health
        self.adrenaline = self.max_adrenaline

    def move(self, player):
        """ Defines the AI for the Sectoid class """
        move_complete = Character.move(self, player)
        if not move_complete:
            # Always balanced and attacking.
            self.set_stance('b')
            return self.attack_enemy(player)
        return False


class Muton(Character):
    '''Defines the attributes of a Muton in the game. Inherits the constructor and methods
    of the Character class '''

    # Constructor for Muton class
    def __init__(self, char_name, app, lvl):
        Character.__init__(self, char_name, app, lvl)
        self.res()
        self.inv[0][1] += 1

    def res(self):
        self.max_health = 175 + (self.lvl * 10)
        self.max_adrenaline = 20 + (self.lvl * 10)
        self.attack = 5 + self.lvl
        self.defense = 5 + self.lvl
        self.mind = 4
        self.resistance = 4 + self.lvl
        self.health = self.max_health
        self.adrenaline = self.max_adrenaline

    def move(self, player):
        """ Defines the AI for the Muton class """
        move_complete = Character.move(self, player)
        if not move_complete:
            # Always aggressively attacking.
            self.set_stance('b')
            return self.attack_enemy(player)
        return False


class Ethereal(Character):
    '''Defines the attributes of an Ethereal in the game. Inherits the constructor and methods
    of the Character class '''

    # Constructor for Ethereal class
    def __init__(self, char_name, app, lvl):
        Character.__init__(self, char_name, app, lvl)
        self.res()
        self.inv[1][1] += 1

    def res(self):
        self.max_health = 150 + (self.lvl * 10)
        self.max_adrenaline = 60 + (self.lvl * 10)
        self.attack = 2 + int((self.lvl / 2) - 0.5)
        self.defense = 4 + int((self.lvl / 2) - 0.5)
        self.mind = 8 + self.lvl
        self.resistance = 8 + self.lvl
        self.health = self.max_health
        self.adrenaline = self.max_adrenaline

    def move(self, player):
        """ Defines the AI for the Ethereal class """
        move_complete = Character.move(self, player)
        if not move_complete:
            # Always defensive
            self.set_stance('d')
            if self.adrenaline >= 10:
                # If adrenaline is greater than 10, use throw on the player.
                return self.use_ability(1, player)
            else:
                # Otherwise just attack.
                return self.attack_enemy(player)
        return False


class Psionic(Character):
    '''Defines the attributes of a Psionic Soldier in the game. Inherits the constructor and methods
    of the Character class '''

    # Constructor for Psionic class
    def __init__(self, char_name, app, lvl):
        Character.__init__(self, char_name, app, lvl)
        self.res()
        self.inv[0][1] += 1
        self.inv[1][1] += 1

    def res(self):
        self.max_health = 150 + (self.lvl * 10)
        self.max_adrenaline = 60 + (self.lvl * 10)
        self.attack = 2 + int((self.lvl / 2) - 0.5)
        self.defense = 2 + int((self.lvl / 2) - 0.5)
        self.mind = 8 + self.lvl
        self.resistance = 10 + int((self.lvl / 2) - 0.5)
        self.health = self.max_health
        self.adrenaline = self.max_adrenaline

    def move(self, player):
        """ Defines the AI for the Psionic class """
        move_complete = Character.move(self, player)
        if not move_complete:
            # Always defensive. If no shield, make yourself a shield if more than 20 adrenaline.
            self.set_stance('d')
            if self.shield == 0 and self.adrenaline >= 20:
                self.use_ability(2)
            # If no use shield and has over 10 adrenaline. Use throw on player.
            elif self.adrenaline >= 10:
                return self.use_ability(1, player)
            else:
                # Or just attack.
                return self.attack_enemy(player)
        return False


class Zerg(Character):
    '''Defines the attributes of a Zerg in the game. Inherits the constructor and methods
    of the Character class '''

    # Constructor for Zerg class
    def __init__(self, char_name, app, lvl):
        Character.__init__(self, char_name, app, lvl)
        self.res()
        self.inv[0][1] += 1

    def res(self):
        self.max_health = 125 + (self.lvl * 10)
        self.max_adrenaline = 100 + (self.lvl * 10)
        self.attack = 5 + int((self.lvl / 2) - 0.5)
        self.defense = 5 + int((self.lvl / 2) - 0.5)
        self.mind = 5
        self.resistance = 7 + self.lvl
        self.health = self.max_health
        self.adrenaline = self.max_adrenaline
        self.turn = 0

    def move(self, player):
        """ Defines the AI for the Zerg class """
        move_complete = Character.move(self, player)
        if not move_complete:
            # If health is less than 75 and you didn't use ability last turn. Also adrenaline is over 20. Buff defense and set stance defensive.
            if (self.health * 100 / self.max_health) < 50 and self.adrenaline >= 20 and self.turn == 0:
                self.set_stance('d')
                # Next turn will be a turn where you used ablity last turn.
                self.turn = 1
                return self.use_ability(4)
            # Otherwise if adrenaline not over 19 or you used ability last turn. Just go defensive and attack.
            elif (self.health * 100 / self.max_health) < 50:
                self.set_stance('d')
                # Next turn is turn where you didn't use ability last turn.
                self.turn = 0
                return self.attack_enemy(player)
            # If health is more than 100 and you didn't use ability last turn. Also adrenaline is over 20. Buff attack and set stance defensive.
            if (self.health * 100 / self.max_health) > 75 and self.adrenaline >= 20 and self.turn == 0:
                self.set_stance('d')
                self.turn = 1
                return self.use_ability(3)
            # Otherwise if adrenaline not over 19 or you used ability last turn. Just go aggressive and attack.
            elif (self.health * 100 / self.max_health) > 75:
                self.set_stance('a')
                self.turn = 1
                return self.attack_enemy(player)
            # If none of above applies. Go balanced and just go face(attack).
            self.set_stance('b')
            return self.attack_enemy(player)
        return False
