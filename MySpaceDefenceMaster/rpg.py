#!/usr/local/bin/python3
# This is the initailiser. It calls up the other files and is responsible for setting up the game.
"""
rpg.py - entry point for the RPG Game

Written by Bruce Fuda for Intermediate Programming
Python RPG Assignment 2015
Modified with permission by Edwin Griffin for
Intermediate Programming Object-Oriented Assignment 2018
"""
# this is probabaly for the sleep which causes the delays
import time
# imports the window created in gui for use
import gui
# imports character so we can use that class
import character
# imports battle so we can use that class
import battle
# imports map
import map
# imports random
import random
# imports math
import math

# Creates the window we play the game in.
app = gui.simpleapp_tk(None)
app.title('Alien Defense')

app.write('''
 _______  ___      ___   _______  __    _
|   _   ||   |    |   | |       ||  |  | |
|  |_|  ||   |    |   | |    ___||   |_| |
|       ||   |    |   | |   |___ |       |
|       ||   |___ |   | |    ___||  _    |
|   _   ||       ||   | |   |___ | | |   |
|__| |__||_______||___| |_______||_|  |__|
 ______   _______  _______  _______  __    _  _______  _______
|      | |       ||       ||       ||  |  | ||       ||       |
|  _    ||    ___||    ___||    ___||   |_| ||  _____||    ___|
| | |   ||   |___ |   |___ |   |___ |       || |_____ |   |___
| |_|   ||    ___||    ___||    ___||  _    ||_____  ||    ___|
|       ||   |___ |   |    |   |___ | | |   | _____| ||   |___
|______| |_______||___|    |_______||_|  |__||_______||_______|
''')
app.write("You can exit the game at any time by typing in 'quit'")
app.write("")


def set_mode():
    """ Select the game mode """
    # This is an error checking version of reading user input
    # Understanding try/except cases is important for
    # verifying user input. See class module on Exception Handling.
    while True:
        try:
            # Asks player to input 1 or 2 to choose human or alien.
            app.write("Please select a side:")
            app.write("1. Humans")
            app.write("2. Aliens")
            app.write("")
            # waits for input then assigns it to mode
            app.wait_variable(app.inputVariable)
            mode = app.inputVariable.get()

            # If the input is quit, close window
            if mode == 'quit':
                app.quit()

            mode = int(mode)
            # goes to except ValueError section and prints that if input not 1 or 2
            if mode not in range(1, 3):
                raise ValueError
            else:
                break

        except ValueError:
            app.write("You must enter a valid choice")
            app.write("")

    # Only gets to this point until you give a valid response. After that it returns the response.
    return mode

def set_race(mode):
    """ Set the player's race """
    # Checks mode for 1 or 2 to set race.
    if mode == 2:  # Alien Mode
        #Writes the group you are playing as.
        app.write("Playing as the Alien Invasion Forces.")
        app.write("")

        # race selection - evil
        while True:
            try:
                app.write("Please select your race:")
                app.write("1. Floater")
                app.write("2. Sectoid")
                app.write("3. Muton")
                app.write("4. Ethereal")
                app.write("5. Zerg")
                app.write("")
                app.wait_variable(app.inputVariable)
                # gets selections.
                race = app.inputVariable.get()

                # This quits
                if race == 'quit':
                    app.quit()

                race = int(race)
                # checks if race in values 1,2,3,4 or 5
                if race not in range(1, 6):
                    raise ValueError
                else:
                    break

            except ValueError:
                #If you do not enter an expected input, it prints this and makes you repeat selection.
                app.write("You must enter a valid choice")
                app.write("")

    else:  # Good Mode
        app.write("Playing as the Earth Defence Forces.")
        app.write("")

        # race selection - good. It works same way as the above race selection.
        while True:
            try:
                app.write("Please select your soldier type:")
                app.write("1. Assault Weapons")
                app.write("2. Heavy Weapons")
                app.write("3. Sniper")
                app.write("4. Support")
                app.write("5. Psionic")
                app.write("")
                app.wait_variable(app.inputVariable)
                race = app.inputVariable.get()

                if race == 'quit':
                    app.quit()
                race = int(race)

                if race not in range(1, 6):
                    raise ValueError
                else:
                    break

            except ValueError:
                app.write("You must enter a valid choice")
                app.write("")

    # returns race so that your player may be created.
    return race

