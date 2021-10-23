import pygame
import sys
import random
import copy



class Crossbutton:   
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

class Rollbutton:
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


class Dice:
    def __init__(self, value = 0, img = None, posn = (0, 0), taken = False, x=0, y=0, rect = None, index = 0, i = 0, wait = 3, rndval = None):
        """Create a dice object that stores its value (random number between 1 and 6), an index that determines its relative position to the four other dice,
        the sprite-sheet of 6 dice, its position on that sheet as determined by its value, the sprite size, its position on the screen, its rectangle, a taken value, 
        signifying if the die is kept for next roll or rolled again and an index i used to determine the end of the rolling-animation probably unnecessary: wait"""

        import random
        rng = random.Random()                                               #establish random object
        dice_all_sides = pygame.image.load("dice.jpg")                      #load sprite-sheet
        self.img = img
        self.img = dice_all_sides                                           #reference sprite-sheet as attribute
        dice_width = dice_all_sides.get_width()//6                          #get width of single sprite
        dice_height = dice_all_sides.get_height()                           #get height of single sprite (== height of sprite-sheet)
        self.value = value                  
        self.value = rng.randrange(1, 7)                                    #determine random value between 1 and 6
        self.posn = posn
        self.size = (dice_width, dice_height)                               #size is tuple determined by single sprite
        self.posn = (self.size[0]*(self.value-1), 0)                        #position of individual sprite is determined by value
        self.sprite = self.cutsprite()                                      #the sprite is cut out by method cutsprite
        self.x = x 
        self.y = y
        self.rect = rect
        self.rect = pygame.Rect(self.x, self.y, dice_width, dice_height)    #rectangle is established with coordinates on screen and size
        self.taken = taken
        self.index = index
        self.i = i
        self.wait = wait
        self.rndval = rndval

    def cutsprite (self):
        """Get single sprite coordinates and size"""

        dice_sprite = (self.posn[0], self.posn[1], self.size[0], self.size[1])
        return dice_sprite

    def draw(self, target_surface):
        """Blit Die on screen, establish a small animation to represent the action of rolling a die."""

        rng = random.Random()
        animlen = 27                                                                #length of animation is set to 27
        if self.wait % 3 == 0 and self.i < animlen:                                 #as long as parameter i is smaller than length of animation and 3 frames have passed, value is changed
            self.rndval = rng.randrange(1, 7)                                       #change value of sprite
            self.posn = (self.size[0]*(self.rndval-1), 0)                           #determine position on spritesheet for changed value
            target_surface.blit (self.img, (self.x, self.y), self.cutsprite())      #blit sprite on surface
            self.i += 1                                                             #increase i until length of animation reached
            self.wait += 1
            return
        elif self.wait % 3 != 0 and self.i < animlen:                               #if i smaller than animlen and 3 frames have not passed, display same sprite
            target_surface.blit (self.img, (self.x, self.y), self.cutsprite())      #blit sprite on surface
            self.i += 1                                                             #increase i until length of animation reached
            self.wait += 1
        else:
            self.posn = (self.size[0]*(self.value-1), 0)                            #if i reaches length of animation: set position on sprite-sheet to the one corresponding to the value
            target_surface.blit (self.img, (self.x, self.y), self.cutsprite())      #blit
            return

    def keep(self, event):
        """Hanlde event mousebuttondodwn to determine whether a die is to be kept or rolled again with next roll."""

        if self.taken == False and self.rect.collidepoint(event.pos):               #if die is not kept and clicked on 
            self.taken = not self.taken                                             #state changes to self.taken == True (die is kept)
            self.y -= 150                                                           #position is changed to signify it being kept
            self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])     #rectangle changed to new position
        if self.taken and self.rect.collidepoint(event.pos):                        #if die is kept and clicked on, previous actions are reversed
            self.taken = not self.taken
            self.y += 150
            self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])

    def roll_one(self):
        """Change the value of die to a new random number between 1 and 7"""

        import random
        rng = random.Random()                                                       #create new random object
        self.i = 0                                                                  #set index i to 0 to start new animation
        self.value = rng.randrange(1, 7)                                            #set new value between 1 and 6
        self.posn = (self.size[0]*(self.value-1), 0)                                #change sprite-position according to new value
        self.x = self.size[0]*self.index + 50*(self.index+2)                        #determine position on screen
        self.y = 600 
        
    def __str__(self):
        """Make Die-Value printable"""

        return(str(self.value))
                

                
