from scoresheet import *
from dice import *
import pygame
from buttons import *

class Player:
    def __init__(self, name, index, x, y=100, rollcount=0, status=0, nextplayer=None, dice=None, rolled=None, kept=None, scores=None, myturn=False):
        self.name = name
        self.index = index
        self.x = x
        self.y = y
        self.rollcount = rollcount
        self.status = status    # NEEDED??? Status 0 indicates rolling/picking while status 1 indicates crossing. 
        self.nextplayer = nextplayer
        self.dice = dice
        if self.dice == None: self.dice = dict()
        self.rolled = rolled
        if self.rolled == None: self.rolled = dict()
        self.kept = kept
        if self.kept == None: self.kept = dict()
        self.scores = scores
        if self.scores == None:
            self.scores = Scoresheet(self)
        self.myturn = myturn
        
        
    def roll(self):
        if self.rollcount == 0:
            for i in range(1, 6):
                newdie = Dice(i)
                self.dice[i] = self.rolled[i] = newdie
                newdie.roll_one()
            self.rollcount += 1
        else:
            for value in self.scores.scores.values():
                value.dismiss_option()
            for die in self.rolled.values():
                if die.wait >= 30:
                    die.wait = 2
            self.rollcount += 1
            
    def keep(self, die):
        if die in self.rolled.values():
            self.kept[die.index] = self.rolled.pop(die.index)
        elif die in self.kept.values():
            self.rolled[die.index] = self.kept.pop(die.index)
        
    def display_options(self):
        self.options = list()
        for die in self.rolled.values():
            self.options.append(die.value)
        for die in self.kept.values():
            self.options.append(die.value)
        for value in self.scores.scores.values():
            if value.active == True:
                value.potential_score(self.options)
            
    def display_cross_options(self):
        if self.status == 1:
            for value in self.scores.scores.values():
                if value.active == True:
                    value.potential_cross()
    
    def reset_cross(self):
        for value in self.scores.scores.values():
            if value.value != "X" and value.displayvalue == "X":
                value.displayvalue = value.value
                self.display_options()
                    
            
    def draw(self, target_surface):
        self.namebox = Textfield(self.x + self.index * 50, self.y-50, 185, 30, str(self.name), 20)
        self.scores.draw(target_surface)
        if self.myturn:
            self.namebox.bordercolor = pygame.Color(255, 0, 0)
        else:
            self.namebox.bordercolor = pygame.Color(0,0,0)
        self.namebox.draw(target_surface)
        
        
    def end_turn(self):
        self.scores.reset_displayvalues()
        self.dice.clear()
        self.rolled.clear()
        self.kept.clear()
        self.options.clear()
        self.rollcount = 0
        self.myturn = False
    
    def __gt__(self, other):
        return self.scores.scores["total"].value > other.scores.scores["total"].value
    
    def __lt__(self, other):
        return self.scores.scores["total"].value < other.scores.scores["total"].value
    
    def __eq__(self, other):
        return self.scores.scores["total"].value == other.scores.scores["total"].value
             
            
    
        
            
        
        
    
        
            
            
            
class Player_Old:
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