import pygame
from color import *
import sprite as obj
from topLevelBar import *
from console import *
pygame.font.init()
size = [1260, 740]
pygame.display.set_mode(size)

#Menu, creates sprites and places them into a variable
menu_sprites_list = pygame.sprite.Group()
title = obj.ImageSprite(1010,400,125,0,'sprites/title.png')
b = obj.Button("Levels", 50, BLUE, 300, 150, 200, 450, (['levels', 'cursprites'], ['levels', 'fill']))
a = obj.Button("Help", 50, RED, 300, 150, 800, 450, (['help', 'cursprites'], ['help', 'fill']))
menu_sprites_list.add(title,a,b)

#Levels
levels_sprites_list = pygame.sprite.Group()
title = Title("Level Select", 400, 100, 0, 25, WHITE, BLUE, 50)
a = obj.Button("1", 50, (130, 255, 130), 100, 100, 125, 170, 1)
atitle = obj.Button("Using Move", 30, (180,180,100), 400, 100, 225, 170, 1)
b = obj.Button("2", 50, (130, 255, 130), 100, 100, 125, 320, 2)
btitle = obj.Button("Turning Your Bot", 30, (180,180,100), 400, 100, 225, 320, 2)
c = obj.Button("3", 50, (130, 255, 130), 100, 100, 125, 470, 3)
ctitle = obj.Button("Working With Loops", 30, (180,180,100), 400, 100, 225, 470, 3)
d = obj.Button("4", 50, (130, 255, 130), 100, 100, 675, 170, 4)
dtitle = obj.Button("Making Your Bot See", 30, (180,180,100), 400, 100, 775, 170, 4)
e = obj.Button("5", 50, (130, 255, 130), 100, 100, 675, 320, 5)
etitle = obj.Button("Making Decisions", 30, (180,180,100), 400, 100, 775, 320, 5)
f = obj.Button("6", 50, (130, 255, 130), 100, 100, 675, 470, 6)
ftitle = obj.Button("Using Variables", 30, (180,180,100), 400, 100, 775, 470, 6)
menu = obj.Button("Menu", 30, RED, 250, 80, 500, 620, (['menu', 'cursprites'], ['menu', 'fill']))
levels_sprites_list.add(title,a,atitle,b,btitle,c,ctitle,d,dtitle,e,etitle,f,ftitle,menu)

#Help
help_sprites_list = pygame.sprite.Group()
title = Title("Help Section", 400, 100, 0, 25, WHITE, (0,200,20), 50)
menu = obj.Button("Menu", 30, RED, 250, 80, 500, 620, (['menu', 'cursprites'], ['menu', 'fill']))
a = obj.Button("1", 50, (130, 130, 255), 100, 100, 125, 170, [['a', 'cursprites']])
atitle = obj.Button("Using the program", 30, (180,180,100), 400, 100, 225, 170, [['a', 'cursprites']])
b = obj.Button("2", 50, (130, 130, 255), 100, 100, 125, 320, [['b', 'cursprites']])
btitle = obj.Button("Programming syntax", 30, (180,180,100), 400, 100, 225, 320, [['b', 'cursprites']])
c = obj.Button("3", 50, (130, 130, 255), 100, 100, 125, 470, [['c', 'cursprites']])
ctitle = obj.Button("Basic movement commands", 30, (180,180,100), 400, 100, 225, 470, [['c', 'cursprites']])
d = obj.Button("4", 50, (130, 130, 255), 100, 100, 675, 170, [['d', 'cursprites']])
dtitle = obj.Button("Decisions and Loops", 30, (180,180,100), 400, 100, 775, 170, [['d', 'cursprites']])
e = obj.Button("5", 50, (130, 130, 255), 100, 100, 675, 320, [['e', 'cursprites']])
etitle = obj.Button("Operations and comparators", 30, (180,180,100), 400, 100, 775, 320, [['e', 'cursprites']])
f = obj.Button("6", 50, (130, 130, 255), 100, 100, 675, 470, [['f', 'cursprites']])
ftitle = obj.Button("Different object types", 30, (180,180,100), 400, 100, 775, 470, [['f', 'cursprites']])
help_sprites_list.add(title, menu, a, atitle, b, btitle, c, ctitle, d, dtitle, e, etitle, f, ftitle)

