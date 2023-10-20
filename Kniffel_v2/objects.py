import random

class Players:
    """Objects in here will keep scores for individual players"""

    def __init__(self, name, ones = 0, twos = 0, threes = 0, fours = 0, fives = 0, 
    sixes = 0, bonus = 0, three_of_a_kind = 0, four_of_a_kind = 0, 
    full_house = 0, small_street = 0, big_street = 0, kiffel = 0, 
    chance = 0, total = 0):
        """This will store a list of each player's scores"""
        self.name = name
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
    
    def cross(self):
        """Cross off a scoring option"""
        x = input("What do you want to cross off? (Use scores as stated on the scoresheet: 1 for ones, große Straße for big street...)\t")
        if x == "1":
            self.ones = None
        if x == "2":
            self.twos = None
        if x == "3":
            self.threes = None
        if x == "4":
            self.fours = None
        if x == "5":
            self.fives = None
        if x == "6":
            self.sixes = None
        if x == "Dreierpasch":
            self.three_of_a_kind = None
        if x == "Viererpasch":
            self.four_of_a_kind = None
        if x == "kriegt man immer":
            self.full_house = None
        if x == "kleine Straße":
            self.small_street = None
        if x == "große Straße":
            self.big_street = None
        if x == "Kiffel":
            self.kiffel = None
        else:
            print("Your input did not match the scoresheet. Please try again.")
            self.cross()

    def scores (self):
        self.scores = [self.ones, self.twos, self.threes, self.fours, self.fives, self.sixes, self.bonus, self.three_of_a_kind, 
        self.four_of_a_kind, self.full_house, self.small_street, self.big_street, self.kiffel, 
        self.chance, self.total]

    def __str__(self):
        return """{15}1:\t\t\t{0}\n2:\t\t\t{1}\n3:\t\t\t{2}\n4:\t\t\t{3}\n5:\t\t\t{4}\n6:\t\t\t{5}\nBonus:\t\t\t{6}\nDreierpasch:\t\t{7}\nViererpasch:\t\t{8}\nkriegt man immer:\t{9}\nkleine Straße:\t\t{10}\ngroße Straße:\t\t{11}\nKiffel:\t\t\t{12}\nChance:\t\t\t{13}\nTotal:\t\t\t{14}\n""".format(self.ones, self.twos, self.threes, 
        self.fours, self.fives, self.sixes, self.bonus, self.three_of_a_kind, 
        self.four_of_a_kind, self.full_house, self.small_street, self.big_street, self.kiffel, 
        self.chance, self.total, str(self.name))

    

class dice:

    def __init__(self, score = []):
        self.score = score

    def roll (self, result = []):
        rng = random.Random ()
        nmbr = 5 - len(result) 
        throw = []
        for i in range(nmbr):
            throw.append(rng.randrange(1, 7))
        if len(result) == 0:
            print (throw)
        else:    
            print (result, "(kept dice)\t", throw, "(new roll)")
        x = input("\nIf you want to keep any dice, please type their position seperated by a blank space (1 3 5 for first, third and fifth dice...).\nTo discard all dice and roll again, please type 'n'\t")
        if x == "n":
            return result
        x = x.split()
        if len(x) == 5:
            return throw
        else:
            for i in x:
                c = throw[int(i)-1]
                result.append(c)
            return result
   

    def __str__(self):
        return "[{0}]{1}][{2}][{3}][{4}]".format(self.score[0], self.score[1], self.score[2], self.score[3], self.score[4])    
    
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
    
def main():
    x = int(input("How many players are playing today?\t"))
    playerlist = []
    namelist = []
    rnd_count = 0
    for i in range(x):
        y = input("Please type the name of player number {0}.\t".format(i+1))
        namelist.append(y)
        y = Players()
        playerlist.append(y)

    input("Lets play!")

    while rnd_count < 13:
        for ind, i in enumerate(playerlist):
            c = 0
            result = []
            print(namelist[ind], ". Your turn!")
            go = dice()
            print(i)
            input ("First roll!")
            while len(result) < 5 and c < 3:
                result = go.roll()
                c += 1
                input ("Second roll!")
                result = result + go.roll(result)
                c += 1
                input ("Third roll!")
                result = result + go.roll(result)
                c += 1
            possible_outcomes (result, i.scores())






main()



    


