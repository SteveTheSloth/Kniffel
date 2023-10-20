import random
players = []
scores = []
scoresheet = [1, 2, 3, 4, 5, 6, "bonus", "dreierpasch", "viererpasch", "full house", "small street", "big street", "kiffel", "chance"]


rng = random.Random () 
def roll ():
    """Roll dice 3 times while being able to chose to keep one or more dice for the next roll"""
    dice = [rng.randrange (1, 7), rng.randrange (1, 7), rng.randrange (1, 7), rng.randrange (1, 7), rng.randrange (1, 7)]
    for i in range(3):
        dice1 = []
        print ("Roll nr {0}:\n".format(i+1), dice)
        if i < 2:
            if input ("Do you want to keep any of your dice? (y/n) ") == "y":
                keepstrng = input ("Which dice do you want to keep for the next roll? (type 2 4 to keep dice two and four. The dice you decided to keep will be moved to the front.) ")
                keepstrng = keepstrng.split()
                if len (keepstrng) == 5:
                    print (dice)
                    return (dice)
                elif len(keepstrng) >= 1:
                    for i in keepstrng:
                        i = int(i)
                        dice1.append (dice[i-1])
                    while len(dice1) < 5:
                        dice1.append (rng.randrange (1,6))
                dice = dice1      
            else: dice = [rng.randrange (1, 7), rng.randrange (1, 7), rng.randrange (1, 7), rng.randrange (1, 7), rng.randrange (1, 7)]  
    return dice

def possible_outcomes (dicelist, playerscore):
    """Checks for possible scores considering the roll and that player's score"""
    possibilities = []
    x = []
    position = ""
    for i in range(6):      #Check for multiples of single numbers
        if playerscore[i] == 0 and dicelist.count(i+1) >= 1:
            result = (i+1) * dicelist.count(i+1)
            print ("You can take the added {0}s for".format (i+1), result, "points.")
            possibilities.append ((result, "for {0}s".format (i+1), i))
    for i in range(6):      #Check for three of a kind
        if playerscore[7] == 0 and dicelist.count(i+1) >= 3:
            result = sum(dicelist)
            print ("You can take three of a kind of {0}s for".format(i+1), result, "points.")
            possibilities.append ((result, "three of a kind ({0}s)".format(i+1), 7))
    for i in range(6):      #Check for four of a kind        
        if playerscore[8] == 0 and dicelist.count(i+1) >= 4:
            result = sum(dicelist)
            print ("You can take four of a kind of {0}s for ".format(i+1), result, "points.")
            possibilities.append ((result, "four of a kind ({0}s)".format (i+1), 8))
    for i in range(6):      #Check for full house
        if playerscore[9] == 0 and dicelist.count(i+1) >= 2:
            result = 25
            y = [1]
            y *= dicelist.count (i+1)
            x += y
            if len (x) == 5:
                print ("You can take your kriegt man immer for 25 points.")
                possibilities.append ((result, "kriegt man immer", 9))             
    if playerscore [10] == 0 and 3 in dicelist and 4 in dicelist:
        result = 30         #Check for small street 
        if (1 in dicelist and 2 in dicelist) or (2 in dicelist and 5 in dicelist) or (5 in dicelist and 6 in dicelist):
            print ("You can take your small street for 30 points.")
            possibilities.append ((result, "small street", 10))
    if playerscore [11] == 0 and 2 in dicelist and 3 in dicelist and 4 in dicelist and 5 in dicelist:
        if 1 in dicelist:   #Check for big street
            result = 40
            print ("You can take your big street for 40 points.")
            possibilities.append ((result, "big street", 11))
        elif 6 in dicelist:
            result = 40
            print ("You can take your big street for 40 points.")
            possibilities.append ((result, "big street", 11))
    if playerscore [12] == 0:   #Check for kiffel
        for i in range (6):
            if dicelist.count (i+1) == 5:
                result = 50
                print ("You can take your KIFFEL for 50 points.")
                possibilities.append ((result, "KIFFEL", 12))
    if playerscore [13] == 0:   #Check for chance
        result = sum(dicelist)
        print ("You can take your chance for ", result, "points.")
        possibilities.append ((result, "chance", 13))
    print (possibilities)
    return possibilities   


def choice (possibilities, playerscore):
    """Let the players choose which of the scoring option they choose and put them in the right place in their scoresheet"""
    i = int(input("Which scoring option do you choose? (1 for first option, 2 for second option... "))-1
    x = possibilities[i][2]
    chosen = [possibilities[i][0]]
    playerscore = playerscore [:x] + chosen + playerscore [x+1:]
    print (playerscore)
    return playerscore


def scoring (scores):
    for i in range(nr_of_players):
        upper = scores [i][:6]
        upper_sum = sum(upper)
        if upper_sum >= 63:
            upper_sum += 35
        result = upper_sum + sum(scores[i][7:])
    print (players[i], "'s final score is ", result)


nr_of_players = int(input("How many players are kiffeling today? "))
for i in range(nr_of_players):
    name = input ("Enter name for player {0}:  ".format(i+1))
    players.append(name)
    name = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    scores.append(name) 
print (scores, players)

for i in range (13):
    #The game has 13 rounds for each player
    for i in range(nr_of_players):
        #we cycle through the players fo each round
        print ("It's", players[i], "'s turn!")
        dice = roll()
        possible = possible_outcomes (dice, scores[i])
        
        scores [i] = choice (possible, scores[i])

scoring (scores)


    
        