#Help specifics

#Using the program
a_sprites_list = pygame.sprite.Group()
title = Title("Using the program", 400, 100, 0, 25, WHITE, (200,200,20), 50)
a = obj.Button("1", 50, (255, 130, 130), 100, 100, 275, 170, [['a1', 'cursprites']])
atitle = obj.Button("Navigating the program", 30, (180,180,100), 600, 100, 375, 170, [['a1', 'cursprites']])
b = obj.Button("2", 50, (255, 130, 130), 100, 100, 275, 320, [['a2', 'cursprites']])
btitle = obj.Button("Scrolling text", 30, (180,180,100), 600, 100, 375, 320, [['a2', 'cursprites']])
c = obj.Button("3", 50, (255, 130, 130), 100, 100, 275, 470, [['a3', 'cursprites']])
ctitle = obj.Button("Using the text editor", 30, (180,180,100), 600, 100, 375, 470, [['a3', 'cursprites']])
menu = obj.Button("Help", 30, BLUE, 250, 80, 500, 620, (['help', 'cursprites'], ['help', 'fill']))
a_sprites_list.add(title, menu, a, atitle, b, btitle, c, ctitle)

#Navigating the program
a1_sprites_list = pygame.sprite.Group()
title = Title("Navigating the program", 500, 100, 0, 25, WHITE, (180,100,180), 50)
menu = obj.Button("Back", 30, (200,200,20), 250, 80, 500, 620, [['a', 'cursprites']])
tutorial = Help('Navigating the program\n\nTo navigate the program, you simply click on the buttons. The buttons take you to where they tell you they will take you. When you are on the level select screen the buttons take you to the levels.\n\n When you are in a level the top bar will help you navigate the levels. The arrows are the buttons. Pressing the close button on the window while in a level will take you to the level select screen. Otherwise it will exit the game.', 700, 400, 275, 170, False)
a1_sprites_list.add(title, menu, tutorial)

#Scrolling text
a2_sprites_list = pygame.sprite.Group()
title = Title("Scrolling text", 400, 100, 0, 25, WHITE, (180,100,180), 50)
menu = obj.Button("Back", 30, (200,200,20), 250, 80, 500, 620, [['a', 'cursprites']])
tutorial = Help('Scrolling text\n\nOften times the text in a box will be too large for the box. In this case you can scroll down to see the rest of the text(this doesn\'t apply to the text editor). In order to scroll you use the up and down arrows on the side of the box. If a box doesn\'t have this, you can\'t scroll it. You should keep scrolling till the lines don\'t move anymore as sometimes there could be hidden things. You can even try it on this box.\n1\n2\n\n3\n\n\n\n4\n\n\n\n\n\n\n\n8', 700, 400, 275, 170, False)
a2_sprites_list.add(title, menu, tutorial)

#Scrolling text
a3_sprites_list = pygame.sprite.Group()
title = Title("Using the text editor", 500, 100, 0, 25, WHITE, (180,100,180), 50)
menu = obj.Button("Back", 30, (200,200,20), 250, 80, 500, 620, [['a', 'cursprites']])
tutorial = Help('Using the text editor\n\nThe text editor is a box you can type in. You use it to write your code for the bot to follow. The text editor is a white box which has a run button on the bottom, you click this to test and run your code. To use the text editor, you click on it. You can tell that you have clicked on it when a line appears. This line is the text cursor. Once you see this text cursor you can start typing. In order to type, you simply type how you normally would. In order to move the text cursor, you use the left and right buttons on your keyboard. The up and down buttons don\'t work. You can also use the tab button to make 4 spaces. This is for people who like to indent code.', 700, 400, 275, 170, False)
a3_sprites_list.add(title, menu, tutorial)

