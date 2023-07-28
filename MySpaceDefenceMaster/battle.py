#!/usr/local/bin/python3
"""
rpg.py - entry point for the RPG Game

Written by Bruce Fuda for Intermediate Programming
Python RPG Assignment 2015
Modified with permission by Edwin Griffin for
Intermediate Programming Object-Oriented Assignment 2018
"""

# import modules
import sys
import time
import math
import random

class Battle:
    # Creates the battle
    def __init__(self, player, enemies, app, start):
        """
        Instantiates a battle object between the players and enemies specified,
        sending output to the given gui instance
        """
        self.player = player
        self.enemies = enemies
        self.app = app
        self.turn = 1
        self.wins = 0
        self.kills = 0
        self.player_won = False
        self.player_lost = False
        self.player_flee = False
        self.start = start

    def play(self):
        """
        Begins and controls the battle
        returns tuple of (win [1 or 0], no. kills)
        """
        # While no one has won or lost. Continue loop.
        while not self.player_won and not self.player_lost and not self.player_flee:
            # Writes turn that you are on.
            self.app.write("Turn " + str(self.turn))
            self.app.write("")
            time.sleep(1)

            #If you are starting, go first. Otherwise enemy goes first
            if not self.start:
                #Do enemy turn
                self.do_enemy_actions()

            # This is where the bulk of the battle takes place
            for i in range(len(self.player)):
                #Gets rid of a players taunt
                if self.player[i].taunt:
                    self.player[i].taunt = False

                #If player is alive, you can go through with their turn.
                if self.player[i].health > 0:
                    self.do_player_actions(i)

            if self.start:
                #Do enemy turn
                self.do_enemy_actions()

            # advance turn counter
            self.turn += 1

        # returns if won or not. Also returns kills. Only activates once above loop is over.
        return (self.wins, self.kills, self.player_lost)

    def get_action(self, num):
        """ Gets the player's chosen action for their turn """
        while True:
            try:
                self.app.write(
                    self.player[num].name + ' the ' + self.player[num].__class__.__name__ + "'s Turn:")
                self.app.write("1. Attack Enemies")
                self.app.write("2. Use Abilities")
                self.app.write("3. Use Item")
                self.app.write("4. Flee")
                self.app.write("")
                self.app.wait_variable(self.app.inputVariable)
                player_action = self.app.inputVariable.get()

                if player_action == 'quit':
                    self.app.quit()

                # Checks if player action is within range 1 to 4 inclusive.
                player_action = int(player_action)
                if player_action not in range(1, 5):
                    raise ValueError
                else:
                    break

            except ValueError:
                self.app.write("You must enter a valid choice")
                self.app.write("")

        return player_action

    def select_ability(self, num):
        """ Selects the ability the player would like to use """

        # sets player race to the class name the character belongs to.
        player_race = self.player[num].__class__.__name__

        while True:
            try:
                self.app.write("Select your ability:")
                # Writes the abilities to the screen. Only writes them there if it is useable by the race and you have enough adrenaline.
                if player_race in ["Ethereal", "Psionic"] and self.player[num].adrenaline >= 10:
                    self.app.write("1. Throw (10 ap)")
                if self.player[num].adrenaline >= 20 and player_race not in ["Zerg", "Muton", "Floater", "Sectoid", "Ethereal"]:
                    self.app.write("2. Shield (20 ap)")
                if self.player[num].adrenaline >= 20 and player_race in ["Zerg"]:
                    self.app.write("3. Evolve Strength (20 ap)")
                if self.player[num].adrenaline >= 20 and player_race in ["Zerg"]:
                    self.app.write("4. Evolve Defense (20 ap)")
                if self.player[num].adrenaline >= 20 and player_race in ["Support"]:
                    self.app.write("5. Heal (20 ap)")
                if self.player[num].adrenaline >= 20 and player_race in ["Heavy"]:
                    self.app.write("6. Taunt (20 ap)")
                self.app.write("0. Cancel Spell")
                self.app.write("")
                self.app.wait_variable(self.app.inputVariable)
                ability_choice = self.app.inputVariable.get()

                if ability_choice == 'quit':
                    self.app.quit()
                ability_choice = int(ability_choice)
                # checks if you have picked cancel spell.
                if ability_choice == 0:
                    return False
                # Checks if the ability the player has selected, is valid to use by the player. Otherwise it repeats.
                valid_ability = self.player[num].valid_ability(ability_choice)
                if not valid_ability:
                    raise ValueError
                else:
                    break

            except ValueError:
                self.app.write("You must enter a valid choice")
                self.app.write("")

        return ability_choice

    def choose_target(self, ally=False):
        """ Selects the target of the player's action """
        while True:
            try:
                self.app.write("Choose your target:")
                # use j to give a number option
                j = 0

                #If ally is not true, it selects through enemies.
                if not ally:
                    t = False
                    while j < len(self.enemies):
                        # If enemy is alive print it.
                        if self.enemies[j].health > 0:
                            self.app.write(str(j) + ". " + self.enemies[j].name + ' ' + str(self.enemies[j].health) + 'hp')
                        if self.enemies[j].taunt:
                            t = j
                        j += 1
                    self.app.write("")
                    self.app.wait_variable(self.app.inputVariable)
                    target = self.app.inputVariable.get()

                    if target == 'quit':
                        self.app.quit()

                    target = int(target)
                    if t and self.enemies[t].health > 0:
                        self.app.write("Too bad, " + self.enemies[t].name + " has taunted. You will attack them this turn.")
                        target = t
                    # checks if you picked an enemy, and that enemy has greater hp than 0.
                    if not (target < len(self.enemies) and target >= 0) or self.enemies[target].health <= 0:
                        raise ValueError
                    else:
                        break

                #If ally is 'revive', it selects through dead allies.
                elif ally == 'revive':
                    while j < len(self.player):
                        # If character is dead print it.
                        if self.player[j].health <= 0:
                            self.app.write(str(j + 1) + ". " + self.player[j].name + ' the ' + self.player[j].__class__.__name__)
                        j += 1
                    self.app.write("0. Cancel")
                    self.app.write("")
                    self.app.wait_variable(self.app.inputVariable)
                    target = self.app.inputVariable.get()

                    if target == 'quit':
                        self.app.quit()

                    target = int(target) - 1
                    if target == -1:
                        break

                    # checks if you picked a character, and that character has hp less than or equal 0.
                    if not (target < len(self.player) and target >= 0) or self.player[target].health > 0:
                        raise ValueError
                    else:
                        break

                #If ally is true
                else:
                    while j < len(self.player):
                        # If character is alive print it.
                        if self.player[j].health > 0 and self.player[j].health < self.player[j].max_health:
                            self.app.write(str(j + 1) + ". " + self.player[j].name + ' the ' + self.player[j].__class__.__name__ + ': ' + str(self.player[j].health))
                        j += 1
                    self.app.write("0. Cancel")
                    self.app.write("")
                    self.app.wait_variable(self.app.inputVariable)
                    target = self.app.inputVariable.get()

                    if target == 'quit':
                        self.app.quit()

                    target = int(target) - 1
                    if target == -1:
                        break

                    # checks if you picked an ally and that the ally has greater hp than 0 and doesn't have full hp.
                    if not (target < len(self.player) and target >= 0) or self.player[target].health <= 0 or self.player[target].health == self.player[target].max_health:
                        raise ValueError
                    else:
                        break

            except ValueError:
                self.app.write("You must enter a valid choice")
                self.app.write("")

        # returns the target identity number.
        return target

    #The use item menu
    def use_Item(self, num):
        while True:
            try:
                #Displays the player you are playing's items
                self.app.write(self.player[num].name + ' the ' + self.player[num].__class__.__name__ + "'s items:")
                self.app.write("1. Medikit: " + str(self.player[num].inv[0][1]))
                self.app.write("2. Adrenaline Shot: " + str(self.player[num].inv[1][1]))
                self.app.write("3. Pheonix Down: " + str(self.player[num].inv[2][1]))
                self.app.write("0. Cancel")
                self.app.write("")
                self.app.wait_variable(self.app.inputVariable)
                player_action = self.app.inputVariable.get()

                if player_action == 'quit':
                    self.app.quit()

                # Checks if player action is within range 1 to 4. Not including 4.
                player_action = int(player_action)
                if player_action not in range(0, 4):
                    raise ValueError
                else:
                    break

            except ValueError:
                self.app.write("You must enter a valid choice")
                self.app.write("")

        #Returns your choice
        return player_action

    def choose_stance(self):
        while True:
            try:
                # Writes stance options.
                self.app.write("Choose your stance:")
                self.app.write("a - Aggressive")
                self.app.write("d - Defensive")
                self.app.write("b - Balanced")
                self.app.write("")
                self.app.wait_variable(self.app.inputVariable)
                stance_choice = self.app.inputVariable.get()

                if stance_choice == 'quit':
                    self.app.quit()

                # Checks if you chose a, d or b.
                if stance_choice not in ['a', 'd', 'b'] or stance_choice == '':
                    raise ValueError
                else:
                    break

            except ValueError:
                self.app.write("You must enter a valid choice")
                self.app.write("")

        # returns your stance letter.
        return stance_choice

    def do_player_actions(self, num):
        """ Performs the player's actions """

        turn_over = False
        self.app.write('----------------------------------------------------')
        # If player has not won or the turn isn't over. Continue the loop.
        while not self.player_won and not turn_over and not self.player_flee:
            # Getting rid of taunting
            self.player[num].taunt = False
            # prints hp, shields, adrenaline and medkits remaining for the player.
            self.player[num].print_status()
            # brings up the stance choice menu which allows you to choose your stance.
            stance_choice = self.choose_stance()
            # Uses output of stance choice to set stance.
            self.player[num].set_stance(stance_choice)

            # Brings up the action menu and gets players choice.
            player_action = self.get_action(num)

            has_attacked = False

            if player_action == 4:
                has_attacked = True
                #If the player chose to flee, you have a 1/10 chance to flee.
                fleeChance = random.randint(0,10)
                if fleeChance == 10:
                    self.player_flee = True
                else:
                    self.app.write('You have failed to flee')

            # If the action is 3
            elif player_action == 3:
                # Player uses item
                has_attacked = True
                #Calls the use item menu
                c = self.use_Item(num)
                if c == 1:
                    #Player tries to use the medkit
                    has_attacked = self.player[num].use_medikit()
                elif c == 2:
                    #Player tries to use an adrenaline shot
                    has_attacked = self.player[num].use_adshot()
                elif c == 3:
                    #targ calls chose target with its ally variable equaling revive
                    targ = self.choose_target('revive')
                    '''If player didn't chose a target then, the character didn't do an action.
                       Otherwise the player tries to use a pheonix down'''
                    if targ != -1:
                        has_attacked = self.player[num].use_pd(targ)
                    else:
                        has_attacked = False
                else:
                    #If player chose not to use an item, you haven't done an action.
                    has_attacked = False

            elif player_action == 2:
                # brings up the menu to select the ability and stores the return in ability_choice.
                ability_choice = self.select_ability(num)

                # If the ability choice is not 0, use an ability.
                if ability_choice != 0:
                    has_attacked = True
                    # If the choice is 1. You will choose a target first.
                    if ability_choice == 1:
                        target = self.choose_target()
                        # If the ability kills the enemy. You get one more kill and xp and gold.
                        if self.player[num].use_ability(ability_choice, self.enemies[target]):
                            #Gain gold and xp
                            self.player[0].gold += 10
                            if math.ceil(self.enemies[target].lvl / 2) == 0:
                                self.app.write('You get 1 xp and 10 gold.')
                            else:
                                self.app.write('You get ' + str(math.ceil(self.enemies[target].lvl / 2)) + ' xp and 10 gold.')
                            for p in self.player:
                                #Dead players get no xp
                                if p.health > 0:
                                    #xp gained is based on enemy level
                                    p.xp += math.ceil(self.enemies[target].lvl / 2)
                                    #If their level is 0, they give 1 xp
                                    if math.ceil(self.enemies[target].lvl / 2) == 0:
                                        p.xp += 1
                                    #If you have double the xp of your current level, you level up and you xp is subtracted.
                                    while p.xp >= 2 * p.lvl:
                                        p.xp -= 2 * p.lvl
                                        p.lvl += 1
                                        p.res()
                                        self.app.write(p.name + ' has leveled up! ' + p.name + ' is now level ' + str(p.lvl))

                            #Your kills are increased by 1
                            self.kills += 1
                    elif ability_choice == 5:
                        #The ability is heal, so you choose a target with ally set to true.
                        target = self.choose_target(True)

                        #If you chose a target, use heal on that target
                        if target != -1:
                            self.player[num].use_ability(ability_choice, self.player[target])
                        else:
                        #Otherwise you didn't do an action
                            has_attacked = False
                    else:
                        self.player[num].use_ability(ability_choice)

            else:
                # If you tried no other action, just attack.

                #Choose target
                target = self.choose_target()
                has_attacked = True

                #If you killed the target
                if self.player[num].attack_enemy(self.enemies[target]):
                    #Gain gold and xp
                    self.player[0].gold += 10
                    if math.ceil(self.enemies[target].lvl / 2) == 0:
                        self.app.write('You get 1 xp and 10 gold.')
                    else:
                        self.app.write('You get ' + str(math.ceil(self.enemies[target].lvl / 2)) + ' xp and 10 gold.')
                    for p in self.player:
                        #Dead players get no xp
                        if p.health > 0:
                            #xp gained is based on enemy level
                            p.xp += math.ceil(self.enemies[target].lvl / 2)
                            #If their level is 0, they give 1 xp
                            if math.ceil(self.enemies[target].lvl / 2) == 0:
                                p.xp += 1
                            #If you have double the xp of your current level, you level up and you xp is subtracted.
                            while p.xp >= 2 * p.lvl:
                                p.xp -= 2 * p.lvl
                                p.lvl += 1
                                p.res()
                                self.app.write(p.name + ' has leveled up! ' + p.name + ' is now level ' + str(p.lvl))

                    #Your kills are increased by 1
                    self.kills += 1

            turn_over = True
            # If you haven't done something. Your turn is not over.
            if not has_attacked:
                turn_over = False
            else:
                # Checks if you have won or not.
                self.player_won = True
                for enemy in self.enemies:
                    if enemy.health > 0:
                        self.player_won = False
                        break

                if self.player_won == True:
                    # prints a victory message.
                    self.app.write("Your enemies hath been vanquished!!")
                    self.app.write("")
                    time.sleep(1)
                    #Gain additional xp and gold
                    self.player[0].gold += 10
                    for p in self.player:
                        p.xp += 1
                        while p.xp >= 2 * p.lvl:
                            p.xp -= 2 * p.lvl
                            p.lvl += 1
                            p.res()
                    self.app.write("You get some bonus xp and 10 additional gold!!")
                    self.app.write("")
                    time.sleep(1)
                    # Sets wins up by one.
                    self.wins += 1

    def do_enemy_actions(self):
        """ Performs the enemies' actions """

        #Checks if player has lost or not.
        turn_over = False
        self.player_lost = True
        for x in self.player:
            if x.health > 0:
                self.player_lost = False
                break

        # If player has not won, it is enemies turn.
        if not self.player_won and self.player_lost == False and not self.player_flee:
            self.app.write("Enemies' Turn:")
            self.app.write("")
            time.sleep(1)

            # Cycles through the enemies so that they can do a move.
            for enemy in self.enemies:
                enemy.taunt = False;
                # Can only act if its alive and can only act if the player hasn't lost.
                if enemy.health > 0 and not self.player_lost:

                    #Finds the player with the least health
                    h = 50000
                    t = 0
                    for i in range(len(self.player)):
                        #If a characters health is lower than the stored health in h
                        if self.player[i].health < h and self.player[i].health > 0:
                            #t the target id, becomes the characters id
                            t = i
                            #h becomes the characters hp
                            h = self.player[i].health

                        #If the character is taunting and alive
                        if self.player[i].taunt and self.player[i].health > 0:
                            #The target becomes the id of the the taunting character and we break out of the for loop.
                            t = i
                            break

                    #en_heal checks if the enemy has used heal or taunt
                    en_heal = False

                    #If the enemy is a support and has over 20 adrenaline
                    if enemy.__class__.__name__ == 'Support' and enemy.adrenaline > 20:
                        #Check if its fellow enemies have less than 50hp, but more than 0hp.
                        for i in self.enemies:
                            if (i.health < 50 or i.health < (i.max_health/2)) and i.health > 0:
                                #If they are less than 50 but more than 0 hp, use heal on them.
                                enemy.use_ability(5, i)
                                #Make en_heal true
                                en_heal = True
                                #Break out because you have healed
                                break

                    if enemy.__class__.__name__ == 'Heavy' and enemy.adrenaline > 20:
                        en_heal = True

                        #Check if its fellow enemies have taunt.
                        for i in self.enemies:
                            if enemy.taunt:
                                #If a fellow enemy has taunt. The enemy will not taunt
                                en_heal = False
                                break

                        if en_heal:
                            enemy.use_ability(6)

                    #If you haven't used heal or taunt, do your usual ai action.
                    if not en_heal:
                        enemy.move(self.player[t])

                    #Checks if player has lost
                    self.player_lost = True
                    for x in self.player:
                        if x.health > 0:
                            self.player_lost = False
                            break

            # If the player has lost. Write a losing message.
            if self.player_lost == True:
                self.app.write("You have been killed by your enemies.")
                self.app.write("")
                time.sleep(1)

        #If you have fled write a message
        elif self.player_flee == True:
            self.app.write("You have run from your enemies.")
            self.app.write("")
            time.sleep(1)
