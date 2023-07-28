import pygame
from color import *
import sprite as obj

#Colors
r = 'r'
b = 'b'
g = 'g'
c = 'c'
y = 'y'
p = 'p'

#Level layouts, the list in list is the layout, the number at the end is the orientation.
lvl_1 =([[1,1,1,1,1,1,1,1,1],
         [1,1,1,1,1,1,1,1,1],
         [1,1,1,1,3,1,1,1,1],
         [1,1,1,1,0,1,1,1,1],
         [1,1,1,1,0,1,1,1,1],
         [1,1,1,1,0,1,1,1,1],
         [1,1,1,1,2,1,1,1,1],
         [1,1,1,1,1,1,1,1,1]], 
         0,
         {'v':['move','turnLeft','turnRight','loop','see','if'], 'l':20},

         #Validation Levels
         ([[1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1],
           [1,1,3,1,1,1,1,1,1],
           [1,1,0,1,1,1,1,1,1],
           [1,1,0,1,1,1,1,1,1],
           [1,1,0,1,1,1,1,1,1],
           [1,1,2,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1]],

          [[1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,3,1,1,1],
           [1,1,1,1,1,0,1,1,1],
           [1,1,1,1,1,0,1,1,1],
           [1,1,1,1,1,0,1,1,1],
           [1,1,1,1,1,2,1,1,1],
           [1,1,1,1,1,1,1,1,1]]),
           'Complete this level using the move function'
        )

lvl_2 =([[1,1,1,1,1,1,1,1,1],
         [1,1,1,1,1,1,1,1,1],
         [1,1,1,3,1,1,1,1,1],
         [1,1,1,0,1,1,1,1,1],
         [1,1,1,0,0,1,1,1,1],
         [1,1,1,1,0,1,1,1,1],
         [1,1,1,1,2,1,1,1,1],
         [1,1,1,1,1,1,1,1,1]], 
         0,
         {'v':['move','turnLeft','turnRight','loop','see','if'], 'l':20},

         #Validation Levels
         ([[1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1],
           [1,3,1,1,1,1,1,1,1],
           [1,0,1,1,1,1,1,1,1],
           [1,0,0,1,1,1,1,1,1],
           [1,1,0,1,1,1,1,1,1],
           [1,1,2,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1]],

          [[1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1],
           [1,1,1,1,3,1,1,1,1],
           [1,1,1,1,0,1,1,1,1],
           [1,1,1,1,0,0,1,1,1],
           [1,1,1,1,1,0,1,1,1],
           [1,1,1,1,1,2,1,1,1],
           [1,1,1,1,1,1,1,1,1]]),
           'Complete this level with turnLeft and turnRight'
        )

lvl_3 =([[2,0,1,1,1,1,1,1,1],
         [1,0,0,1,1,1,1,1,1],
         [1,1,0,0,1,1,1,1,1],
         [1,1,1,0,0,1,1,1,1],
         [1,1,1,1,0,0,1,1,1],
         [1,1,1,1,1,0,0,1,1],
         [1,1,1,1,1,1,0,0,1],
         [1,1,1,1,1,1,1,3,1]], 
         1,
         {'v':['move','turnLeft','turnRight','loop','see','if'], 'l':6},

         #Validation Levels
         ([[1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1],
           [1,1,2,0,1,1,1,1,1],
           [1,1,1,0,0,1,1,1,1],
           [1,1,2,1,3,1,1,1,1],
           [1,1,1,1,1,1,1,1,1]],

          [[1,1,1,1,1,1,1,1,1],
           [1,1,2,0,1,1,1,1,1],
           [1,1,1,0,3,1,1,1,1],
           [1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1]]),
           'Complete this level using loops'
        )

lvl_4 =([[1,1,1,1,1,1,1,1,1],
         [1,1,1,3,0,1,1,1,1],
         [1,1,1,1,0,1,1,1,1],
         [1,1,1,1,0,1,1,1,1],
         [1,1,1,1,0,1,1,1,1],
         [1,1,1,1,0,1,1,1,1],
         [1,1,1,1,2,1,1,1,1],
         [1,1,1,1,1,1,1,1,1]], 
         0,
         {'v':['move','turnLeft','turnRight','loop','see','if'], 'l':10},

         #Validation Levels
         ([[1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1],
           [1,3,0,1,1,1,1,1,1],
           [1,1,0,1,1,1,1,1,1],
           [1,1,2,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1]],

          [[1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1],
           [1,1,1,1,3,0,1,1,1],
           [1,1,1,1,1,0,1,1,1],
           [1,1,1,1,1,0,1,1,1],
           [1,1,1,1,1,2,1,1,1],
           [1,1,1,1,1,1,1,1,1]]),

           'Complete this level using the see function.'
        )

lvl_5 =([[1,1,1,1,1,1,1,1,1],
         [1,1,1,1,1,1,1,1,1],
         [1,1,1,1,1,1,1,1,1],
         [1,1,1,1,1,1,1,1,1],
         [1,1,1,1,1,1,1,1,1],
         [1,1,1,3,r,1,1,1,1],
         [1,1,1,1,2,1,1,1,1],
         [1,1,1,1,1,1,1,1,1]], 
         0,
         {'v':['move','turnLeft','turnRight','loop','see','if'], 'l':10},

         #Validation Levels
         ([[1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1],
           [1,1,3,1,1,1,1,1,1],
           [1,1,g,1,1,1,1,1,1],
           [1,1,2,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1]],

          [[1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,b,3,1,1],
           [1,1,1,1,1,2,1,1,1],
           [1,1,1,1,1,1,1,1,1]]),

           'Make a decision on which direction to turn. Red is left, blue is right.'
        )