#Programming Syntax
b_sprites_list = pygame.sprite.Group()
title = Title("Programming Syntax", 450, 100, 0, 25, WHITE, (200,200,20), 50)
tutorial = Help('Programming Syntax\n\nIn order to program you put one command after each other on new lines like this:\ncommand1\ncommand2\ncommand3\n\nAll commands are followed by brackets e.g. command1(). If the command requires information of some kind, it goes in the brackets e.g. command1(info). Finally come commands run other commands of your choosing. Using these looks like this:\ncommand1(info){\n   command2()\n  command3()\n}\n\nYou can also declare variables which store things. The syntax for that is a = ... The ... is stuff you put in there to store.', 700, 400, 275, 170, False)
menu = obj.Button("Help", 30, BLUE, 250, 80, 500, 620, (['help', 'cursprites'], ['help', 'fill']))
b_sprites_list.add(title, menu, tutorial)

#Basic movement commands
c_sprites_list = pygame.sprite.Group()
title = Title("Basic movement commands", 570, 100, 0, 25, WHITE, (200,200,20), 50)
a = obj.Button("1", 50, (255, 130, 130), 100, 100, 275, 170, [['c1', 'cursprites']])
atitle = obj.Button("Moving Forward", 30, (180,180,100), 600, 100, 375, 170, [['c1', 'cursprites']])
b = obj.Button("2", 50, (255, 130, 130), 100, 100, 275, 320, [['c2', 'cursprites']])
btitle = obj.Button("Turning Left", 30, (180,180,100), 600, 100, 375, 320, [['c2', 'cursprites']])
c = obj.Button("3", 50, (255, 130, 130), 100, 100, 275, 470, [['c3', 'cursprites']])
ctitle = obj.Button("Turning Right", 30, (180,180,100), 600, 100, 375, 470, [['c3', 'cursprites']])
menu = obj.Button("Help", 30, BLUE, 250, 80, 500, 620, (['help', 'cursprites'], ['help', 'fill']))
c_sprites_list.add(title, menu, a, atitle, b, btitle, c, ctitle)

#Moving Forward
c1_sprites_list = pygame.sprite.Group()
title = Title("Moving Forward", 400, 100, 0, 25, WHITE, (180,100,180), 50)
menu = obj.Button("Back", 30, (200,200,20), 250, 80, 500, 620, [['c', 'cursprites']])
tutorial = Help('Moving Forward\n\nTo move forward you use the move() command. Inside the brackets you put a number. The bot moves forward one tile in the direction it is facing.', 700, 400, 275, 170, False)
c1_sprites_list.add(title, menu, tutorial)

#Turning Left
c2_sprites_list = pygame.sprite.Group()
title = Title("Turning Left", 400, 100, 0, 25, WHITE, (180,100,180), 50)
menu = obj.Button("Back", 30, (200,200,20), 250, 80, 500, 620, [['c', 'cursprites']])
tutorial = Help('Turning Left\n\nTo turn the bot left you use the command left(). Inside the brackets you put the number of times it wants to turn left. The bot always turns 90 degrees.', 700, 400, 275, 170, False)
c2_sprites_list.add(title, menu, tutorial)

#Turning right
c3_sprites_list = pygame.sprite.Group()
title = Title("Turning Right", 400, 100, 0, 25, WHITE, (180,100,180), 50)
menu = obj.Button("Back", 30, (200,200,20), 250, 80, 500, 620, [['c', 'cursprites']])
tutorial = Help('Turning Right\n\nTo turn the bot right you use the command right(). Inside the brackets you put the number of times it wants to turn right. The bot always turns 90 degrees.', 700, 400, 275, 170, False)
c3_sprites_list.add(title, menu, tutorial)

