import pygame
import sys
import random
import copy

from pygame.constants import MOUSEBUTTONDOWN
from buttons import *
from dice import *
from players import *
from scoresheet import *

def end_screen(playerlist):
    playerlist.sort(reverse=True)
    
    for index, item in enumerate(playerlist):
        if len(playerlist) < 4:
            item.index = index
            item.x = 325 - ((len(playerlist) - 2) * 75) + (item.index * 150)
            for value in item.scores.scores.values():
                value.x = item.x + item.index*50
        else:
            if index > 2:
                item.index = index - 3
                item.x = 325 - ((len(playerlist) - 2) * 75) + ((item.index) * 150)
                item.y += 400
                for key, value in item.scores.scores.items():
                    value.x = item.x + item.index*50
                    if type(key) == type(1):
                        value.y = item.y + 320/16*(key-1)
                item.scores.scores["total top"].y = item.y + 320/16*(6)
                item.scores.scores["bonus"].y = item.y + 320/16*(7)
                item.scores.scores["total"].y = item.y + 320/16*(15)
            else:
                item.index = index
                item.x = 325 - ((len(playerlist) - 2) * 75) + (item.index * 150)
                for value in item.scores.scores.values():
                    value.x = item.x + item.index*50
                    
    while True:            
        clock = pygame.time.Clock()                                                                            
        surface_sz = 1000                                                                                   
        main_surface = pygame.display.set_mode((surface_sz, surface_sz))
        
        ev = pygame.event.poll()                                                                        #Look for any event
        if ev.type == pygame.QUIT:                                                                      #window close button clicked?
            pygame.quit()                                                                               #quit game
            sys.exit() 
        
        main_surface.fill((0, 200, 255))
        for i in playerlist:
            if i == playerlist[0]: i.myturn = True
            else: i.myturn = False
            i.draw(main_surface)
        pygame.display.flip()
        clock.tick(60)
               
def get_names():
    """Preparation of the game. Enables user to put in up to six player names."""
    
    clock = pygame.time.Clock()                                                                          
    main_surface = pygame.display.set_mode((1000, 1000))                                                  
    MYFONT = pygame.font.SysFont("Courier", 30)                                                        
    TEXTPOS, TEXTPOSTWO = (70, 250), (25, 300) # Assign two positions for the text above the buttons. 
    the_text = MYFONT.render("Click on a box to enter a Player's name. Click", True, (0,0,0))          #set text above boxes for introductions
    the_text_two = MYFONT.render("'Continue' to confirm the players and start the game.", True, (0,0,0))
    buttons = list()                                                                                          
    playerlist = list()                                                                                    

    
    for i in range(1, 7):
        x = y = 0
        if i % 2 == 0:
            x = 300
        if i in [3, 4]:
            y = 100
        if i in [5, 6]:
            y = 200
        i = NameButton(200+x, 400+y, 200, 50)
        buttons.append(i)
          
    continue_button = ClickButton(350, 700, 200, 50, " CONTINUE",)
    buttons.append(continue_button)

    for index, i in enumerate(buttons):
        if index+1 < len(buttons):
            i.nextbutton = buttons[index+1]
        else:
            i.nextbutton = buttons[0]
    buttons[0].change_status()
    
    while True:
        ev = pygame.event.poll()                                                                        #Look for any event
        if ev.type == pygame.QUIT:                                                                      #window close button clicked?
            pygame.quit()                                                                               #quit game
            sys.exit()                                                                                  #exit compiler

        if ev.type == pygame.MOUSEBUTTONDOWN:
            for i in buttons[:-1]:
                if i.is_clicked(ev) and i.status:
                    break
                elif i.is_clicked(ev):
                    for j in buttons[:-1]:
                        j.text = j.user_input
                        j.status = False
                        j.change_color()
                    continue_button.status = False
                    i.change_status()
        
            if continue_button.is_clicked(ev):
                for i in buttons[:-1]:
                    if i.user_input != "":
                        playerlist.append(i.user_input)
                if playerlist != []: return playerlist
            
        if ev.type == pygame.KEYDOWN:
            
            for i in buttons:
                if i.status:
                    if i.handle_keys(ev):
                        for i in buttons[:-1]:
                            if i.user_input != "":
                                playerlist.append(i.user_input)
                        if playerlist != []: return playerlist
                    break
                
        main_surface.fill((255,255,255))                                                                #background is white
        main_surface.blit(the_text, TEXTPOS)                                                            #blit texts on screen
        main_surface.blit(the_text_two, TEXTPOSTWO)
        
        for i in buttons:                                                                                 #draw boxes
            i.draw(main_surface)     
        pygame.display.flip()
        clock.tick(60)
                                                                                          #limit to 60fps
                                                                                          