lvl_6 =([[1,1,1,1,r,1,1,1,1],
         [1,1,1,3,0,1,1,1,1],
         [1,1,1,1,0,1,1,1,1],
         [1,1,0,0,0,1,1,1,1],
         [1,1,1,1,0,1,1,1,1],
         [1,0,0,0,0,1,1,1,1],
         [1,1,1,1,2,1,1,1,1],
         [1,1,1,1,1,1,1,1,1]], 
         0,
         {'v':['move','turnLeft','turnRight','loop','see','if'], 'l':10},

         #Validation Levels
         ([[1,1,1,1,1,1,1,1,1],
           [1,1,0,0,0,1,1,1,1],
           [1,1,1,1,r,1,1,1,1],
           [1,1,0,0,0,0,0,3,1],
           [1,1,1,1,0,1,1,1,1],
           [1,1,0,0,0,0,0,1,1],
           [1,1,1,1,2,1,1,1,1],
           [1,1,1,1,1,1,1,1,1]],

          [[1,1,1,1,1,1,1,1,1],
           [1,1,1,0,0,1,1,1,1],
           [1,1,1,0,0,1,1,1,1],
           [1,0,0,0,0,1,1,1,1],
           [1,1,1,1,r,1,1,1,1],
           [1,3,0,0,0,1,1,1,1],
           [1,1,1,1,2,1,1,1,1],
           [1,1,1,1,1,1,1,1,1]]),

           'Find a way to complete this level when the amount of steps you make is the amount of times you need to turn left when you see red. The goal might not be in front of you when you turn.'
        )

#Help texts for each level
text_1 = '\nWelcome to the game. (note: If you are very new to coding, I strongly suggest looking at the help area. The help bits in the level assume you have some understanding of syntax.)\n\
The first command for you to learn is move(). \n\
To use move you type the command move() and place a number in the brackets.\
The number in the brackets tells the robot how many steps to move. An important thing to remember \
is that the move command moves the bot in the direction it is facing.'

text_2 = '\nThe second and third command to learn is turnLeft and turnRight\n\
To use turnLeft you type the command turnLeft() and place a number in the brackets. \
The number in the brackets tells the robot how many times to turn left. This is a way to \
move your bot in different directions. turnRight is the same as turnLeft but it turns the bot left instead of right.'

text_3 = '\nThe fourth command to learn is loop\n\
There are two ways you can use loop(){\}. The first way is to put a number in the brackets. \
The number in the brackets tells the robot how many times to run a set of instructions which are \
placed in the {\} brackets. An example for this is:\n\
loop(4){\n\
    move(1)\n\
    turnLeft(1)\n\
}\n\
This makes the bot move forward and turn left four times. You will be taught the second part later.'

text_4 = '\nThe fourth command to learn is see.\n\
Your bot can look at things in front of it. You can use see() to check if something is in front of you. \
Within the brackets of see() you can place a certain object keyword, which is a word(remember a word is in "" quotes), \
within the brackets. If the bot sees that object in front of it. It will return out True. You could use this in conjunction \
with a loop to make a loop go on till a bot sees something or while a bot sees something. e.g.\n\
loop(not see("wall")){\n\
    ...\n\
}\n\
The above loop runs until you see a wall. This is also the second way to use a loop. The loop will run while the argument in the \
brackets is true.\n\
The keywords for see() are:\n\
wall: looks for wall\n\
green: looks for green\n\
red: looks for red\n\
blue: looks for blue\n\
cyan: looks for cyan\n\
yellow: looks for yellow\n\
purple: looks for purple\n\
color: looks for any color'

text_5 = '\nThe fifth command you will learn is the if command.\n\
The if(){\} command is a command that executes a piece of code in the {} brackets if the statements in the\
 () brackets is evaluated to true. A true statement is something like 1 < 2 or 1 + 1 == 2. Certain commands can also\
 give out a true or false response like the see command. There are a few important symbols/words you need to remember with\
 evaluations. These symbols/words are used to compare things and return true or false depending on the comparison. These\
 symbols can be used in if brackets or loop brackets to govern how they would run.\
\nHere are the symbols/words(the symbol is usually in between a and b as it is comparing the two):\n\
a == b : this returns true if a is equal to b like 1 == 1 or 2 == 2\n\
a != b : this returns true if a is not equal to b like 1 != 2 or 2 != 3\n\
a < b : this returns true if a is less than b, for words it looks at the length of the word\n\
a <= b : this is true if a is less than or equal to b\n\
a > b : is true if a is more than b\n\
a >= b : is true if a is more than or equal to b\n\
a in b : is true if a is in b. This cannot be used with numbers. It can only be used with words or lists i.e. "a" is in "ab"\n\
a not in b : is true if a is not in b i.e. "a" is not in "b"\n\
not a : this is not a comparative symbol/word. Instead it works to make a true statement false or a false statement true\
 i.e. not(2 > 1) is false or not a if a is false becomes true.'

text_6 = '\n This time you will be using a variable\n\
A variable is a storage space. In it you can store any number(1,2,3), word("abc") or a list, which you will learn later.\n\
 You can create a variable with an = sign. To do this you say that some variable name(varname) is equal(=) to some value(val)\
 like this:\n\
varname = val, e.g.\n\
a = 1,\n\
b = "hello"\n\
You can also use variables to create other variable or to change themselves. e.g.\n\
a = 1, b = a, thus making b = 1\n\
a = 1, a = a + 1, thus making a = 2.\n\
While changing, using or creating variables, and operators can be used. However we will go into operators later.'