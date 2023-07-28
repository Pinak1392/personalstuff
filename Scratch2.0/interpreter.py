import inspect
import re
import time
import pygame

pygame.init()
pygame.font.init()

#FOR THE ERROR CHECKING PARTS OF THE CODE, CHECK OUT MY BLOG. BECAUSE I DONT WANT TO GO THROUGH AND COMMENT EVERY SINGLE ONE.

#Has a class for the interpreter
class control:
    def __init__(self, bot, code, button, valids, var={}):
        #Gets bot, code and initialises a command/variable dictionary
        self.bot = bot
        self.code = code
        self.button = button
        self.legal = valids['v']
        self.line = 1
        self.lineLimit = valids['l']
        self.commandDict = {
            'move':self.move,
            'turnLeft':self.turnLeft,
            'turnRight':self.turnRight,
            'say':self.say,
            'string':self.string,
            'number':self.integer,
            'if':self._if,
            'loop':self._loop,
            'inp':self.inp,
            'store':self.store,
            'remove':self.remove,
            'size':self.size,
            'delay':self.delay,
            'see':self.see,
            'isNumber':self.intCheck,
            'isString':self.strCheck,
            'isList':self.listCheck
        }
        self.commandDict.update(var)

    #Used to get params out of brackets, i.e. "hello,", 2, ",you" = ["hello,",2,",you"]
    def getParams(self, text):
        #The returned list
        l = []
        #This is where stuff is stored until it finds a valid comma
        group = ''
        quotes = False
        
        #If you find a comma not inbetween quotes, append the previous stuff you find to the list.
        #Then start again from there.
        for i in text:
            if i == ',' and not quotes:
                l.append(group)
                group = ''
                continue
            elif i == '"':
                if quotes:
                    quotes = False
                else:
                    quotes = True
            group += i

        #Add to l if there is remaining stuff in group.
        if group:
            l.append(group)

        return l

    #Get's the run order for your code
    def getOrd(self, text):
        #Take out trailing characters and then split it by line
        text = text.strip()
        text = text.split('\n')

        #The run order list
        order = []

        #Command arg and inner will be modified and appended to order over and over.
        #Command is the function to run
        #Arg is the stuff inside the ()
        #Inner is the stuff inside the {}
        #Sometimes these things change around, this is usually for variable declarations and dot functions
        command = ''
        arg = ''
        inner = ''

        #Bracks and curlBracks exist to solve nesting issues
        bracks = 0
        curlBracks = 0

        #Which state my code is on. Determines what action it will do and what its looking for.
        state = 1
        #Whether we are declaring a new function or not.
        #Function declaration I have not implemented, but its parts are there.
        funcDec = False

        #Look through lines of code
        for i in range(len(text)):
            #Check if its a comment
            if text[i].strip().startswith('#'):
                continue

            #This is for inner. If inner has a value, we add \n to it.
            #So it will be able to differentiate lines of code in the function we put it into.
            if inner != '':
                inner += '\n'
            
            for a in text[i].strip():
                #Gets the starting command, i.e. the var name or command name
                if state == 1:
                    command += a
                    if a == '(':
                        #Get the arguments in the brackets
                        state = 2
                    if a == '.':
                        #Get the function
                        state = 6
                    #Check that we don't have a number as a variable name start.
                    #I don't need worry about this for functions or dot functions because
                    #they use predefined things and numbers are never defined in the commandDict
                    if a == '=':
                        if re.match(r'^[0-9]', command):
                            return ['err','Don\'t use numbers in variable declarations']
                        #If variable declaration, switch to state for to find what it's value will be
                        state = 4

                #Gets the stuff in ()
                elif state == 2:
                    arg += a
                    #when found stuff inside brackets, go to state 3
                    if a == ')':
                        if bracks == 0:
                            state = 3
                        else:
                            bracks -= 1
                    elif a == '(':
                        bracks += 1
                
                #Gets variable modification part
                elif state == 4:
                    arg += a

                #Check if function had {}, if it does sqitch to state 5.
                #The = one is for function declerations. It's there but it gives info out the end which I don't use.
                elif state == 3:
                    if a == '{':
                        state = 5
                    elif a == '=':
                        funcDec = True
                        state = 7
                
                #Get the innards of the {}.
                elif state == 5:
                    inner += a
                    if a == '{':
                        curlBracks += 1
                    if a == '}':
                        #When you finish getting innards of the {} switch to state 1. Basically reset.
                        if curlBracks == 0:
                            inner = inner[:-1]
                            state = 1
                        else:
                            curlBracks -= 1 

                #The dot function parsing.
                #Switches around command and inner when it gets them both.
                elif state == 6:
                    inner += a
                    if a == '(':
                        state = 2
                        g = command[:]
                        command = inner[:]
                        inner = g[:-1]
        
                #Looks for innards for a function declaration
                elif state == 7:
                    if a == '{':
                        state = 5

            #If we are still getting stuff inside {} dont use up arg, command and inner
            if state != 5:
                #This is here cause I don't really know what to do with a function declaration
                if funcDec:
                    order.append([self.createFunc, command[:-1], (arg[:-1], inner)])
                    arg = ''
                    command = ''
                    funcDec = False

                #Variable declaration section. Just appends, stuff to put into function so that we can run it later.
                if state == 4:
                    order.append([self.varChange, command, arg])
                    arg = ''
                    command = ''
                
                #Remove trailing brackets
                if arg:
                    if arg.endswith(')'):
                        arg = arg[:-1]
                    else:
                        return ['err',f'line {self.line}: missing end bracket']

                if command:
                    command.strip()
                    #remove trailing brackets
                    if command.endswith('('):
                        command = command[:-1]

                    #If it ain't a real command
                    if command not in self.commandDict:
                        return ['err',f'line {self.line}: Command {command} not recognised']
                    elif command not in self.legal:
                        return ['err',f'line {self.line}: Command {command} is illegal for this level']
                    
                    #Appends stuff to put into function along with function so that we can run it later.
                    order.append([self.commandDict[command], arg, inner, self.commandDict])
                
                #reset for next line
                command = ''
                inner = ''
                arg = ''
                state = 1

            self.line += 1
            if self.line > self.lineLimit:
                return ['err', 'line limit exceeded']

        #Returns run order
        return order

    #A delay function, takes an int
    def delay(self, arg, *dump):
        if type(arg) == list:
            return arg
        arg = int(self.intCheck(arg))
        a = time.time()
        while time.time() - a < arg:
            pass

    #An if function. Gets a run order from the inner and if the arg turns out to be true. Run the inner code.
    def _if(self, arg, inner, *dump):
        try:
            order = self.getOrd(inner)
            if type(order) == list:
                if order[0] == 'err':
                    return order
            if self.evaluate(arg):
                #What runs the inner code
                for i in order:
                    out = i[0](i[1],i[2])
                    if type(out) == list:
                        return out
            else:
                pass
        
        except:
            return ['err', 'something went wrong with the if condition']

    #See if something is in front of it.
    #Uses bot see function.
    #Makes sure it sends a string to see function.
    def see(self, arg, *dump):
        arg = self.strCheck(arg)
        if type(arg) == list:
            return arg
        #Returns output from see
        out = self.bot.see(arg)
        if type(out) == list:
            return out
        return str(out)

    #Don't bother looking at this
    def createFunc(self, name, functionality, *dump):
        print(name,functionality)
        localVars = self.getParams(functionality[0])
        code = functionality[1]
        print(localVars)
        def tempFunc(self, arg, *dump):
            arg = self.getParams(arg)
            for i in arg:
                pass

        print(arg)

        pass

    #This is a list function
    def store(self, arg, array, *dump):
        try:
            #Makes sure the thing you use it on is a list.
            #This is a dot function.
            l = self.listCheck(self.commandDict[array])
            if type(l) == list:
                if l[0] == 'err':
                    return l
            arg = eval(self.evaluate(arg))
            if type(arg) == list:
                if arg[0] == 'err':
                    return arg
            l.append(arg)
            #Varchange removes final character, so I just use it with an added disposable '.'
            return self.varChange(array + '.',str(l))
        except:
            return ['err',"You can only store to a list"]

    #This is also a list function
    def remove(self, arg, array, *dump):
        try:
            #Makes sure the thing you use it on is a list.
            #This is a dot function.
            l = self.listCheck(self.commandDict[array])
            if type(l) == list:
                if l[0] == 'err':
                    return l
            #Check if input is integer
            arg = self.intCheck(arg)
            if type(arg) == list:
                return arg
            #Save popped value in ret to return later
            ret = str(l.pop(int(arg)))
            #Change variable to new version without the removed element
            a = self.varChange(array + '.',str(l)) 
            if a:
                return a
            #Return popped value
            return ret
        except:
            return ['err',"Remove requires a list and a number value"]

    #Get size of string or list
    def size(self, arg, array = '', *dump):
        try:
            #This can be a dot function or a normal function.
            #However you can't use this as a dot function with a non variable. Don't ask why I made it like this.
            if array:
                l = eval(self.commandDict[array])
                ret = len(l)
            else:
                errorCheck = self.evaluate(arg)
                if type(errorCheck) == list:
                    return errorCheck
                arg = eval(errorCheck)
                ret = len(arg)
            return str(ret)
        except:
            return ['err',f'size can\'t take a number or a function']

    #This is basically a while loop
    def _loop(self, arg, inner, *dump):
        try:
            originalLine = self.line + 0

            #Get run order of inner which is the code
            order = self.getOrd(inner)
            if type(order) == list:
                if order[0] == 'err':
                    return order

            self.line = originalLine + 1

            #If a plain number is inputed, the loop runs that many times.
            intcheck = self.intCheck(arg)
            if type(intcheck) == list:
                return intcheck

            elif intcheck:
                for arbitaryNum in range(int(intcheck)):
                    self.line = originalLine + 1
                    for i in order:
                        b = None
                        #Check if user hasn't aborted the code
                        events = pygame.event.get()
                        for event in events:
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                pos = pygame.mouse.get_pos()
                                if self.button.rect.collidepoint(pos):
                                    b = self.button.clicked(pos)

                        out = i[0](i[1],i[2])
                        if type(out) == list:
                            return out

                        if type(b) == list:
                            return b
                        
                        self.line += 1
                        if self.line > self.lineLimit:
                            return ['err', 'line limit exceeded']

            else:
                #Keep running innards while arg evaluates to true
                while self.evaluate(arg):
                    self.line = originalLine + 1
                    for i in order:
                        b = None
                        #Check if user hasn't aborted the code
                        events = pygame.event.get()
                        for event in events:
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                pos = pygame.mouse.get_pos()
                                if self.button.rect.collidepoint(pos):
                                    b = self.button.clicked(pos)

                        out = i[0](i[1],i[2])
                        if type(out) == list:
                            return out

                        if type(b) == list:
                            return b
                        
                        self.line += 1
                        if self.line > self.lineLimit:
                            return ['err', 'line limit exceeded']
                        
        except Exception as e:
            return ['err',"something went wrong with the loop condition"]

    #Adds variable to commandDict
    def varChange(self, command, arg, *dump):
        #Make sure it not function or something else invalid
        arg = self.evaluate(arg)
        if type(arg) == list:
            return arg
        try:
            self.commandDict[command[:-1].strip()] = arg.strip()
        except:
            self.commandDict[command[:-1].strip()] = ''

    #Modifies a dataType into a string
    def string(self, arg, *dump):
        try:
            errorCheck = self.evaluate(arg)
            if type(errorCheck) == list:
                return errorCheck

            arg = '"' + self.evaluate(arg) + '"'
            return arg

        except:
            return ['err',f'String can\'t take a function']

    #Changes an intable string into an int
    def integer(self, arg, *dump):
        arg = self.evaluate(arg)
        if type(arg) == list:
            return arg
        try:
            arg = arg[1:-1]
            int(arg)
            return arg
        except:
            return ['err', f'Number requires an intable string']

    #IDK why I made this, but this takes a string argument and then gives an input prompt and returns a string.
    def inp(self, arg, *dump):
        try:
            arg = self.strCheck(arg)
            if type(arg) == list:
                return arg
            return '"' + input(arg) + '"'
        except:
            return ['err','Inp requires a string']

    #Checks if a variable is an int
    def intCheck(self, arg, *dump):
        try:
            arg = str(self.evaluate(arg))
            if type(arg) == list:
                return arg
            int(arg)
            return arg
        except:
            return False

    #Checks if a variable is a list
    def listCheck(self, arg, *dump):
        arg = eval(self.evaluate(arg))
        if type(arg) == list:
            return arg
        else:
            return False

    #Checks if a variable is a string
    def strCheck(self, arg, *dump):
        arg = self.evaluate(arg)
        if type(arg) == list:
            return arg
        #Strings in my script are strings which are wrapped with ""
        if arg.endswith('"') and arg.startswith('"'):
            return arg[1:-1]
        else:
            return False

    #Moves the bot using the bot move function, requires an integer input
    def move(self, arg, *dump):
        integer = self.intCheck(arg)
        if type(integer) == list:
            return integer
        if integer == False:
            return ['err',"Move requires a number"]

        outp = self.bot.move(int(integer))
        if outp:
            return outp

    #Turns left with bot left function, requires an integer input
    def turnLeft(self, arg, *dump):
        integer = self.intCheck(arg)
        if type(integer) == list:
            return integer
        if integer == False:
            return ['err',"turnLeft requires a number"]
            
        self.bot.left(int(integer))

    #Turns right with bot right function, requires an integer input
    def turnRight(self, arg, *dump):
        integer = self.intCheck(arg)
        if type(integer) == list:
            return integer
        if integer == None:
            return ['err',"turnRight requires a number"]
        
        self.bot.right(int(integer))

    #The bot says something.
    #This is not connected to the bot yet.
    #Currently prints to console.
    def say(self, arg, *dump):
        string = self.strCheck(arg)
        if type(string) == list:
            return string
        if string == False:
            return ['err',"say requires a string"]
        print(f'bot says {string}')

    #This is my evaluate function.
    #It replaces variables with their values in an operation.
    #e.g. a + b becomes 1 + 2 if a = 1 and b = 2
    def evaluate(self, arg, *dump):
        try:
            #This is the new arg and it is the old one with variable/functions replaced with counterparts
            narg = ''
            #Just a thing which is true if we are currently looking at something within quotes
            quotes = False
            #param, tempArg, dotFunc and notFunc are used during function handling
            param = ''
            tempArg = ''
            #If notFunc is false we are handling a function
            notFunc = True
            dotFunc = False
            #bracks handles bracket wrapping issues
            bracks = 0

            #Looks through the argument
            for z in range(len(arg)):
                #If notFunc is true, a non integer not within quotes
                #is replaced with its value within the commandDict.
                #While going through the arg we add the value in arg to narg.
                #If the value is in the commandDict we add that to the narg instead.
                if notFunc:
                    halt = False
                    if arg[z] == '"':
                        if quotes:
                            quotes = False
                        else:
                            quotes = True
                        
                        narg += param + '"'
                        param = ''
                        halt = True    

                    #If we hit a space, an operator, brackets, a comma and brackets that aren't in quotes.
                    #Treat them like variables or a function.
                    if arg[z] in '  +-/*().,[]' and not quotes:
                        #Check if the value is an instantiated variable or function
                        if param in self.commandDict and not quotes:
                            #This says it is a dot function
                            if arg[z] == '.':
                                notFunc = False
                                dotFunc = True
                                #Makes bracks -1. It's looking out for a ) but doesn't start with (
                                #You cant put something with {} in a equation or variable declaration
                                bracks -= 1
                                halt = True
                            
                            #Put in the value of the variable in place of the variable in the arg.
                            #It doesn't put it in if the value is a function.
                            elif type(self.commandDict[param]) == str:
                                narg += self.commandDict[param] + arg[z]
                                #Resets the param
                                param = ''
                                halt = True 
                            #This is a normal function not a dot function
                            elif arg[z] == '(':
                                notFunc = False
                                halt = True
                            #IDK why this is here. But it breaks and activates try except.
                            else:
                                narg += self.commandDict[param] + arg[z]
                                param = ''
                                halt = True
                        
                        #If it isn't a function or a variable. Just add it to narg as is.
                        else:
                            narg += param + arg[z]
                            #Reset param after adding it
                            param = ''
                            halt = True
                            
                    #If we did something this run.
                    #It's something we don't want to add to param.
                    if not halt:
                        param += arg[z]

                else:
                    #Handles adding the output of the function to narg.

                    #If we completed finding stuff in the brackets
                    if arg[z] == ')' and bracks == 0:
                        if dotFunc:
                            #A state system
                            stat = 0
                            #The command/function
                            com = ''
                            #The new argument to put into said fucntion
                            newArg = ''

                            #We use the tempArg we got when looking through till we find the latest )
                            for i in tempArg:
                                #Look through tempArg, appending to com until we find the (.
                                #Com will be the dot function.
                                if stat == 0:
                                    if i != '(':
                                        com += i
                                    else:
                                        stat += 1
                                else:
                                    #Then we log everything until we find ).
                                    #This can be a future issue but dot funcs use lists.
                                    #So as of now, there really isn't a reason why there would be
                                    #more brackets in the brackets of the function.
                                    #Until we find ), we are adding to newArg cause it is the
                                    #arguments of the dot function.
                                    if i != ')':
                                        newArg += i
                                    else:
                                        break
                            
                            #c is the output, it equals the output of the function.
                            #param is the list or string that is being affected
                            c = self.commandDict[com](newArg, param)
                        
                        else:
                            #If it ain't a dot function, its just your normal variable with
                            #tempArg as arguments and param as the function.
                            c = self.commandDict[param](tempArg)
                        
                        if type(c) == list:
                            return c

                        #We add c, the function output, to narg
                        narg += c

                        #Then we reset
                        tempArg = ''
                        param = ''
                        notFunc = True
                        dotFunc = False
                    else:
                        #If we haven't found the closing bracket keep adding to temp arg
                        if arg[z] == '(':
                            bracks += 1
                        elif arg[z] == ')':
                            bracks -= 1
                        
                        tempArg += arg[z]

            #If there is a param left at the end. It is processed.
            #We don't need to worry about it being a function or a dot function.
            if param != '':
                if param in self.commandDict and not quotes:
                    if type(self.commandDict[param]) == int or type(self.commandDict[param]) == str:
                        narg += self.commandDict[param]
                else:
                    narg += param
            
            
            #We use eval to evaluate the result of the equation
            narg = eval(narg.strip())
            #If the output is a string, wrap it with double quotes so my code knows its a string.
            if type(narg) == str:
                narg = f'"{narg}"'
            #Otherwise make it a string
            elif type(narg) == int or type(narg) == list:
                narg = str(narg)
            #Return the output
            return narg
        
        except Exception as e: 
            return ['err',f'Error occured with {arg} evaluation: {e}']

    #This simply runs the code
    def run(self):
        order = self.getOrd(self.code)
        if order[0] == 'err':
            return order

        self.line = 1
        for i in range(len(order)):  
            a = order[i][0](order[i][1],order[i][2])
            b = None
            #Check if user hasn't aborted the code
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if self.button.rect.collidepoint(pos):
                        b = self.button.clicked(pos)

            if a:
                if a[0] == 'err':
                    a[1] = f"line {self.line}: " + a[1]
                return a

            if type(b) == list:
                return b

            self.line += 1
            if self.line > self.lineLimit:
                return ['err', 'line limit exceeded']

#A name main thing for my interpreter
if __name__ == "__main__":
    with open('interpret.txt') as f:
        a = control(None, f.read(), None)
        a.run()