#Decisions and looping
d_sprites_list = pygame.sprite.Group()
title = Title("Basic movement commands", 570, 100, 0, 25, WHITE, (200,200,20), 50)
a = obj.Button("1", 50, (255, 130, 130), 100, 100, 275, 170, [['d1', 'cursprites']])
atitle = obj.Button("Bot senses", 30, (180,180,100), 600, 100, 375, 170, [['d1', 'cursprites']])
b = obj.Button("2", 50, (255, 130, 130), 100, 100, 275, 320, [['d2', 'cursprites']])
btitle = obj.Button("Looping", 30, (180,180,100), 600, 100, 375, 320, [['d2', 'cursprites']])
c = obj.Button("3", 50, (255, 130, 130), 100, 100, 275, 470, [['d3', 'cursprites']])
ctitle = obj.Button("If statements", 30, (180,180,100), 600, 100, 375, 470, [['d3', 'cursprites']])
menu = obj.Button("Help", 30, BLUE, 250, 80, 500, 620, (['help', 'cursprites'], ['help', 'fill']))
d_sprites_list.add(title, menu, a, atitle, b, btitle, c, ctitle)

#Bot senses
d1_sprites_list = pygame.sprite.Group()
title = Title("Bot senses", 400, 100, 0, 25, WHITE, (180,100,180), 50)
menu = obj.Button("Back", 30, (200,200,20), 250, 80, 500, 620, [['d', 'cursprites']])
tutorial = Help('Bot senses\n\nYour bot can look at things in front of it. You can use see() to check if something is in front of you. \
Within the brackets of see() you can place a certain object keyword, which is a word(remember a word is in "" quotes), \
within the brackets. If the bot sees that object in front of it. It will return out True.The keywords for see() are:\n\
wall: looks for wall\n\
green: looks for green\n\
red: looks for red\n\
blue: looks for blue\n\
cyan: looks for cyan\n\
yellow: looks for yellow\n\
purple: looks for purple\n\
color: looks for any color', 700, 400, 275, 170, False)
d1_sprites_list.add(title, menu, tutorial)

#Looping
d2_sprites_list = pygame.sprite.Group()
title = Title("Looping", 400, 100, 0, 25, WHITE, (180,100,180), 50)
menu = obj.Button("Back", 30, (200,200,20), 250, 80, 500, 620, [['d', 'cursprites']])
tutorial = Help('Looping\n\nThe loop(){\} command can run the commands inside it multiple times. There are two ways you can use loop(){\}. The first way is to put a number in the brackets. \
The number in the brackets tells the robot how many times to run a set of instructions which are \
placed in the {\} brackets. An example for this is:\n\
loop(4){\n\
    move(1)\n\
    turnLeft(1)\n\
}\n\n The second way to use loop is to put an argument(An argument usually uses a comparator or a function. e.g. see(something) or  1 == 1) in the brackets. As long as the argument is true. The loop will run what is in it\'s {\} brackets', 700, 400, 275, 170, False)
d2_sprites_list.add(title, menu, tutorial)

#If statements
d3_sprites_list = pygame.sprite.Group()
title = Title("If statements", 500, 100, 0, 25, WHITE, (180,100,180), 50)
menu = obj.Button("Back", 30, (200,200,20), 250, 80, 500, 620, [['d', 'cursprites']])
tutorial = Help('If statements\n\nThe if(){\} command is a command that executes a piece of code in the {} brackets if the argument in the\
 () brackets is evaluated to true.', 700, 400, 275, 170, False)
d3_sprites_list.add(title, menu, tutorial)

#Decisions and looping
e_sprites_list = pygame.sprite.Group()
title = Title("Operations and comparators", 570, 100, 0, 25, WHITE, (200,200,20), 50)
a = obj.Button("1", 50, (255, 130, 130), 100, 100, 275, 170, [['e1', 'cursprites']])
atitle = obj.Button("Operators", 30, (180,180,100), 600, 100, 375, 170, [['e1', 'cursprites']])
b = obj.Button("2", 50, (255, 130, 130), 100, 100, 275, 420, [['e2', 'cursprites']])
btitle = obj.Button("Comparators", 30, (180,180,100), 600, 100, 375, 420, [['e2', 'cursprites']])
menu = obj.Button("Help", 30, BLUE, 250, 80, 500, 620, (['help', 'cursprites'], ['help', 'fill']))
e_sprites_list.add(title, menu, a, atitle, b, btitle)

