import pygame
from buttons import *

class ScoreOption(ClickButton):
    def __init__(self, x, y, width, height, name, fontsize, condition, active=True, status=0, value=0, displayvalue=0):
        self.name = name
        self.active = active
        self.displayvalue = displayvalue
        self.condition = condition
        self.value = value
        text = str(self.name) + ":" + " "*(18-len(name) - len(str(self.displayvalue))) + str(self.displayvalue)
        super().__init__(x, y, width, height, text, fontsize, (255,255,255), nextbutton=None, status=status)
        
        
    def draw_border(self, target_surface):
        if self.status == 0:
            pygame.draw.rect(target_surface, (255, 255, 255), self.rect, 2)
        if self.status == 1:    # Status 1 indicates a pickable option.
            pygame.draw.rect(target_surface, (255, 0, 0), self.rect, 2)
        if self.status == 2:    # Status 2 indicates a crossable option.
            pygame.draw.rect(target_surface, (140, 0, 255), self.rect, 2)
            
    def potential_score(self, roll_result):
        if self.value == 0:
            if self.condition(roll_result) != None and self.condition(roll_result) != 0: 
                self.displayvalue = self.condition(roll_result) 
                self.status = 1
            else:
                self.status = 0
                
    def take_option(self):
        if self.value == 0 and self.displayvalue != 0:
            self.value = self.displayvalue
            self.status = 0
             
    def dismiss_option(self):
        if self.value == 0 and self.displayvalue != 0:
            self.displayvalue = 0
            self.status = 0
    
    def cross_option(self):
        if self.value == 0:
            self.displayvalue = self.value = "X"
            self.status = 0  
            
    def potential_cross(self):
        if self.value == 0:
            self.status = 2
            self.displayvalue = "X"

class Scoresheet:
    def __init__(self, player=None, scores=None, top=None, bottom=None, length=12):
        self.player = player
        self.scores = scores
        if self.scores == None: self.scores = dict()
        self.top = top
        if self.top == None: self.top = dict()
        self.bottom = bottom
        if self.bottom == None: self.bottom = dict()
        self.length = length
        self.rect = pygame.Rect(self.player.x + self.player.index * 50, self.player.y, 185, 300)   
        
    def numbers(self, i):
        return lambda result: sum([x for x in result if x == i and result.count(i) > 0])
        
            
    def bonus(self):
        if self.total_top() >= 63:
            return 35
            
    def total_top(self):
        x = 0
        for value in self.scores.values():
            if "total" in value.name:
                break
            elif value.value != "X": x += value.value
        return x          
        
    def three_of_a_kind(self, result):
        for i in result:
            if result.count(i) >= 3:
                return sum(result)
        
    def four_of_a_kind(self, result):
        for i in result:
            if result.count(i) >= 4:
                return sum(result)
            
    def full_house(self, result):
        result.sort()
        if result.count(result[0]) >= 2 and result.count(result[4]) >= 2 and result.count(result[0]) + result.count(result[4]) == 5:
            return 25
        
    def small_street(self, result):
        result.sort()
        if len(([x for i, x in enumerate(result) if i < 4 and x + 1 == result[i + 1] or 3 <= i <= 4 and x - 1 == result[i - 1]])) >= 4:
            return 30
        
        
    def big_street(self, result):
        result.sort()
        if len(([x for i, x in enumerate(result) if i < 4 and x + 1 == result[i + 1] or 3 <= i <= 4 and x - 1 == result[i - 1]])) == 5:
            return 40
        
    def kniffel(self, result):
        if len([x for x in result if x == result[0]]) == 5:
            return 50
    
    def chance(self, result):
        return sum(result)
    
    def total(self):
        x = 0
        for value in self.scores.values():
            if type(value.value) == type(1) and "total" not in value.name: x += value.value
        return x     
    
    def add_conditional_scoring_option_top(self, name, condition):
        key = len(self.scores) + 1
        self.top[key] = self.scores[key] = ScoreOption(self.player.x + self.player.index * 50, self.player.y + 320/16*(key-1), 190, 320/16, name, 15, condition)
        
    def add_conditional_scoring_option_bottom(self, name, condition):
        key = len(self.scores) + 1
        self.bottom[key] = self.scores[key] = ScoreOption(self.player.x + self.player.index * 50, self.player.y + 320/16*(key-1), 190, 320/16, name, 15, condition)
        
    def add_self_calculating_score(self, name, condition):
        key = len(self.scores) + 1
        self.scores[name] = ScoreOption(self.player.x + self.player.index * 50, self.player.y + 320/16*(key-1), 190, 320/16, name, 15, condition, False)
        
    def set_up_standard_scoring_options(self):
        names = ["ones", "twos", "threes", "fours", "fives", "sixes"]
        for i in range (1, 7):
            self.add_conditional_scoring_option_top(names[i-1], self.numbers(i))
        self.add_self_calculating_score("total top", self.total_top)
        self.add_self_calculating_score("bonus", self.bonus)
        self.add_conditional_scoring_option_bottom("three of a kind", self.three_of_a_kind)
        self.add_conditional_scoring_option_bottom("four of a kind", self.four_of_a_kind)
        self.add_conditional_scoring_option_bottom("full house", self.full_house)
        self.add_conditional_scoring_option_bottom("small street", self.small_street)
        self.add_conditional_scoring_option_bottom("big street", self.big_street)
        self.add_conditional_scoring_option_bottom("kniffel", self.kniffel)
        self.add_conditional_scoring_option_bottom("chance", self.chance)
        self.add_self_calculating_score("total", self.total)           
        
    def reset_displayvalues(self):
        for value in self.scores.values():
            if value.active == True and (value.value != value.displayvalue):
                value.displayvalue = value.value
                value.status = 0
                value.text = str(value.name) + ":" + " "*(18-len(value.name) - len(str(value.displayvalue))) + str(value.displayvalue)
                
    def calculate_dependant_scores(self):
        self.scores["total top"].displayvalue = self.scores["total top"].value = self.total_top()
        if self.scores["total top"].value >= 63:
            self.scores["bonus"].value = 35
        
    def calculate_total(self):
        self.scores["total"].displayvalue = self.scores["total"].value = self.total()
            
    def __str__(self):  # Probably not needed.
        scorelist = list()
        scorestring = str()
        for value in self.scores.values():
            scorelist.append((value[0], value[2]))
        for i in scorelist:
            scorestring += str(i[0]) + ":" + " "*(18-len(i[0])-len(i[2])) + (str(i[2])) + ","
        return scorestring
            
     
    def draw(self, target_surface):                 
        for value in self.scores.values():
            value.text = str(value.name) + ":" + " "*(18-len(value.name) - len(str(value.displayvalue))) + str(value.displayvalue)
            value.draw(target_surface)
            value.draw_border(target_surface)
            
        
        
        
    
    
    
    
class Scoresheet_old:
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