def set_name():
    """ Set the player's name """
    while True:
        try:
            app.write("Please enter your Character Name:")
            app.write("")
            app.wait_variable(app.inputVariable)
            char_name = app.inputVariable.get()

            if char_name == 'quit':
                app.quit()

            # If you enter nothing. It sends you to the value error section.
            if char_name == '':
                raise ValueError
            else:
                break

        except ValueError:
            #It reminds you that your player must have a name which isn't blank and makes you re-enter a name.
            app.write("")
            app.write("Your name cannot be blank")

    #Returns the name you inputed
    return char_name


def create_player(mode, race, char_name):
    """ Create the player's character """
    # Checks the mode, race and char_name you would have created before. Also gives it the app it needs to write too.
    # Aliens
    #If the mode is 2 (Aliens), the function returns a class of the character you chose with the name you chose.
    if mode == 2:
        if race == 1:
            player = character.Floater(char_name, app, 1)
        elif race == 2:
            player = character.Sectoid(char_name, app, 1)
        elif race == 3:
            player = character.Muton(char_name, app, 1)
        elif race == 4:
            player = character.Ethereal(char_name, app, 1)
        else:
            player = character.Zerg(char_name, app, 1)
    # Humans
    else:
        if race == 1:
            player = character.Assault(char_name, app, 1)
        elif race == 2:
            player = character.Heavy(char_name, app, 1)
        elif race == 3:
            player = character.Sniper(char_name, app, 1)
        elif race == 4:
            player = character.Support(char_name, app, 1)
        else:
            player = character.Psionic(char_name, app, 1)

    # returns the new player
    return player


def set_difficulty():
    """ Set the difficulty of the game """
    while True:
        try:
            app.write("Please select a difficulty level:")
            app.write("e - Easy")
            app.write("m - Medium")
            app.write("h - Hard")
            app.write("l - Legendary")
            app.write("g - GODMODE")
            app.write("")
            app.wait_variable(app.inputVariable)
            difficulty = app.inputVariable.get()

            if difficulty == 'quit':
                app.quit()

            # if difficulty is not a valid option, repeat with an error message.
            if difficulty not in ['e', 'm', 'h', 'l', 'g'] or difficulty == '':
                raise ValueError
            else:
                break

        except ValueError:
            app.write("You must enter a valid choice")
            app.write("")

    # returns difficulty
    return difficulty


def create_enemies(mode, lvl):
    """ Create the enemies """
    #enList stores the enemies that will be returned by this function.
    enList = []
    while len(enList) < 4:
        if mode == 2:  # Alien Mode - good enemies
            # if you are alien, it checks your difficulty and picks an enemy from the enemies below.
            choice = [character.Support("Support_" + str(len(enList)), app, lvl), character.Heavy("Heavy_" + str(len(enList)), app, lvl),
                      character.Assault("Assault_" + str(len(enList)), app, lvl), character.Psionic("Psionic_" + str(len(enList)), app, lvl),
                      character.Sniper("Sniper_" + str(len(enList)), app, lvl)]

        else:  # Human Mode - evil enemies
            # if you are humans, it checks your difficulty and picks an enemy from the enemies below.
            choice = [character.Zerg("Zerg_" + str(len(enList)), app, lvl), character.Muton("Muton_" + str(len(enList)), app, lvl),
                      character.Floater("Floater_" + str(len(enList)), app, lvl), character.Ethereal("Ethereal_" + str(len(enList)), app, lvl),
                      character.Sectoid("Sectoid_" + str(len(enList)), app, lvl)]

        #Appends the picked enemy to the list of enemies, enList.
        enList.append(choice[math.floor(random.random() * len(choice))])

    # returns the enemies you will be fighting.
    return enList