#Operators
e1_sprites_list = pygame.sprite.Group()
title = Title("Operators", 400, 100, 0, 25, WHITE, (180,100,180), 50)
menu = obj.Button("Back", 30, (200,200,20), 250, 80, 500, 620, [['e', 'cursprites']])
tutorial = Help('Operators\n\nOperators modify numbers. Operators require two numbers to function. Here are the symbols(the symbol is usually in between a and b as it is operating on the two):\n\
a + b : this returns the two numbers added together, e.g. 1 + 1 outputs 2\n\
a - b : this returns a minus b e.g. 2 - 1 outputs 1\n\
a / b : this returns a divided by b e.g. 6/3 outputs 2\n\
a * b : this returns a multiplied by b e.g. 2*3 ouputs 6\n\
a ** b : this returns a to the power of b e.g. 2**2 outputs 4\n\
a % b : this returns a modulus b this outputs the remainder of a/b e.g. 9/2 outputs 1 because 9/2 is 4 remainder 1.', 700, 400, 275, 170, False)
e1_sprites_list.add(title, menu, tutorial)

#Comparators
e2_sprites_list = pygame.sprite.Group()
title = Title("Comparators", 400, 100, 0, 25, WHITE, (180,100,180), 50)
menu = obj.Button("Back", 30, (200,200,20), 250, 80, 500, 620, [['e', 'cursprites']])
tutorial = Help('Comparators\n\nComparators are symbols that compare two variables or other things. They often make up an argument as they give out a true or false response. Here are the symbols/words(the symbol is usually in between a and b as it is comparing the two):\n\
a == b : this returns true if a is equal to b like 1 == 1 or 2 == 2\n\
a != b : this returns true if a is not equal to b like 1 != 2 or 2 != 3\n\
a < b : this returns true if a is less than b, for words it looks at the length of the word\n\
a <= b : this is true if a is less than or equal to b\n\
a > b : is true if a is more than b\n\
a >= b : is true if a is more than or equal to b\n\
a in b : is true if a is in b. This cannot be used with numbers. It can only be used with words or lists i.e. "a" is in "ab"\n\
a not in b : is true if a is not in b i.e. "a" is not in "b"\n\
not a : this is not a comparative symbol/word. Instead it works to make a true statement false or a false statement true\
 i.e. not(2 > 1) is false or not a if a is false becomes true.', 700, 400, 275, 170, False)
e2_sprites_list.add(title, menu, tutorial)

#Different object types
f_sprites_list = pygame.sprite.Group()
title = Title("Different object types", 500, 100, 0, 25, WHITE, (200,200,20), 50)
a = obj.Button("1", 50, (255, 130, 130), 100, 100, 275, 170, [['f1', 'cursprites']])
atitle = obj.Button("Number", 30, (180,180,100), 600, 100, 375, 170, [['f1', 'cursprites']])
b = obj.Button("2", 50, (255, 130, 130), 100, 100, 275, 320, [['f2', 'cursprites']])
btitle = obj.Button("Word", 30, (180,180,100), 600, 100, 375, 320, [['f2', 'cursprites']])
c = obj.Button("3", 50, (255, 130, 130), 100, 100, 275, 470, [['f3', 'cursprites']])
ctitle = obj.Button("List", 30, (180,180,100), 600, 100, 375, 470, [['f3', 'cursprites']])
menu = obj.Button("Help", 30, BLUE, 250, 80, 500, 620, (['help', 'cursprites'], ['help', 'fill']))
f_sprites_list.add(title, menu, a, atitle, b, btitle, c, ctitle)