class Scoresheet:
    def __init__(self, ones = 0, twos = 0, threes = 0, fours = 0, fives = 0, 
    sixes = 0, bonus = 0, three_of_a_kind = 0, four_of_a_kind = 0, 
    full_house = 0, small_street = 0, big_street = 0, kiffel = 0, 
    chance = 0, total = 0, redtextind = [], redrect = [], purptextind = [], purprect = []):  
        """Establish a scoresheet that keeps track of the scores for a single player. It also stores lists for scoring options (redtextind) 
        and their corresponding rectangles (redrect) as well as for crossing options (purptextind) and their corresponding rectangles (purprect)."""

        self.ones = ones
        self.twos = twos
        self.threes = threes
        self.fours = fours
        self.fives = fives
        self.sixes = sixes
        self.bonus = bonus
        self.three_of_a_kind = three_of_a_kind
        self.four_of_a_kind = four_of_a_kind
        self.full_house = full_house
        self.small_street = small_street
        self.big_street = big_street
        self.kiffel = kiffel
        self.chance = chance
        self.total = total
        self.top = self.ones + self.twos + self.threes + self.fours + self.fives + self.sixes
        self.redtextind = redtextind
        self.redrect = redrect
        self.purptextind = purptextind
        self.purprect = purprect

    def won(self, target_surface, player):
        """Create a red border for winner's scoresheet"""

        rect = pygame.Rect(player.x, player.y + 50, 185, 300)                    #create a rectangle for scoresheet
        pygame.Surface.fill(target_surface, (255,255,255), rect)
        pygame.draw.rect(target_surface, (255, 0, 0), rect, 2)                   #draw the white rectangle on target surface 
        my_font = pygame.font.SysFont("Courier", 15)                             #set text font and size
        splittext = str(self).split(",")  
        color = (0, 0, 0)  
        for index, i in enumerate(splittext):                                    #display scoring possibilities regularly if they are in neither list
            text = my_font.render(i, True, color)
            target_surface.blit(text, (rect.x+5, player.y + 50 + index * 20))

    def change_value(self, index, value):
        """Change the value of an attribute indicated by an index to the given value, if it equals zero."""

        if index == 0:
            self.ones = value
        if index == 1:
            self.twos = value
        if index == 2:
            self.threes = value
        if index == 3:
            self.fours = value
        if index == 4:
            self.fives = value
        if index == 5:
            self.sixes = value
        if index == 7:
            self.three_of_a_kind = value
        if index == 8:
            self.four_of_a_kind = value
        if index == 9:
            self.full_house = value
        if index == 10:
            self.small_street = value
        if index == 11:
            self.big_street = value
        if index == 12:
            self.kiffel = value
        if index == 13:
            self.chance = value
        
    def has_bonus(self):
        """Check if the value of the top part of the scoresheet is equal or higher 63. If so, set bonus to 35 points."""

        if self.ones + self.twos + self.threes + self.fours + self.fives + self.sixes >= 63:
            self.bonus = 35

    def __str__ (self):
        """Return a formatted string of the scores."""

        return """1:               {0},2:               {1},3:               {2},4:               {3},5:               {4},6:               {5},Bonus:           {6},Three of a kind: {7},Four of a kind:  {8},Full House:      {9},Small Street:    {10},Big Street:      {11},Kiffel:          {12},Chance:          {13},Total:           {14}""".format(self.ones, self.twos, self.threes, self.fours, self.fives, self.sixes, self.bonus , self.three_of_a_kind, 
        self.four_of_a_kind, self.full_house, self.small_street, self.big_street, self.kiffel, 
        self.chance, self.total)              
                
    def showsheet(self, target_surface, player):
        """Draw a player's scoresheet. Requires target_surface and player."""

        options = player.checkoptions()                                     #get scoring options of player
        rect = pygame.Rect(player.x, player.y + 50, 185, 300)               #create a rectangle for scoresheet
        pygame.draw.rect(target_surface, (255, 255, 255), rect)             #draw the white rectangle on target surface 
        my_font = pygame.font.SysFont("Courier", 15)                        #set text font and size
        splittext = str(self).split(",")                                    #split the string of scoresheet into a list
        if player.crosses == False and type(options) == type ([]):          #if the player has not clicked the cross button and they have already rolled (options is not None)
            for i in options:
                self.redtextind.append(i[0])                                #append the options list with the index corresponding to a scoring option
                self.change_value(i[0], i[1])                               #change the value of that option to the potential value if said option is picked
        
        color_inactive = (0,0,0)                                            #define colors for different actions
        color_active = (255,0,0)
        color_cross = (140, 0, 255)

        for index, i in enumerate(splittext):                               #for items in the list of all scoring possibilities
             
            if player.crosses and index in self.purptextind:                #if the player has clicked the cross button and the index of a scoring possibility is part of the list of crossing options
                color = color_cross                                         #set color to indicate crossing off
                x = pygame.Rect(rect.x, player.y + 50 + index*20, 180, 20)  #create rectangle for single crossing option (y value is set through index of a single scoring possibility)
                pygame.draw.rect(target_surface, color, x, 2)               #draw rectangle with bordering the crossing option
                text = my_font.render(i, True, color)                       #render text for scoring possibility in crossing color
                target_surface.blit(text, (rect.x+5, player.y + 50 + index * 20))       #blit
                if len(self.purprect) < len(self.purptextind):              #add rectangle for crossing option to list of rectangles (purprect) if it has not yet been added
                    self.purprect.append(x)
                

            elif index in self.redtextind:                                  #if the index of a scoring possibility is part of the options list
                color = color_active                                        #set color to indicate scoring option
                x = pygame.Rect(rect.x, player.y +50 + index *20, 180, 20)  #create rectangle
                pygame.draw.rect(target_surface, color, x, 2)               #draw rectangle
                text = my_font.render(i, True, color)                       #render text
                target_surface.blit(text, (rect.x+5, player.y + 50 + index * 20))       #blit
                if len(self.redrect) < len(self.redtextind):                #add rectangle to list of scoring options if not yet part
                    self.redrect.append(x)
        
            else:
                color = color_inactive                                      #display scoring possibilities regularly if they are in neither list
                text = my_font.render(i, True, color)
                target_surface.blit(text, (rect.x+5, player.y + 50 + index * 20))
              
    def picked(self, event, player):                                        #Let player pick scoring/crossing off options
        
        for index, i in enumerate(self.purprect):                       
            if i.collidepoint(event.pos) and len(self.purptextind) > 0:     #if clicked on a rect that is in purprect list
                self.change_value(self.purptextind[index], "X")             #change value of clicked option to "X"
                self.purptextind = []                                       #empty all lists for next roll
                self.purprect = []
                player.roll = []
                player.kept = []
                player.my_turn = False                                      #change player status to not my_turn and not crosses
                player.crosses = False
                player.rollcount = 0                                        #reset player's rollcount

        for index, i in enumerate(self.redrect):
            if i.collidepoint(event.pos) and len(self.redtextind) > 0:      #if clicked on a rect that is in redrect list
                self.redtextind.remove(self.redtextind[index])              #remove clicked item from redtextind list
                self.redrect = []                                           #empty redrect list
                for i in self.redtextind:                                   #change values of remaining scoring options in redtextind to 0
                    self.change_value(i, 0)
                self.redrect = []                                           #empty all lists for next roll
                self.redtextind = []
                player.roll = []
                player.kept = []
                self.has_bonus()                                            #check if points needed for bonus reached
                player.my_turn = False                                      #change player status to not my_turn
                player.rollcount = 0                                        #reset player's rollcount
        
    def calc_total(self):                                                   #make sure that no option has the value "X" in the calculation of total scores
        if self.ones == "X":
            self.ones = 0
        if self.twos == "X":
            self.twos = 0
        if self.threes == "X":
            self.threes = 0
        if self.fours == "X":
            self.fours = 0
        if self.fives == "X":
            self.fives = 0
        if self.sixes == "X":
            self.sixes = 0
        if self.three_of_a_kind == "X":
            self.three_of_a_kind = 0
        if self.four_of_a_kind == "X":
            self.four_of_a_kind = 0
        if self.full_house == "X":
            self.full_house = 0
        if self.small_street == "X":
            self.small_street = 0
        if self.big_street == "X":
            self.big_street = 0
        if self.kiffel == "X":
            self.kiffel = 0
        if self.chance == "X":
            self.chance = 0
        
        self.total = self.ones + self.twos + self.threes + self.fours + self.fives + self.sixes + self.bonus + self.three_of_a_kind + self.four_of_a_kind + self.full_house + self.small_street + self.big_street + self.kiffel + self.chance
                

