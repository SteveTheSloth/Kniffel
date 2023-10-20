"""This file keeps the scores of each player in a list. Therefore we need to put in player names and use these names as identifiers for lists that will keep track of individual scores"""
import copy

        
players = []
scores = []
scoresheet = [1, 2, 3, 4, 5, 6, "bonus", "dreierpasch", "viererpasch", "full house", "small street", "big street", "kiffel", "chance"]

def make_lists ():
    """This needs to run the entire time, because we need to change the scores of each list"""
    nr_of_players = int(input("How many players are kiffeling today? "))
    for i in range(nr_of_players):
        name = input ("Enter name for player {0}:  ".format(i+1))
        name = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        scores.append(name) 
    print (scores)

#make_lists ()


def create_lists ():
    count = 0
    names = []
    while True:
        if count > 1:
            print ("If this was your last player, please press enter.")
        count += 1 
        name = input("Please enter name for player {0}: ". format({count}) + "\n")
        if name == "":
            return names
        names.append(name)
        print (names)
    

#players = create_lists ()
for nr, name in enumerate(players):
    print (name)
    name = list
    

for i in range(len(players)):
    players[i]

#print (players)

def possible_outcomes (dicelist, playerscore):
    """Checks for possible scores considering the roll and that player's score"""
    possibilities = []
    x = []
    position = ""
    for i in range(6):      #Check for multiples of single numbers
        if playerscore[i] == 0 and dicelist.count(i+1) >= 1:
            result = (i+1) * dicelist.count(i+1)
            print ("You can take the added {0}s for".format (i+1), result, "points.")
            possibilities.append ((result, "for {0}s".format (i+1)))
            position += str(i+1) + " "
    for i in range(6):      #Check for three of a kind
        if playerscore[8] == 0 and dicelist.count(i+1) >= 3:
            result = sum(dicelist)
            print ("You can take three of a kind of {0}s for".format(i+1), result, "points.")
            possibilities.append ((result, "three of a kind ({0}s)".format(i+1)))
            position += "8 "
    for i in range(6):      #Check for four of a kind        
        if playerscore[9] == 0 and dicelist.count(i+1) >= 4:
            result = sum(dicelist)
            print ("You can take four of a kind of {0}s for ".format(i+1), result, "points.")
            possibilities.append ((result, "four of a kind ({0}s)".format (i+1)))
            position += "9 "
    for i in range(6):      #Check for full house
        if playerscore[10] == 0 and dicelist.count(i+1) >= 2:
            result = 25
            y = [1]
            y *= dicelist.count (i+1)
            x += y
            if len (x) == 5:
                print ("You can take your kriegt man immer for 25 points.")
                possibilities.append ((result, "kriegt man immer"))      
                position += "10 "         
    if playerscore [11] == 0 and 3 in dicelist and 4 in dicelist:
        result = 30         #Check for small street 
        if (1 in dicelist and 2 in dicelist) or (2 in dicelist and 5 in dicelist) or (5 in dicelist and 6 in dicelist):
            print ("You can take your small street for 30 points.")
            possibilities.append ((result, "small street"))
            position += "11 "
    if playerscore [12] == 0 and 2 in dicelist and 3 in dicelist and 4 in dicelist and 5 in dicelist:
        if 1 in dicelist:   #Check for big street
            result = 40
            print ("You can take your big street for 40 points.")
            possibilities.append ((result, "big street"))
            position += "12 "
        elif 6 in dicelist:
            result = 40
            print ("You can take your big street for 40 points.")
            possibilities.append ((result, "big street"))
            position += "12 "
    if playerscore [13] == 0:   #Check for kiffel
        for i in range (6):
            if dicelist.count (i+1) == 5:
                result = 50
                print ("You can take your KIFFEL for 50 points.")
                possibilities.append ((result, "KIFFEL"))
                position += "13 "
    if playerscore [14] == 0:   #Check for chance
        result = sum(dicelist)
        print ("You can take your chance for ", result, "points.")
        possibilities.append ((result, "chance"))
        position += "14 "
    print (possibilities)
    return possibilities, position


            
dice = [2, 4, 3, 5, 6]
playerscore = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                
possible_outcomes(dice, playerscore)

def choice (possibilities, position, playerscore):
    """Let the players chose which of the scoring option they choose and put them in the right place in their scoresheet"""
    position = position.split()
    i = int(input("Which scoring option do you choose? (1 for first option, 2 for second option... "))-1
    x = position[i]
    chosen = possibilities[i][0]
    playerscore = playerscore [:x] + chosen + playerscore [x+1:]