#Numbers
f1_sprites_list = pygame.sprite.Group()
title = Title("Number", 400, 100, 0, 25, WHITE, (180,100,180), 50)
menu = obj.Button("Back", 30, (200,200,20), 250, 80, 500, 620, [['f', 'cursprites']])
tutorial = Help('Number\n\nNumbers are like numbers in the real world. They can be modified with all the operators.', 700, 400, 275, 170, False)
f1_sprites_list.add(title, menu, tutorial)

#Word
f2_sprites_list = pygame.sprite.Group()
title = Title("Word", 400, 100, 0, 25, WHITE, (180,100,180), 50)
menu = obj.Button("Back", 30, (200,200,20), 250, 80, 500, 620, [['f', 'cursprites']])
tutorial = Help('Word\n\nWords are consisted of anything as long as they are in "" quotes. Words can use the + operator. This joins the second word on to the end of the first. It cannot use any other operator. Word can use any comparator that doesn\'t check greater or less than. Words can also use the size() function to figure out how long they are. Words can also be treated as lists although they can\'t use list commands.', 700, 400, 275, 170, False)
f2_sprites_list.add(title, menu, tutorial)

#List
f3_sprites_list = pygame.sprite.Group()
title = Title("List", 400, 100, 0, 25, WHITE, (180,100,180), 50)
menu = obj.Button("Back", 30, (200,200,20), 250, 80, 500, 620, [['f', 'cursprites']])
tutorial = Help('List\n\nList are consisted of multiple things as long as they are in [] brackets and are seperated by commas(,) e.g. [0,"hi",1,3,"534de"]. Lists can use the + operator. This joins the second list on to the end of the first. It cannot use any other operator. List can use any comparator that doesn\'t check greater or less than. Lists can also use the size() function to figure out how long they are. Lists can use the dot commands which are list commands. Dot commands take the syntax of list.command(). store() command stores what is in the brackets in to the list. remove() takes out whatever is in the index which you placed in the brackets. Then it shifts everything index greater than it to the left. Indexes are the location where the things are stored. [0,1,2,3,4,5,...] These are the indexes for things stored, first slot is 0, second is 1 and so on. You can segment a list byt putting [a:b] in front of it. The a is the start index of your segment and the b is the end index or your segment + 1. Not having any a assumes that you want your segment to start from the start. Not having any b assumes the segment goes to the end. You can also see what is stored in a specific index of a list by doing list[index].', 700, 400, 275, 170, False)
f3_sprites_list.add(title, menu, tutorial)

#Holds the sprite templates, so you can interchange them
scenes = {
    'levels':{'cursprites':levels_sprites_list, 'fill':(150,150,100)},
    'help':{'cursprites':help_sprites_list, 'fill':(150,150,100)},
    'menu': {'cursprites':menu_sprites_list, 'fill':(150,150,100)},
    'a': {'cursprites':a_sprites_list},
    'a1':{'cursprites':a1_sprites_list},
    'a2':{'cursprites':a2_sprites_list},
    'a3':{'cursprites':a3_sprites_list},
    'b':{'cursprites':b_sprites_list},
    'c': {'cursprites':c_sprites_list},
    'c1':{'cursprites':c1_sprites_list},
    'c2':{'cursprites':c2_sprites_list},
    'c3':{'cursprites':c3_sprites_list},
    'd': {'cursprites':d_sprites_list},
    'd1':{'cursprites':d1_sprites_list},
    'd2':{'cursprites':d2_sprites_list},
    'd3':{'cursprites':d3_sprites_list},
    'e': {'cursprites':e_sprites_list},
    'e1':{'cursprites':e1_sprites_list},
    'e2':{'cursprites':e2_sprites_list},
    'f': {'cursprites':f_sprites_list},
    'f1':{'cursprites':f1_sprites_list},
    'f2':{'cursprites':f2_sprites_list},
    'f3':{'cursprites':f3_sprites_list},
}