class Player:
    def __init__(self, name, x, position = 0, y = 50, fontsize = 20, roll = [], kept = [], my_turn = False, rollcount = 0, crosses = False):
        """Establish a player with a name and a scoresheet, that can perform rolls, an x and y value for the positioning on screen, lists for kept and rolled dice, 
        a counter that keeps track of how many times they have rolled, two statuses to determine if it is their turn and whether they want to cross off an option, and the fontsize for displaying their name."""
        self.my_turn = my_turn
        self.name = name
        self.position = position
        self.scores = Scoresheet()                         
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y+5, 130, 30)
        self.fontsize = fontsize
        self.roll = roll
        self.kept = kept
        self.rollcount = rollcount
        self.crosses = crosses

    def draw(self, target_surface):                                             #draw (see Crossbutton for explanation)
        """Draw player name and box. Target surface required."""

        self.rect = pygame.Rect(self.x, self.y+5, 130, 30)

        if self.my_turn:                                                        #set different colors depending on if it is player's turn or not
            color = (240, 80, 217)                  
        else:
            color = (31, 222, 219)

        pygame.Surface.fill(target_surface, (255,255,255), self.rect)
        pygame.draw.rect(target_surface, color, self.rect, 2)       
        my_font = pygame.font.SysFont("Courier", self.fontsize)
        text = my_font.render(str(self.name), True, (0,0,0))        
        target_surface.blit(text, (self.rect.x+5, self.y+10))

    def __lt__(self, other):
        if self.scores.total < other.scores.total:
            return True

    def __gt__(self, other):
        if self.scores.total > other.scores.total:
            return True

    def __eq__(self, other):
        if self.scores.total == other.scores.total:
            return True
 
    def checkoptions(self):
        """Check for the scoring options the player has, considering their roll/kept dice and previous scores."""

        if self.roll == [] and self.kept == []:                                 #if no dice in player's lists, no options checked
            return

        options = []                                                            #create lists to store the scoring options and the values of the dice in roll and kept lists
        results = []

        for i in self.roll:                                                     #append results list with player's dice
            x = i.value
            results.append(x)
        for i in self.kept:
            x = i.value
            results.append(x)
        
        for i in range(1, 7):                                                   #check for multiples of a single die - check if number is in results and add number*count to options
            if i in results:
                if i == 1 and self.scores.ones == 0:
                    val = results.count(i) * i
                    options.append((i-1, val))
                if i == 2 and self.scores.twos == 0:
                    val = results.count(i) * i
                    options.append((i-1, val))
                if i == 3 and self.scores.threes == 0:
                    val = results.count(i) * i
                    options.append((i-1, val))
                if i == 4 and self.scores.fours == 0:
                    val = results.count(i) * i
                    options.append((i-1, val))
                if i == 5 and self.scores.fives == 0:
                    val = results.count(i) * i
                    options.append((i-1, val))
                if i == 6 and self.scores.sixes == 0:
                    val = results.count(i) * i
                    options.append((i-1, val))
        
        for i in results:
            if results.count(i) >= 3:                                           #if a number is in results at least 3 times, add up all numbers in results and add to options
                if self.scores.three_of_a_kind == 0:
                    val = 0
                    for i in results:
                        val += i
                    options.append((7, val))
                    break

        for i in results:
            if results.count(i) >= 4:                                           #if a number is in results at least 4 times, add up all numbers in results and add to options
                if self.scores.four_of_a_kind == 0:
                    val = 0
                    for i in results:
                        val += i
                    options.append((8, val))
                    break

        results.sort()                                                          #sort results to check for next scoring options more easily

        if results.count(results[0]) + results.count(results[4]) == 5:          #if the count for first and last item in results equals 5 and
            if results.count(results[0]) > 1 and results.count(results[4]) > 1: #the count of both is bigger than one, it is a full house. 
                if self.scores.full_house == 0:
                    options.append((9, 25))
                
        if 3 in results and 4 in results:                                       #numbers 3 and 4 are required for small street
            if 1 in results and 2 in results:                                   #check if remaining numbers match requirements for small street
                if self.scores.small_street == 0:
                    options.append((10, 30))
            elif 2 in results and 5 in results:
                if self.scores.small_street == 0:
                    options.append((10, 30))
            elif 5 in results and 6 in results:
                if self.scores.small_street == 0:
                    options.append((10, 30))

        if 2 in results and 3 in results and 4 in results and 5 in results:     #2, 3, 4, 5 required for big street, one of 1 and 6 also needed.
            if 1 in results:
                if self.scores.big_street == 0:
                    options.append((11, 40))
            elif 6 in results:
                if self.scores.big_street == 0:
                    options.append((11, 40))
        
        if results.count(results[0]) == 5:                                      #if a number's count equals 5, it is a kiffel
            if self.scores.kiffel == 0:
                options.append((12, 50))

        if self.scores.chance == 0:                                             #no requirement for chance apart from chance not having been taken yet
            val = 0
            for i in results:
                val += i
            options.append((13, val))    

        return options


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
            
  
def get_names():
    """Function in preparation of the game. Enables players to put in names"""
    
    clock = pygame.time.Clock()                                                                         #set a clock to determine framerate
        
    surface_sz = 1000                                                                                   #set surface size
    main_surface = pygame.display.set_mode((surface_sz, surface_sz))                                    #create a surface

    color = pygame.Color(50, 240, 50)                                                                   #set a color for the continue button
    my_font = pygame.font.SysFont("Courier", 30)                                                        #determine a font

    textpos = (70, 250)                                                                                 #assign two positions for the text above the buttons
    textpos_two = (25, 300)
    boxes = []                                                                                          #create empty list for boxes
    playerlist = []                                                                                     #create empty list for player

    for i in range(1, 7):                                                                               #create 6 boxes, add them to list
        i = Box(i)
        boxes.append(i)

    for index, i in enumerate(boxes):
        if index+1 < len(boxes):
            i.next = boxes[index+1]
        else:
            i.next = boxes[0]


    the_text = my_font.render("Click on a box to enter a Player's name. Click", True, (0,0,0))          #set text above boxes for introductions
    the_text_two = my_font.render("'Continue' to confirm the players and start the game.", True, (0,0,0))
    continue_rect = pygame.Rect(350, 700, 200, 50)                                                      #create rectangle for continue button
    continue_text = my_font.render(" CONTINUE", True, (0,0,0))

    boxes[0].is_active(boxes)
    while True:
        ev = pygame.event.poll()                                                                        #Look for any event
        if ev.type == pygame.QUIT:                                                                      #window close button clicked?
            pygame.quit()                                                                               #quit game
            sys.exit()                                                                                  #exit compiler

        enter = 0
        for i in boxes:
            if enter != 1:                                                                              #check if boxes are clicked
                enter = i.is_clicked(ev, boxes)            

        if ev.type == pygame.MOUSEBUTTONDOWN:                                                           #check if continue is clicked   
            if continue_rect.collidepoint(ev.pos):
                for i in boxes:
                    if i.user_input != "":                                                              #if continue is clicked and a box has an input
                        playerlist.append(i.user_input)                                                 #add input to playerlist
                if playerlist != []:
                    return playerlist                                                                   #return playerlist
                else:
                    boxes[0].status = False
                    boxes[0].is_active(boxes)
                
            
        main_surface.fill((255,255,255))                                                                #background is white

        for i in boxes:                                                                                 #draw boxes
            i.draw(main_surface)     

        pygame.draw.rect(main_surface, color, continue_rect, 2)                                         #draw the rectangle for continue buton
        main_surface.blit(continue_text, (continue_rect.x+5, continue_rect.y+10))                       #blit continue on rectangle      

        main_surface.blit(the_text, textpos)                                                            #blit texts on screen
        main_surface.blit(the_text_two, textpos_two)
        
        pygame.display.flip()                                                                           #flip display
        clock.tick(60)                                                                                  #limit to 60fps