def main(): 
    pygame.init()                                                                                      #initiealize pygame and set up screen
    clock = pygame.time.Clock()
    main_surface = pygame.display.set_mode((1000, 1000))
    namelist = get_names()                                                                             #start the games' first screen and get the list of players 
    playerlist = list()                                                                                   #create empty playerlist

    
    for index, item in enumerate(namelist):                                                            #set up the players. 
        if len(namelist) %2 == 0:                                                                      #if there is an even number, the distance from the center of the screenwidth is equal
            posx = 325 - ((len(namelist) - 2) * 75) + (index * 150)
            newplayer = Player(str(item), index, posx)
            newplayer.scores.set_up_standard_scoring_options()
            playerlist.append(newplayer)                                                                       #playerlist is appended with each player
        else:
            posx = 400 - ((len(namelist) - 1) * 75) + (index * 150)                                    #if there is an odd number, there is a player in the center of the screen
            newplayer = Player(str(item), index, posx)
            newplayer.scores.set_up_standard_scoring_options()
            playerlist.append(newplayer)
    
    if len(playerlist) > 1:
        for index, i in enumerate(playerlist):
            if index < len(playerlist)-1:
                i.nextplayer = playerlist[index+1]
            else:
                playerlist[-1].nextplayer = playerlist[0]
        
    rollbutton = ClickButton(250, 800, 180, 50, "   Roll")                                                                          #establish rollbutton
    crossbutton = ClickButton(450, 800, 180, 50, "  Cross")                                                                        #establish crossbutton
    continuebutton = ClickButton(650, 800, 190, 50, " Continue")
    loadgamebutton = ClickButton(800, 800, 180, 50, "Load")

    playerlist[0].myturn = True                                                                       #it's the first player's turn
    activeplayer = playerlist[0]                                                                                    #playercount starts with 1
    turns = 12                                                                                          #number of turns starts with 1

    while True:                                                                                        #start game loop
        if turns <= playerlist[0].scores.length: 
            if len(playerlist) == 1:                                                                   #if there is only 1 player, that player remains active and turns are counted after each of their decisions to cross off, or take a score
                if playerlist[0].myturn == False:  
                    turns += 1
                    playerlist[0].myturn = True                    
            elif activeplayer.myturn == False:
                for i in playerlist:
                    if i.myturn:
                        activeplayer = i
                        if activeplayer is playerlist[0]: turns += 1
        else:
            for i in playerlist:
                i.scores.calculate_dependant_scores()
                i.scores.calculate_total()
            end_screen(playerlist)
                
        
        ev = pygame.event.poll()    
        if ev.type == pygame.QUIT:  
            pygame.quit()
            sys.exit()

        if ev.type == pygame.MOUSEBUTTONDOWN:
            
            if activeplayer.myturn == False:
                if len(playerlist) > 1 and continuebutton.is_clicked(ev):
                    activeplayer.nextplayer.myturn = True
                    continuebutton.change_status()
                else:
                    continue
            
            if rollbutton.is_clicked(ev):
                if activeplayer.rollcount < 3:
                    activeplayer.roll()
            
            if crossbutton.is_clicked(ev):
                if activeplayer.status == 1:
                    activeplayer.status = 0
                else:
                    activeplayer.status = 1
                    activeplayer.scores.reset_displayvalues()
                    
            if len(playerlist) > 1 and activeplayer.myturn == False and continuebutton.is_clicked(ev):
                activeplayer.nextplayer.myturn = True
            
            for die in activeplayer.dice.values():
                if die.is_clicked(ev):
                    activeplayer.keep(die)
                    break
            
                
            for value in activeplayer.scores.scores.values():
                if activeplayer.status == 0 and value.is_clicked(ev):
                    if value.displayvalue == 0:
                        break
                    value.take_option()
                    activeplayer.scores.calculate_dependant_scores()
                    activeplayer.end_turn()
                    continuebutton.change_status()
                    break
                elif activeplayer.status == 1 and value.is_clicked(ev):
                    if value.displayvalue != "X":
                        break
                    value.cross_option()
                    activeplayer.scores.calculate_dependant_scores()
                    activeplayer.end_turn()
                    continuebutton.change_status()
                    break
                    
        for die in activeplayer.rolled.values():
                die.roll_animation()            
                
        if activeplayer.status == 0 and len(activeplayer.rolled) >= 1:
            for die in activeplayer.rolled.values():
                if not die.wait >= 30:
                    break
                activeplayer.display_options()
        if activeplayer.rollcount != 0:
            activeplayer.display_cross_options()
            
        main_surface.fill((0, 200, 255))

        for die in activeplayer.rolled.values():
            die.draw(main_surface)
        for die in activeplayer.kept.values():
            die.draw(main_surface)   
        for i in playerlist:
            i.draw(main_surface)
            
        crossbutton.draw(main_surface)
        rollbutton.draw(main_surface)
        continuebutton.draw(main_surface)

        pygame.display.flip()
        clock.tick(60)

    
main ()
