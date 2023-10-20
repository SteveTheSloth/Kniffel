"""This file contains the code for playing one round of Kiffel"""

import random

rng = random.Random () 
def roll ():
    """Roll dice 3 times while being able to chose to keep one or more dice for the next roll"""
    dice = [rng.randrange (1, 6), rng.randrange (1, 6), rng.randrange (1, 6), rng.randrange (1, 6), rng.randrange (1, 6)]
    for i in range(3):
        dice1 = []
        print ("Roll nr {0}:\n".format(i+1), dice)
        if i < 2:
            if input ("Do you want to keep any of your dice? (y/n) ") == "y":
                keepstrng = input ("Which dice do you want to keep for the next roll? (type 2 4 to keep dice two and four. The dice you decided to keep will be moved to the front. ) ")
                keepstrng = keepstrng.split ()
                if len (keepstrng) == 5:
                    print (dice)
                elif len(keepstrng) >= 1:
                    for i in keepstrng:
                        i = int(i)
                        dice1.append (dice[i-1])
                    while len(dice1) < 5:
                        dice1.append (rng.randrange (1,6))
                dice = dice1      
            else: dice = [rng.randrange (1, 6), rng.randrange (1, 6), rng.randrange (1, 6), rng.randrange (1, 6), rng.randrange (1, 6)]  
    return dice
                
#roll ()

def choice (playerscore)

                





    