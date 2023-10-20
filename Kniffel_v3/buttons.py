import pygame
from pygame.constants import KEYDOWN
from dice import *


import pygame
from pygame.constants import KEYDOWN

class Textfield:
    def __init__(self, x, y, width, height, text, fontsize=30, color=(0,0,0)):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.pos = (self.x, self.y)
        self.size = (self.width, self.height)
        self.text = text
        self.fontsize = fontsize
        self.color = color
        self.bordercolor = color
        
        
    def change_color(self):
        """Change the color of a box to indicate active/inactive state."""
        if self.status:
            self.bordercolor = pygame.Color(255, 0, 0)
        else:
            self.bordercolor = pygame.Color(self.color)
        
    def draw(self, target_surface):
        """Draw Button on Surface."""
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.Surface.fill(target_surface, (255,255,255), self.rect)
        pygame.draw.rect(target_surface, self.bordercolor, self.rect, 2)        #draw a white rectangle on the designated surface. Position and size determined in __init__
        my_font = pygame.font.SysFont("Courier", self.fontsize)                        #define font and text size
        target_surface.blit(my_font.render(self.text, True, (0,0,0)), (self.x+self.fontsize//6, self.y+self.fontsize//3))

    def change_status(self):
        """Change the status if the Button is clicked."""
        self.status = not self.status
        if type(self) == NameButton:
            if self.status: self.text = self.user_input + "|"
            else: self.text = self.user_input
        self.change_color()
        
        
class ClickButton(Textfield):
    def __init__ (self, x, y, width, height, text, fontsize=30, color=(0,0,0), nextbutton=None, status=False):
        """Create a clickable button with attributes determining position and size, a displayed text, its fontsiize and color, as well as an optional next button to cycle through buttons and a status to indicate active/inactive status."""
        super().__init__(x, y, width, height, text, fontsize, color)
        self.nextbutton = nextbutton
        self.status = status
   
    def is_clicked(self, event):
        """Handle mousebuttondown event."""
        if self.rect.collidepoint(event.pos): 
            return True
        else: 
            return False
        
    def handle_keys(self, event):
        """Handle Keyboard events."""
        if event.key == pygame.K_TAB:
            self.change_status()
            self.nextbutton.change_status()
        elif event.key == pygame.K_RETURN:
            if type(self) == NameButton:
                self.change_status()
                self.nextbutton.change_status()
            else:
                return True
        elif type(self) == NameButton:
            self.add_user_input(event)
            
    
        
    
        
class NameButton(ClickButton):
    def __init__ (self, x, y, width, height, color=pygame.Color(0, 0, 0), fontsize=30,  text=None, nextbutton=None, user_input=None, status=False):
        """Create a clickable button, that can be filled with text by the user."""
        super().__init__(x, y, width, height, text, fontsize, color, nextbutton, status)
        self.user_input = user_input
        if self.user_input == None: self.user_input = ""
            
    def add_user_input(self, event):
        """Enable user to input player names via keyboard."""
        if self.status:
            if event.key == pygame.K_BACKSPACE:
                self.user_input = self.user_input[:-1]
            elif len(self.user_input) < 10:
                self.user_input += event.unicode
            self.text = self.user_input + "|"
        else: self.text = self.user_input 
            
        
    
            

class Crossbutton_Old:   
    def __init__ (self, rect = None):
        """Button to cross one score off of Player's scoresheet"""

        self.rect = rect                                        #establish rectangle in desired position/size
        self.rect = pygame.Rect(600, 800, 120, 50)
        

    def is_clicked(self, event, player):
        """Handle mousebuttondown event that collides with the button. Parameters event and player needed."""

        if self.rect.collidepoint(event.pos):                   #if event position collides with rectangle of button
            for i in player.scores.redtextind:                  #change scoring options back to zero (previously changed to potential value)
                player.scores.change_value(i, 0)
            player.crosses = True                               #Player state changed to "crosses"
            player.scores.redtextind = []                       #scoring options deleted
            player.scores.redrect = []                          #rectangles corresponding to scoring options deleted
            player.scores.purptextind = []                      #making sure list of crossing options is empty
            player.scores.purprect = []                         #making sure list of rectangles corresponding to crossing options is empty
            if player.scores.ones == 0:                         #if a scoring option is neither crossed off, nor already taken, add to list of crossing options
                player.scores.purptextind.append(0)
            if player.scores.twos == 0:
                player.scores.purptextind.append(1)
            if player.scores.threes == 0:
                player.scores.purptextind.append(2)
            if player.scores.fours == 0:
                player.scores.purptextind.append(3)
            if player.scores.fives == 0:
                player.scores.purptextind.append(4)
            if player.scores.sixes == 0:
                player.scores.purptextind.append(5)
            if player.scores.three_of_a_kind == 0:
                player.scores.purptextind.append(7)
            if player.scores.four_of_a_kind == 0:
                player.scores.purptextind.append(8)
            if player.scores.full_house == 0:
                player.scores.purptextind.append(9)
            if player.scores.small_street == 0:
                player.scores.purptextind.append(10)
            if player.scores.big_street == 0:
                player.scores.purptextind.append(11)
            if player.scores.kiffel == 0:
                player.scores.purptextind.append(12)
            if player.scores.chance == 0:
                player.scores.purptextind.append(13)

    def draw(self, target_surface):
        """Blit button on main surface. Target surface parameter needed."""

        pygame.draw.rect(target_surface, (255, 255, 255), self.rect)        #draw a white rectangle on the designated surface. Position and size determined in __init__
        my_font = pygame.font.SysFont("Courier", 30)                        #define font and text size
        self.text = my_font.render("Cross", True, (0,0,0))                  #attribute the render of the word "Cross" in black to parameter text
        target_surface.blit(self.text, (605, 810))                          #blit render on designated coordinates

class Rollbutton_Old:
    def __init__ (self, rect = None):
        """Button to roll dice that have not been kept."""

        self.rect = rect
        self.rect = pygame.Rect(450, 800, 120, 50)                          #establish rectangle in desired position/size
        
    def is_clicked(self, event, player):
        """Handle event mousebutton down if it collides with button-rectangle"""

        if self.rect.collidepoint(event.pos):                               #if event collides with rectangle
            if player.rollcount == 3:                                       #if player has already rolled 3 times, button is deactivated
                return
            else:   
                player.rollcount += 1                                       #else: update player's rollcount by +1
            for i in player.scores.redtextind:                              #for every scoring option the player has (determined in player.checkoptions()), change value to zero (new roll, so new options needed)
                player.scores.change_value(i, 0)
            player.scores.redtextind = []                                   #empty list of scoring options
            player.scores.redrect = []                                      #empty list of corresponding rectangles
            
            count = 0
            if player.roll == []:                                           #if this is the player's first roll, create dice objects in the amount of 5 (maximum number of dice). If not, subtract amount of kept dice from 5.
                for i in range(5 - len(player.kept)):
                    i = Dice()
                    i.index = count                                         #each die gets an index to represent it's position relative to the other dice
                    i.roll_one()                                            #each die is rolled (starts rolling animation)
                    count += 1                                              #count increased for index of next dice
                    player.roll.append(i)                                   #append the current player's rolled list containing their rolled (not kept) dice
            else:
                for i in player.roll:                                       #for each die in player's rolled list
                    i.roll_one()                                            #roll die
                
    def draw(self, target_surface):                                         
        """Blit button with text "Roll" on designated surface. Requires surface parameter."""

        pygame.draw.rect(target_surface, (255, 255, 255), self.rect)       #See Crossbutton for explanation
        my_font = pygame.font.SysFont("Courier", 30)
        self.text = my_font.render("Roll", True, (0,0,0))        
        target_surface.blit(self.text, (455, 810))
        
        
class Box:
    def __init__(self, number, next = None, color = pygame.Color(31, 222, 219), status = False, x = 200, y = 400, user_input = ""):
        """Create a box that displays a number of players, that can be clicked and cosecutively changes to an input 
        box that allows for player names to be given according to the number of players that has been chosen. Requires number and has a color, status, x-, and y-position and user input."""  

        my_font = pygame.font.SysFont("Courier", 30)
        self.status = status
        self.number = number
        self.next = next
        self.color = color
        self.text = my_font.render(str(self.number), True, (0,0,0))
        self.x = x
        self.y = y
        self.user_input = user_input
        self.makebox()                                                  #calculate position for individual box
        self.rect = pygame.Rect(self.x, self.y, 200, 50)                #establish rectangle with x- and y- position and designated size
        
    def __str__(self):
        """format string for number display"""

        return(str("    {0}".format(self.number)))                      

    def makebox(self):   
        """calculate individual x-, and y-position corresponding to number"""

        if self.number % 2 == 0:
            self.x += 300
        if self.number == 3 or self.number == 4:
            self.y += 100
        if self.number > 4:
            self.y += 200
        
    def is_clicked(self, event, boxes):
        """handle events. Requires event and list of boxes."""                                             

        my_font = pygame.font.SysFont("Courier", 30)
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.is_active(boxes)         
            else:
                self.status = False                                                     #if box has not been clicked, it is inactive

        if event.type == pygame.KEYDOWN:                                                #if the event is keydown
            if self.status:                                                             #if box is active
                if event.key == pygame.K_RETURN or event.key == pygame.K_TAB:           #if return is clicked, deactivate box and activate next one
                    self.is_active(boxes)
                    self.next.is_active(boxes)
                    return 1
                
                elif event.key == pygame.K_BACKSPACE:                                   #if backspace is clicked, delete last symbol in input
                    self.user_input = self.user_input[:-1]
                else:
                    if len(self.user_input) < 10:
                        self.user_input += event.unicode                                #if any other button is clicked, append user_input
                self.text = my_font.render((self.user_input + "|"), True, (0, 0, 0))    #render user input
        
    def is_active(self, boxes = None):
        """activate (or deactivate) a box that has been clicked on"""

        my_font = pygame.font.SysFont("Courier", 30)
        self.status = not self.status
        if self.status:
            self.color = pygame.Color(240, 80, 217)
            x = boxes.copy()                                                    #copy list of existing boxes
            x.remove(self)                                                      #if a box has been clicked, remove it from the copied list
            for i in x:
                if i.user_input == "":                                          #if there is no user input in the boxes in the copied list: display their number and set status to False (inactive)
                    i.text = my_font.render(str(i.number), True, (0,0,0))
                    i.status = False
                    i.color = pygame.Color(31, 222, 219)
                if i.user_input != "":                                          #if there is an input, don't display the number
                    i.text = my_font.render(i.user_input, True, (0,0,0))
                    i.status = False
                    i.color = pygame.Color(31, 222, 219)
            self.text = my_font.render(self.user_input + "|", True, (0,0,0))    #display a "|" to indicate being ready to take text-input
        else:
            self.color = pygame.Color(31, 222, 219)

    def draw(self, screen):
        """blit box on screen"""

        screen.blit(self.text, (self.rect.x+5, self.rect.y+5))
        pygame.draw.rect(screen, self.color, self.rect, 2)
