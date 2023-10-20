import pygame
import random

class Dice:
    def __init__(self, index=0, value=None, posn=None, taken=False, x=0, y=0, wait=2):
        """Create a dice object that stores its value (random number between 1 and 6), an index that determines its relative position to the four other dice,
        the sprite-sheet of 6 dice, its position on that sheet as determined by its value, the sprite size, its position on the screen, its rectangle, a taken value, 
        signifying if the die is kept for next roll or rolled again and an index i used to determine the end of the rolling-animation probably unnecessary: wait"""
        self.spritesheet = pygame.image.load("dice.jpg")                      #load sprite-sheet                      #get height of single sprite (== height of sprite-sheet)
        self.index = index
        self.value = value                                 
        self.size = (self.spritesheet.get_width()//6, self.spritesheet.get_height())                               #size is tuple determined by single sprite
        self.posn = posn
        self.x = x 
        self.y = y
        self.taken = taken
        self.wait = wait
        
    def draw(self, target_surface):
        self.x = self.size[0]*self.index + 30*self.index                        #determine position on screen
        if self.taken: 
            self.y = 500
            target_surface.blit (self.spritesheet, (self.x, self.y), self.cutsprite())
            return
        else: self.y = 600                                                                 #length of animation is set to 27
        target_surface.blit (self.spritesheet, (self.x, self.y), self.cutsprite())
        
        
    def roll_animation(self):
        ANIMLEN = 30
        if self.wait % 2 == 0 and self.wait < ANIMLEN:                                 #as long as parameter i is smaller than length of animation and 3 frames have passed, value is changed
            self.roll_one()                                                        #determine position on spritesheet for changed value
            self.wait += 1    
        elif self.wait % 2 != 0 and self.wait < ANIMLEN:                               #if i smaller than animlen and 3 frames have not passed, display same sprite
            self.wait += 1
        elif self.wait >= ANIMLEN:
            return
            
            
    def roll_one(self):
        """Give one die a random value between 1 and 6."""
        rng = random.Random()                                                       #create new random object
        self.value = rng.randrange(1, 7)                                            #set new value between 1 and 6
        self.posn = (self.size[0]*(self.value-1), 0)                                #change sprite-position according to new value
        
    def cutsprite (self):
        """Get single sprite coordinates and size."""
        dice_sprite = (self.posn[0], self.posn[1], self.size[0], self.size[1])
        return dice_sprite

    def is_clicked(self, event):
        """Check if die has been clicked."""
        rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])
        if rect.collidepoint(event.pos): 
            self.taken = not self.taken
            return True 
        else: 
            return False 
        
    def __gt__(self, other):
        return self.value > other.value
    
    def __lt__(self, other):
        return self.value < other.value
    
    def __eq__(self, other):
        return self.value == other.value
        
        
        

class Dice_Old:
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
        ANIMLEN = 27                                                                #length of animation is set to 27
        if self.wait % 3 == 0 and self.i < ANIMLEN:                                 #as long as parameter i is smaller than length of animation and 3 frames have passed, value is changed
            self.rndval = rng.randrange(1, 7)                                       #change value of sprite
            self.posn = (self.size[0]*(self.rndval-1), 0)                           #determine position on spritesheet for changed value
            target_surface.blit (self.img, (self.x, self.y), self.cutsprite())      #blit sprite on surface
            self.i += 1                                                             #increase i until length of animation reached
            self.wait += 1
            return
        elif self.wait % 3 != 0 and self.i < ANIMLEN:                               #if i smaller than animlen and 3 frames have not passed, display same sprite
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
        rng = random.Random()                                                       #create new random object
        self.i = 0                                                                  #set index i to 0 to start new animation
        self.value = rng.randrange(1, 7)                                            #set new value between 1 and 6
        self.posn = (self.size[0]*(self.value-1), 0)                                #change sprite-position according to new value
        self.x = self.size[0]*self.index + 50*(self.index+2)                        #determine position on screen
        self.y = 600 
        
    def __str__(self):
        """Make Die-Value printable"""
        return(str(self.value))