#This function brings up a menu for player choices
def playerturn():
    #While the player hasn't entered a valid choice this loop goes on
    while True:
        app.write("---------------------------------------------")
        app.write('Pick which way to move (w,a,s,d) or open up your stats and inventory screen with i')

        #Waits for the input, then stores it to quit_choice
        app.wait_variable(app.inputVariable)
        quit_choice = app.inputVariable.get()

        #If quit_choice is quit, it quits game.
        if quit_choice == 'quit':
            app.quit()

        #Depending on what you enter the function returns something. If you enter something invalid, it displays and error and you must repeat.
        if quit_choice == 'w':
            return -1, 0

        elif quit_choice == 'a':
            return 0, -1

        elif quit_choice == 's':
            return 1, 0

        elif quit_choice == 'd':
            return 0, 1

        elif quit_choice == 'i':
            return 0, 0

        else:
            app.write('Choose a valid choice')

#This function is the menu for the store.
def store():
    #This loop goes on until you press 0 to break out of it.
    while True:
        try:
            app.write('----------------------------------')
            #Writes down your teams gold
            app.write('Gold: ' + str(player[0].gold))
            app.write('')

            #writes down what the shop sells and how much it costs
            app.write('1. Medikit (20 gold)')
            app.write('2. Adrenaline shot (20 gold)')
            app.write('3. Pheonix Down (60 gold)')
            app.write('4. Revive team member (60 gold)')

            #press 0 to go back
            app.write('0. Back')
            app.write('')
            app.wait_variable(app.inputVariable)

            #stores the id of the item you wish to buy
            item_choice = int(app.inputVariable.get())

            '''The below parts check which item you chose to get. It also checks if you have the gold for the item or the revival.
               Then it displays the players which you can give it to. If you picked to go back, you are broken out of the while loop'''
            if item_choice == 4 and player[0].gold >= 60:
                app.write('-------------------------------------')
                app.write('Which player do you want to give it to?')

                #Displays the players you can revive
                c = 1
                for x in player:
                    if x.health <= 0:
                        app.write(str(c) + ': ' + x.name)
                    c += 1

                app.write('0. Back')
                app.write('')

                #Stores the id of the player you wish to give the revival to
                player_choice = int(app.inputVariable.get()) - 1

                #If the person you chose doesn't exist, is alive or you chose to go back. Don't give the revival to anyone and return to shop screen.
                if player_choice in range(0,4):
                    if player[player_choice].health <= 0:
                        #Set the selected persons health back to their max health
                        player[player_choice].health = player[player_choice].maxhealth
                        #Subtract 60 gold from the players account
                        player[0].gold -= 60

            elif item_choice == 3 and player[0].gold >= 60:
                app.write('-------------------------------------')
                app.write('Which player do you want to give it to?')

                #Displays players you can give the item too
                c = 1
                for x in player:
                    app.write(str(c) + ': ' + x.name)
                    c += 1

                app.write('0. Back')
                app.write('')

                #Stores the id of the player they chose in player_choice
                app.wait_variable(app.inputVariable)
                player_choice = int(app.inputVariable.get()) - 1

                #Checks if the player you chose exists. If the condition isn't met, it returns to shop menu.
                if player_choice in range(0,4):
                    #give selected player selected item
                    player[player_choice].inv[2][1] += 1
                    #subtract gold from account
                    player[0].gold -= 60

            elif item_choice == 2 and player[0].gold >= 20:
                app.write('-------------------------------------')
                app.write('Which player do you want to give it to?')

                #Displays players you can give the item too
                c = 1
                for x in player:
                    app.write(str(c) + ': ' + x.name)
                    c += 1

                app.write('0. Back')
                app.write('')

                #Stores the id of the player they chose in player_choice
                app.wait_variable(app.inputVariable)
                player_choice = int(app.inputVariable.get()) - 1

                #Checks if the player you chose exists. If the condition isn't met, it returns to shop menu.
                if player_choice in range(0,4):
                    #give selected player selected item
                    player[player_choice].inv[1][1] += 1
                    #subtract gold from account
                    player[0].gold -= 20

            elif item_choice == 1 and player[0].gold >= 20:
                app.write('-------------------------------------')
                app.write('Which player do you want to give it to?')

                #Displays players you can give the item too
                c = 1
                for x in player:
                    app.write(str(c) + ': ' + x.name)
                    c += 1

                app.write('0. Back')
                app.write('')

                #Stores the id of the player they chose in player_choice
                app.wait_variable(app.inputVariable)
                player_choice = int(app.inputVariable.get()) - 1

                #Checks if the player you chose exists. If the condition isn't met, it returns to shop menu.
                if player_choice in range(0,4):
                    #give selected player selected item
                    player[player_choice].inv[0][1] += 1
                    #subtract gold from account
                    player[0].gold -= 20

            #if you chose back, break out of the shop loop, thus exiting this function.
            elif item_choice == 0:
                break

            #if you didn't chose a valid option, give an error message and go to shop menu, which is the start of this loop.
            else:
                app.write('Pick valid option')

        except ValueError:
            #If they don't put in only numbers a value error will be raised, thus activating this message.
            app.write('Please input numbers only')