def main(): 
    """Main game loop"""

    pygame.init()                                                                                      #initiealize pygame and set up screen
    clock = pygame.time.Clock()
    surface_sz = 1000
    main_surface = pygame.display.set_mode((surface_sz, surface_sz))
    namelist = get_names()                                                                             #start the games' first screen and get the list of players 
    playerlist = []                                                                                    #create empty playerlist

    
    
    
    for index, item in enumerate(namelist):                                                            #set up the players. 
        if len(namelist) %2 == 0:                                                                      #if there is an even number, the distance from the center of the screenwidth is equal
            posx = 365 - ((len(namelist) - 2) * 75) + (index * 150)
            x = Player(item, posx, index)
            playerlist.append(x)                                                                       #playerlist is appended with each player
        else:
            posx = 440 - ((len(namelist) - 1) * 75) + (index * 150)                                    #if there is an odd number, there is a player in the center of the screen
            x = Player(item, posx, index)
            playerlist.append(x)
    
    rollbutton = Rollbutton()                                                                          #establish rollbutton
    crossbutton = Crossbutton()                                                                        #establish crossbutton

    playerlist[0].my_turn = True                                                                       #it's the first player's turn
    playercount = 1                                                                                    #playercount starts with 1
    turns = 1                                                                                          #number of turns starts with 1

    while True:                                                                                        #start game loop
        if turns < 14:                                                                                 #the game takes 13 turns
            if len(playerlist) == 1:                                                                   #if there is only 1 player, that player remains active and turns are counted after each of their decisions to cross off, or take a score
                if playerlist[0].my_turn == False:  
                    turns += 1
                    playerlist[0].my_turn = True                    
            else:
                if playerlist[playercount-1].my_turn == False:                                         #if the active player's status is set to inactive
                    if playercount % len(playerlist) == 0:                                             #check if a full turn has been played
                        playerlist[0].my_turn = True                                                   #first player is active
                        turns += 1                                                                     #turns increased
                        playercount = 1                                                                #playercount reset
                    else:
                        playerlist[playercount].my_turn = True                                         #else: next player's turn
                        playerlist[playercount].roll = []                                              #Why do I need these two lines? without them, the dice of prev player keep showing for current player
                        playerlist[playercount].kept = []
                        playercount += 1                                                               #playercount increased

        else:                                                                                          #if the end of the game has been reached
            count = 0
            totals = []
            playertotals = []

            while True:                                                                                #Loop for final scores
                ev = pygame.event.poll()   
                if ev.type == pygame.QUIT:  
                    pygame.quit()
                    sys.exit()

                main_surface.fill((0, 200, 255))
             
                                                    
            

                if count < 1:
                    for i in playerlist:     
                        i.my_turn = False                                                               #set status to False for all players
                        i.scores.calc_total()                                                           #calculate total scores for each player
                        totals.append(i.scores.total)
                    totals.sort(reverse=True)
                    playerlist.sort(reverse=True)

                    for index, i in enumerate(playerlist):
                        i.position = index
                        if len(namelist) %2 == 0:                                                       #calculate x-positions according to new position
                            i.x = 365 - ((len(namelist) - 2) * 75) + (index * 150)
                        else:
                            i.x = 440 - ((len(namelist) - 1) * 75) + (index * 150)

                    if len(playerlist) > 3:                                                             #put scoresheets in desired places for final scoring
                        for i in playerlist:
                            if i.position <= len(playerlist)/2:
                                i.x += i.position * 50
                            else:
                                i.y += 350
                                i.x = playerlist[0].x
                                i.x += (i.position - len(playerlist)//2) * 200
                    else:
                        for i in playerlist:
                            i.x += i.position * 50

                    count += 1
                
                for i in playerlist:                                                                     #draw players and scoresheets
                    if i.scores.total == totals[0]:                                                      #if player's total matches the highest total
                        i.scores.won(main_surface, i)                                                    #player won
                        i.draw(main_surface)
                    else:
                        i.draw(main_surface)
                        i.scores.showsheet(main_surface, i)

                pygame.display.flip()
                clock.tick(60)

        ev = pygame.event.poll()    
        if ev.type == pygame.QUIT:  
            pygame.quit()
            sys.exit()

        if ev.type == pygame.MOUSEBUTTONDOWN:
            
            for i in playerlist:
                if i.my_turn:  
                    rollbutton.is_clicked(ev, i)
                    crossbutton.is_clicked(ev, i)

                    for x in i.roll:
                        x.keep(ev)
                        if x.taken:
                            i.kept.append(x)
                            i.roll.remove(x)
                    for x in i.kept:
                        x.keep(ev)
                        if not x.taken and x in i.kept:
                            i.kept.remove(x)  
                            i.roll.append(x)      
                    i.scores.picked(ev, i)

        main_surface.fill((0, 200, 255))

        for i in playerlist:
            if i.my_turn:
                for y in i.kept:
                    y.draw(main_surface)
                for x in i.roll:               
                    x.draw(main_surface)
                    x.rect = pygame.Rect(x.x, x.y, x.size[0], x.size[1])
                
                i.scores.showsheet(main_surface, i)
                
        for i in playerlist:
            i.draw(main_surface)
        
        crossbutton.draw(main_surface)
        rollbutton.draw(main_surface)

        pygame.display.flip()
        clock.tick(60)

    
main ()
