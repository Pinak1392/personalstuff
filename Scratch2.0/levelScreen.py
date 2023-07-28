import pygame
from color import *
import sprite as obj
import pygame_textinput as pt
from renderLevel import *
import console as con
from topLevelBar import *
from interpreter import *
from copy import deepcopy
from levels import *

def levelScreen(screen, lvl):
    #Get sprites to render and the bot object
    curSprites, bot, valids, validations, challenge = renderLVL((550,500), lvl, 700, 50, screen)
    #Create text input box
    txtInp = pt.Textinput('TextArea',300,500,350,50,'')
    curSprites.add(txtInp)
    #Create console box
    c = con.Console(900,170,350,570,'')
    curSprites.add(c)
    objective = con.Tooltip(challenge, 300, 150, 10, 50)
    curSprites.add(objective)
    helptip = con.Help(eval(f'text_{lvl}'), 300, 510, 10, 230)
    curSprites.add(helptip)
    toplevelBar = TopBar(lvl, 1260, 40, 0, 0)
    curSprites.add(toplevelBar)

    #A dictionary to store values that can be requested
    #I did this because I thought there would be issues with displaying
    #and that displays would be controlled of a singular loop looking at this dict values.
    #It's nothing but a gimmick rn. I also made it this way because of how I stored my variables in my
    #interpreter and that thing stuck with me. So I randomly made things structured like that because I forgot
    #how normal variables worked and somehow I could visualize it better. I think I was afraid that the variable
    #would be lost as that is what happens in my program. So to me at the time, I think variables were one
    #time disposables unless they were placed in a dict. But, I won't change how it is now. For there is a story
    #behind this now. And I have grown attached to it.
    offers = {}
    offers['fill'] = (255,255,100)
    offers['cursprites'] = curSprites
    offers['bot'] = bot
    offers['code'] = None
    offers['console'] = c
    offers['tbox'] = txtInp
    offers['valid'] = valids

    done = False
    while not done:
        pygame.event.pump()
        screen.fill(offers['fill'])
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT: # If user clicked close
                return 0
            #Changes stuff using outputs of the functions
            elif event.type == pygame.KEYDOWN:
                for i in offers['cursprites']:
                    if 'keyPressed' in dir(i):
                        outP = i.keyPressed(event)
                        if outP:
                            for a in outP:
                                offers[a[1]] = a[0]

            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                #Gets clicked and not clicked sprites
                clicked_sprites = [s for s in offers['cursprites'] if s.rect.collidepoint(pos)]
                notClicked_sprites = [s for s in offers['cursprites'] if not s.rect.collidepoint(pos)]
                for i in clicked_sprites:
                    if 'clicked' in dir(i):
                        outP = i.clicked(pos)
                        if outP:
                            #This int assumes that the user has clicked to go to next level
                            if type(outP) == int:
                                #So we go out of the level with an int
                                return outP
                            else:
                                #Changes stuff using outputs of the functions
                                for a in outP:
                                    offers[a[1]] = a[0]

                for i in notClicked_sprites:
                    #Changes stuff using outputs of the functions
                    if 'notClicked' in dir(i):
                        i.notClicked(pos)

        #If we have code to execute, execute it. Code is detected when run is clicked.
        if offers['code']:
            #Change the bots internal sprite log to the ones on the level
            offers['bot'].curSprites, offers['bot'].fill = offers['cursprites'], offers['fill']
            try:
                #Run the level
                out = control(offers['bot'], offers['code'], offers['tbox'], offers['valid'], offers['valid']['vars'][0]).run()
            except:
                out = control(offers['bot'], offers['code'], offers['tbox'], offers['valid']).run()
            
            #Reset the bot orientation and internal sprite log and level
            offers['bot'].reset()
            if out:
                #If we win, validate
                if out[0] == 'win':
                    offers['console'].update('Running validation tests')
                    offers['cursprites'].draw(screen)
                    pygame.display.flip()
                    offers['bot'].sim = True
                    failed = False
                    #Validates the code by running other levels against it
                    for i in validations:
                        offers['bot'].lvl = deepcopy(i)
                        try:
                            out = control(offers['bot'], offers['code'], offers['tbox'], offers['valid'], offers['valid']['vars'][i + 1]).run()
                        except:
                            out = control(offers['bot'], offers['code'], offers['tbox'], offers['valid']).run()

                        #Check if we win those levels
                        if out:
                            if out[0] != 'win':
                                failed = True
                                if len(out) > 1:
                                    offers['console'].update(f'Validation failed with {out[0]} {out[1]}')
                                break
                        else:
                            failed = True
                            offers['console'].update('Validation Failed, try again')
                            break
                    
                    #If we haven't failed, we have won the level.
                    if not failed:
                        offers['console'].update('Good job you did it')
                        offers['cursprites'].draw(screen)
                        pygame.display.flip()
                        time.sleep(1)
                        #We output to next level.
                        return lvl + 1

                elif out[0] == 'err':
                    #If we hit error output it to console
                    offers['console'].update(out[1])

            #Updates the abort button if you didnt click while running
            if offers['tbox'].buttonOff:
                offers['tbox'].buttonOff = False
                for i in offers['tbox'].runButton:
                    i.text = 'Run'
                    i.update()
                offers['tbox'].textBlit()
            
            offers['bot'].sim = False
            offers['code'] = ''
        
        #Draws the sprites
        offers['cursprites'].draw(screen)

        #update screen
        pygame.display.flip()


if __name__ == "__main__":
    # Initialize the game engine
    pygame.init()
    pygame.font.init()

    # Set the height and width of the screen
    size = [1260, 740]
    screen = pygame.display.set_mode(size)

    levelScreen(screen, 1)
    levelScreen(screen, 2)
    levelScreen(screen, 3)

    # Be IDLE friendly
    pygame.quit()