'''def quit_game():
  """ Quits the game """
  while True:
    #This is not same as app.quit(). app.quit() is actual quit. This just ask if you want to quit and acts based on response.
    try:
      app.write("Play Again? (y/n)")
      app.write("")
      app.wait_variable(app.inputVariable)
      quit_choice = app.inputVariable.get()

      if quit_choice == 'quit':
        app.quit()

      #Choice must be y or n. Or you must repeat this over and over until you make response y or n.
      if quit_choice not in ['y','n'] or quit_choice == '':
        raise ValueError
      else:
        break

    except ValueError:
      app.write("You must enter a valid choice")
      app.write("")

  #returns your choice.
  return quit_choice '''

#This brings up the menu to give items
def moveItem():
    while True:
        try:
            #Displays all players and the numbers to select them
            app.write('Player who is giving item:')
            app.write('0. ' + player[0].name)
            app.write('1. ' + player[1].name)
            app.write('2. ' + player[2].name)
            app.write('3. ' + player[3].name)
            app.write('')

            #Stores the id of the player who is giving in the giver variable
            app.wait_variable(app.inputVariable)
            giver = int(app.inputVariable.get())

            #Displays all players and the numbers to select them
            app.write("---------------------------------------------")
            app.write('Player who is getting item:')
            app.write('0. ' + player[0].name)
            app.write('1. ' + player[1].name)
            app.write('2. ' + player[2].name)
            app.write('3. ' + player[3].name)
            app.write('')

            #Stores the id of the player who is getting the item in the variable getter
            app.wait_variable(app.inputVariable)
            getter = int(app.inputVariable.get())

            app.write("---------------------------------------------")
            app.write('Item you wish to give:')

            #Displays all the items that the giving player has
            j = 1
            for x in player[giver].inv:
                if x[1] > 0:
                    app.write(str(j) + '. ' + x[0] + ': ' + str(x[1]))
            app.write('0. Back')
            app.write('')

            #Stores the id of the item in the variable item
            app.wait_variable(app.inputVariable)
            item = int(app.inputVariable.get()) - 1

            #Checks if you have picked valid giving and getting players
            if giver in range(0,4) and getter in range(0,4):
                '''If the giving character has more than 0 of the item, then it subtracts 1 of the item away from said player
                and adds it to the inventory of the character who is getting it. If you chose back you are taken out of the
                move items function. If you don't pick a valid item, you must go through choosing again.'''
                if item == 0 and player[giver].inv[0][1] > 0:
                    player[giver].inv[0][1] -= 1
                    player[getter].inv[0][1] += 1
                elif item == 1 and player[giver].inv[1][1] > 0:
                    player[giver].inv[1][1] -= 1
                    player[getter].inv[1][1] += 1
                elif item == 2 and player[giver].inv[2][1] > 0:
                    player[giver].inv[2][1] -= 1
                    player[getter].inv[2][1] += 1
                elif item == -1:
                    break
                else:
                    app.write('Pick a valid item')
                    app.write('')
                    app.write("---------------------------------------------")

            #If you have not picked valid giving or getting characters, you get an error and must re-pick.
            else:
                app.write('Pick valid characters')
                app.write('')
                app.write("---------------------------------------------")

        except ValueError:
            #If you don't input a number, it gives this error and you must repeat.
            app.write('Please input numbers only')

#Menu for stats
def stats():
    while True:
        # stats screen

        #If you have had no battles yet, it doesn't display your battle stats
        try:
            if battles > 0:
                app.write("---------------------------------------------")
                app.write("No. Battles: {0}".format(str(battles)))
                app.write("No. Wins: {0}".format(wins))
                app.write("No. Kills: {0}".format(kills))
                app.write("Success Rate (%): {0:.2f}%".format(float(wins * 100 / battles)))
                app.write("Avg. kills per battle: {0:.2f}".format(float(kills) / battles))
                app.write("")
            app.write("---------------------------------------------")
            #Displays your party gold
            app.write('Gold: ' + str(player[0].gold))

            #Displays your party level which is always the level of the highest level member in your party.
            l = 0
            for p in player:
                if p.lvl > l:
                    l = p.lvl
            app.write('Party Level: ' + str(l))

            app.write("---------------------------------------------")
            app.write("")
            #Displays your players health and level
            app.write(player[0].name + ' ' + str(player[0].health) + 'hp, lvl: ' + str(player[0].lvl) + ' ' + \
                      player[1].name + ' ' + str(player[1].health) + 'hp, lvl: ' + str(player[1].lvl))
            app.write(player[2].name + ' ' + str(player[2].health) + 'hp, lvl: ' + str(player[2].lvl) + ' ' + \
                      player[3].name + ' ' + str(player[3].health) + 'hp, lvl: ' + str(player[3].lvl))
            app.write("")
            app.write('1. Inventory')
            app.write('0. Back')

            #Stores your choice on whether you want to back out of the stats screen or look at inventory.
            app.wait_variable(app.inputVariable)
            quit_choice = int(app.inputVariable.get())

            '''If you chose to go to the inventory, it takes you to the inventory.
               If you chose to go back, you break out of this menu.
               And if you chose an invalid response you go to start of this menu again with an error message.'''
            if int(quit_choice) == 1:
                inventoryMenu()
            elif int(quit_choice) == 0:
                break
            else:
                raise ValueError

        except ValueError:
            app.write("")
            app.write('Choose a valid choice')

def inventoryMenu():
    while True:
        try:
            # Shows the inventory that each character in your party has
            app.write(player[0].name + ': ')
            app.write('  Medikit: ' + str( + player[0].inv[0][1]))
            app.write('  Adrenaline Shots: ' + str(player[0].inv[1][1]))
            app.write('  Pheonix Down: ' + str(player[0].inv[2][1]))
            app.write("")
            app.write(player[1].name + ': ')
            app.write('  Medikit: ' + str( + player[1].inv[0][1]))
            app.write('  Adrenaline Shots: ' + str(player[1].inv[1][1]))
            app.write('  Pheonix Down: ' + str(player[1].inv[2][1]))
            app.write("")
            app.write(player[2].name + ': ')
            app.write('  Medikit: ' + str( + player[2].inv[0][1]))
            app.write('  Adrenaline Shots: ' + str(player[2].inv[1][1]))
            app.write('  Pheonix Down: ' + str(player[2].inv[2][1]))
            app.write("")
            app.write(player[3].name + ': ')
            app.write('  Medikit: ' + str( + player[3].inv[0][1]))
            app.write('  Adrenaline Shots: ' + str(player[3].inv[1][1]))
            app.write('  Pheonix Down: ' + str(player[3].inv[2][1]))

            app.write("")
            app.write('1. Move items')
            app.write('0. Back')

            #Stores your choice on whether to go back or move items in quit_choice
            app.wait_variable(app.inputVariable)
            quit_choice = app.inputVariable.get()

            #If you chose to move item. The move item function is activated.
            if int(quit_choice) == 1:
                #Move item takes you to the moving item menu. Once you back out of that menu, you come back to this one.
                moveItem()

            #If you chose back, you are broken out of this menu.
            elif int(quit_choice) == 0:
                break

        except ValueError:
            app.write("")
            app.write('Choose a valid choice')

# creates the battles, wins and kills
battles = 0
wins = 0
kills = 0

#Creates the list where your characters will be stored
player = []

# Asks for input on mode and returns mode to mode.
mode = set_mode()

#Does character creation 4 times because you are a party of 4
for i in range(4):
    # Asks for race and assigns returned race to race. It needs the mode to work.
    race = set_race(mode)

    # Sets char_name to your character name, which is what set_name will return.
    char_name = set_name()

    # Creates you character based upon the above variables and adds it to the player list.
    player.append(create_player(mode, race, char_name))

# Writes out the name and class for your party members.
app.write('Your party consists of ' + player[0].name + ' the ' + player[0].__class__.__name__ + ', '
          + player[1].name + ' the ' + player[1].__class__.__name__ + ', '
          + player[2].name + ' the ' + player[2].__class__.__name__ + ' and '
          + player[3].name + ' the ' + player[3].__class__.__name__)
app.write("")

# Sets difficulty
difficulty = set_difficulty()

while True:
    #Finds the level of the max leveled player in your party
    l = 0
    for p in player:
        if l < p.lvl:
            l = p.lvl

    #The amount of enemies on the map
    enNum = 8

    #Creates the world by calling map class from the map file. It uses the difficult, enNum and l variables.
    world = map.map(20, 90, 8, enNum, difficulty, l)

    #As long as all the enemies are alive, continue this loop.
    while enNum > 0:
        #Draw the map
        for y in world.update():
            app.write(' '.join(y))

        #Bring up the player options for movement or stats screen
        my, mx = playerturn()
        #If the player selected the stats screen on their turn, bring up the stats screen.
        if mx == my:
            stats()

        #Call the p_move map function with mx and my inputs
        pturn = world.p_move(my, mx)

        #If pturn is a string, this means that the players has encountered something when it moved.
        if type(pturn) == str:
            #pturn has enemy in it, you have encountered an enemy
            if 'enemy' in pturn:
                app.write('You have encountered an enemy.')
                #Takes the end part of pturn as the enemy level and puts it in enLvl
                enLvl = int(pturn[5:])
                # Creates enemies based on the mode you are in and the enemy level
                enemies = create_enemies(mode, enLvl)

                #Displays the enemies you are fighting
                app.write('You are fighting:')
                for x in enemies:
                    app.write(x.name + ' level ' + str(x.lvl))
                    app.write('')
                    time.sleep(1)

                ''' Creates the battle and gives that class the enemies and player info.
                    Also the app to display in. Also sets end var to true, to show that player starts'''
                encounter = battle.Battle(player, enemies, app, True)
                # Plays the battle. And at the end you get a win and the amount of kills you had.
                battle_wins, battle_kills, loss = encounter.play()
                # After a battle is finished, the kills and wins are added to your current kills and wins. You also get plus one to battle.
                battles += 1
                wins += battle_wins
                kills += battle_kills
                enNum -= 1
                #If you have lost, the game says you lose and quits you out.
                if loss:
                    app.write("You have failed. GG.")
                    app.write("")
                    time.sleep(1)
                    app.write("Thank you for playing Alien Defense.")
                    time.sleep(2)
                    app.quit()

                #Otherwise your characters healths are reset if they are alive, and it returns you to map.
                for p in player:
                    p.reset()

            #If pturn = shop then it invokes the shop menu.
            elif pturn == 'shop':
                store()
        else:
            #If pturn isn't a string, it must be either true or false

            #If pturn is true, that means you moved to an empty space
            if pturn:
                #Now it stores the results of enemy movements in engage.
                engage = world.enemyMove()
                #If engage is an int, that means that the enemy has hit a player and has returned its level.
                if type(engage) == int:
                    app.write('You have encountered an enemy.')
                    #enLvl is set to the enemy level
                    enLvl = engage
                    # Creates enemies based on the mode and enemy level
                    enemies = create_enemies(mode, enLvl)

                    #Displays enemies you are fighting
                    app.write('You are fighting:')
                    for x in enemies:
                        app.write('')
                        app.write(x.name + ' the ' + x.__class__.__name__ + ' level ' + str(x.lvl))
                        time.sleep(1)

                    ''' Creates the battle and gives that class the enemies and player info.
                        Also the app to display in. Also sets end var to False, to show that enemies start'''
                    encounter = battle.Battle(player, enemies, app, False)
                    # Plays the battle. And at the end you get a win and the amount of kills you had.
                    battle_wins, battle_kills, loss = encounter.play()
                    # After a battle is finished, the kills and wins are added to your current kills and wins. You also get plus one to battle.
                    battles += 1
                    wins += battle_wins
                    kills += battle_kills
                    enNum -= 1
                    if loss:
                        app.write("You have failed. GG.")
                        app.write("")
                        time.sleep(1)
                        app.write("Thank you for playing Alien Defense.")
                        time.sleep(2)
                        app.quit()

                    # Playing again - reset all enemies and players
                    for p in player:
                        p.reset()
