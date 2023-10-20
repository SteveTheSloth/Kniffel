"""This module is the model part of the Kniffel game. It contains the representation of the data that is used. It can handle requests by the controller and return data based on the 
given request/input."""
import random
from itertools import combinations
from openpyxl import load_workbook

class Player:
    def __init__(
        self, name, index, active=False, mydice=None, scored=None, rollcount=0
    ):
        self.name = name
        self.index = index
        self.active = active
        if self.index == 0:
            self.active = True
        self.mydice = mydice
        if self.mydice == None:
            self.mydice = list()
        self.scored = scored
        if self.scored == None:
            self.scored = dict()
        self.rollcount = rollcount

    def total_top(self):
        """Calculate sum of a player's top section and bonus."""
        total = 0
        for i in range(1, 7):
            x = self.scored.get(i, 0)
            try:
                if type(x[0]) == type(1):
                    total += x[0]
            except TypeError:
                continue
        if total >= 63:
            self.scored[8] = (35, "bonus")
        else: self.scored[8] = (0, "bonus")
        self.scored[7] = (total, "total top")
        
    def total(self):
        """Calculate sum of player's scores."""
        total = 0
        for i in self.scored.keys():
            if i not in [7, 16]:
                x = self.scored.get(i, 0)
                try:
                    if type(x[0]) == type(1):
                        total += x[0]
                except TypeError:
                    continue
        self.scored[16] = (total, "total")

    def roll(self):
        """Change dice value of dice that are not marked as kept. Maximum of three rolls per turn."""
        if self.rollcount >= 3:
            return
        if len(self.mydice) == 0:
            for i in range(5):
                x = Dice(i)
                self.mydice.append(x)
                x.roll()
            self.rollcount += 1
        else:
            for i in self.mydice:
                i.roll()
            self.rollcount += 1

    def change_status(self):
        """Set player status to active."""
        self.active = not self.active

    def keep(self, die):
        """Set die status to kept/unkept."""
        die.keep()

    def options_take(self):
        """Return player's options to take a scoring options depending on their roll."""
        options = dict()
        scoreoptions = Scoresheet.standard_scores()
        for key, value in scoreoptions.items():
            if key not in self.scored:
                if value[0](throw := [x.value for x in self.mydice]) != 0:
                    options[key] = (value[0](throw), value[1])
        return options

    def options_cross(self):
        """Return player's options to cross-off a scoring options."""
        options = dict()
        scoreoptions = Scoresheet.standard_scores()
        for key, value in scoreoptions.items():
            if key not in self.scored and key not in [7, 8, 16]:
                options[key] = ("X", value[1])
        return options

    def change_scored(self, entry):
        """Change a scoring option to a new value (points/X)."""
        self.scored[entry[0]] = (entry[1], entry[2])

    def clear(self):
        """Clear a player's data before next turn."""
        self.mydice.clear()
        self.rollcount = 0

    def __gt__(self, other):
        return self.scored[16][0] > other.scored[16][0]

    def __lt__(self, other):
        return self.scored[16][0] < other.scored[16][0]

    def __eq__(self, other):
        return self.scored[16][0] == other.scored[16][0]
    
    
"""class Autoplayer(Player):
    def __init__(self):
        super().__init__("auto", 0)
        self.indexoptions()
        self.rolldict = dict()
        
        
    def indexoptions(self):
        indexes = list(range(5))
        self.indexcombinations = []
        for i in range(1, 6):
            self.indexcombinations.extend(list(combinations(indexes, i)))

    def chooseindex(self):
        x = random.randrange(0, len(self.indexcombinations))
        return self.indexcombinations[x]
        
    def save_roll(self):
        for i in range(1000):
            self.roll()
            firstroll = [x.value for x in self.mydice]
            index = self.chooseindex()
            for i in self.mydice:
                if i.index in index:
                    i.kept = False
                else:
                    i.kept = True
            notkept = dict()
            changedvalue = [firstroll[k] for k in index]
            changedvalue.sort()
            changedvalue = tuple(changedvalue)
            self.roll()
            secondroll = [i.value for i in self.mydice]
            secondroll.sort()
            secondroll = tuple(secondroll)
            potentialpoints = self.options_take()
            newrolls = dict()
            newrolls[secondroll] = [potentialpoints, 1]
            notkept[changedvalue] = [newrolls, 1]
            firstroll.sort()
            firstroll = tuple(firstroll)
            if firstroll not in self.rolldict:
                self.rolldict[firstroll] = [notkept, 1]
            else:
                self.rolldict[firstroll][1] += 1
                if changedvalue not in self.rolldict[firstroll][0]:
                    self.rolldict[firstroll][0][changedvalue] = [newrolls, 1]
                else:
                    self.rolldict[firstroll][0][changedvalue][1] += 1
                    if secondroll not in self.rolldict[firstroll][0][changedvalue][0]:
                        self.rolldict[firstroll][0][changedvalue][0][secondroll] = [potentialpoints, 1]
                    else:
                        self.rolldict[firstroll][0][changedvalue][0][secondroll][1] += 1     
            self.clear()"""
            
        
class Autokniffel(Player):
    has_taken = False
    
    
    def check_roll(self):
        self.rollvalues = dict()
        throw = self.throw = [x.value for x in self.mydice]
        for key, value in Scoresheet.standard_scores().items():
            if key not in self.scored and key not in [7, 8, 16]:
                if value[0](throw) != 0:
                    self.rollvalues[key] = (value[0](throw := [x.value for x in self.mydice]))
        self.check_take()
        
    def check_take(self):
        self.calc_top_diff()
        self.check_take_kniffel()
        self.check_take_big_street()
        if self.rollcount == 3:   # Check options according to priorities if already rolled 3 times
            self.rollcount_3()
        else: 
            self.multiples_in_roll()
            
    def calc_top_possible(self):
        keys = list()
        for i in range(1, 7):
            if i not in self.scored:
                keys.append(i)
        if self.difference * (sum(list(map(lambda x: x*3, keys)))/sum(keys)) >= 3:
            return True
        elif self.difference * (sum(list(map(lambda x: x*4, keys)))/sum(keys)) >= 3:
            return True
        else:
            return False
         
    def calc_top_diff(self):
        points = 0
        keys = 0
        for i in range(1, 7):
            if i in self.scored:
                if self.scored[i][0] != "X":
                    points += self.scored[i][0]
                keys += i
        if keys != 0:
            self.difference = points/keys
        else: self.difference = 3
    
    
    def check_take_kniffel(self):
        if 14 in self.rollvalues:
            kniffel = (14, self.rollvalues[14], Scoresheet.standard_scores()[14][1])
        else:
            return
        if self.throw[0] in self.scored:  
            self.change_scored(kniffel)  
            self.has_taken = True
            return
        elif self.throw[0] not in self.scored and self.difference > 3:
            self.change_scored(kniffel)
            self.has_taken = True
            return
        elif self.throw[0] not in self.scored and self.difference == 3 and self.throw[0] < 4:
            self.change_scored(kniffel)
            self.has_taken = True
            return
        elif self.calc_top_possible == False:
            self.change_scored(kniffel)
            self.has_taken = True
            return
        
    def check_take_big_street(self):
        if 13 in self.rollvalues:
            self.change_scored((13, self.rollvalues[13], Scoresheet.standard_scores()[13][1]))  
            self.has_taken = True
            return
            
    def multiples_in_roll(self):
        sthrow = set(self.throw)
        self.valamounts = list()
        for i in sthrow:
            self.valamounts.append((i, self.throw.count(i)))
        self.valamounts.sort(reverse=True)
        self.valamounts.sort(key = lambda y: y[1], reverse=True)         # Get Tuples of Value, amount sorted by amount (high to low) and value (high to low)
        
        if self.difference <= 3:
            for i, am in self.valamounts:
                if i not in self.scored:
                    self.goformultiples(i)
                    return
                
        for i, am in self.valamounts:
            if i != 1 and i in self.rollvalues:
                self.goformultiples(i)
                return
                        
        self.check_multiples()
                    
    def check_multiples(self):    
        for i, am in self.valamounts:
            if am == 4 and 14 not in self.scored:
                self.goformultiples(i)
            elif am == 4 and 14 in self.scored and any([9, 10]) not in self.scored:
                self.keep_and_highest(i)
            elif am == 3:
                if 11 in self.rollvalues:
                    if all([ x:= self.valamounts[0][0], y := self.valamounts[1][0]]) <= 3 or all ([x, y]) in self.scored:
                        self.change_scored((11, 25, "full house"))
                        self.has_taken = True
                        return        
                self.calc_kinds(i)
            elif am == 2 and len(self.valamounts) == 3 and all([self.valamounts[0][1], self.valamounts[1][1]]) == 2:
                if all([2, 3, 4]) in self.throw or all([3, 4, 5]) in self.throw:
                    if 12 not in self.scored:
                        self.goforstreet()
                elif 11 not in self.scored and (all(self.valamounts[0][0], self.valamounts[1][0]) <= 3 or all([9, 10]) in self.scored):
                    self.goforfullhouse()
            elif am == 2:
                if i >= 4 and 9 not in self.scored:
                    self.goformultiples(i)
                elif 12 not in self.scored and len([x for x in self.throw if x in [2, 3, 4, 5]]) >= 3 or 13 not in self.scored and all([2, 3, 4, 5]) in self.throw:
                    self.goforstreet()
            else: self.goforstreet()
                
 
    def keep_and_highest(self, keepval):
        for i in self.mydice:
            if i.value == keepval:
                i.kept = True
            elif i.value >= 4:
                i.kept = True
        return
                    
    def calc_kinds(self, i):
        if 15 not in self.scored and any([9, 10, 14]) not in self.scored and i >= 4:
            self.goformultiples(i)
            return
        elif all([9, 10]) not in self.scored and (i >= 4 or len(self.scored) > 10):
            self.goformultiples(i)    
            return
        elif all([10, 15]) not in self.scored and i >= 4:
            self.goformultiples(i)
            return
        elif any([9, 10]) not in self.scored and (i >= 4 or len(self.scored) > 10):
            self.goformultiples(i)
            return
        
                    
            
            
    """def roll_for_what(self):
        
                    
        elif self.difference <= 3:
            i, am = valamounts[0]
            if am != 4 and not (all(item in [x[0] for x in valamounts] for item in [2, 3, 4, 5]) and 13 not in self.scored):
                for i in range(6, 0, -1):
                    if i not in self.scored:
                        self.goformultiples(i)
                        return
        
        elif self.difference <= 3 and sum(self.throw) <= 18:
            for i in range(6, 0, -1):
                if i not in self.scored:
                    self.goformultiples(i)
                    return
                    
        
        for i, am in valamounts:
            if am == 4: # If 4 of a kind rolled
                
                if i >= 4 and 10 not in self.scored or any([i, 14]) not in self.scored: # If value >= 4
                    self.goformultiples(i)
                    return
                elif i < 4 and i in self.scored and 10 not in self.scored or 11 not in self.scored and len(self.scored) >= 12:
                    self.goformultiples(i)
                    return
                elif all(item in self.scored for item in [i, 9, 10, 11, 14, 15]):
                    self.goforstreet()
                    return
                else:
                    self.goforhighscore()
                    return
            elif am == 3:
                if Scoresheet.standard_scores()[11][0](self.throw) != 0:
                    if i in self.scored:
                        self.change_scored((11, 25, "full house"))
                        self.has_taken = True
                        return
                    elif i not in self.scored and self.difference <= 3:
                        self.goformultiples(i)
                        return
                if (i >= 4 and any ([9, 10]) not in self.scored and self.difference > 3) or i not in self.scored:
                    self.goformultiples(i)
                    return
                elif i < 4 and i in self.scored and any([9, 10]) not in self.scored and len(self.scored) >= 10 and self.difference > 3:
                    self.goformultiples(i)
                    return
                elif 11 not in self.scored:
                    self.goforfullhouse()
                    return
            elif 12 in self.rollvalues:
                self.goforstreet()
                return
            elif 12 not in self.scored and all(item in self.throw for item in [2, 3, 4]):
                self.goforstreet()
                return
            elif am == 2:
                if len(twotimes := [twice for twice in valamounts if twice[1]==2]) > 1:
                    for j, jam in twotimes:
                        if j not in self.scored or (j >= 5 and 9 not in self.scored and self.difference >3):
                            self.goformultiples(j)
                            return
                    if 11 not in self.scored:
                        self.goforfullhouse()
                        return
                if i not in self.scored or (10 not in self.scored and len(self.scored) >= 10) or (all(item in self.scored for item in [12, 13])):
                    self.goformultiples(i)
                    return
                else:
                    self.goforstreet()
                    return
            else:
                if any([12, 13]) not in self.scored:
                    self.goforstreet()
                    return
                else:
                    self.goforhighscore()
                    return"""

                        
    def rollcount_3(self):
        
        for i in  range(6, 0, -1):
            if i in self.rollvalues:  # Check if potential good top-option
                option = (i, value := self.rollvalues[i], Scoresheet.standard_scores()[i][1])
                if (3*i <= value and self.difference >= 3) or (self.difference <= 3 and self.difference * (value/(i*3)) >= 3):   # Take top if amount of dicevalues >= 3 & <= 5 or kniffel already taken or possibility to make up for lack of points top
                    self.change_scored(option)
                    self.has_taken = True
                    return
        if 10 in self.rollvalues:
            if self.rollvalues[10] >= 20:
                self.change_scored((10, self.rollvalues[10], Scoresheet.standard_scores()[10][1]))
                self.has_taken = True
                return
        elif 11 in self.rollvalues:
            self.change_scored((11, 25, Scoresheet.standard_scores()[11][1]))
            self.has_taken = True
            return
        elif 12 in self.rollvalues:
            self.change_scored((12, 30, Scoresheet.standard_scores()[12][1]))
            self.has_taken = True
            return
        elif 9 in self.rollvalues:
            if self.rollvalues[9] >= 20:
                self.change_scored((9, self.rollvalues[9], Scoresheet.standard_scores()[9][1]))
                self.has_taken = True
                return
        for i in range(1, 7):
            if i in self.rollvalues:
                option = (i, value := self.rollvalues[i], Scoresheet.standard_scores()[i][1])
                if value == 2*i and self.difference * (value/(i*3)) >= 3: # Take smallest sufficient value
                    self.change_scored(option)
                    self.has_taken = True
                    return
                elif value == 1*i and self.difference * (value/(i*3)) >= 3:
                    self.change_scored(option)
                    self.has_taken = True
                    return
        if 15 in self.rollvalues:
            if self.rollvalues[15] >= 20:
                self.change_scored((15, self.rollvalues[15], Scoresheet.standard_scores()[15][1]))
                self.has_taken = True
                return    
        if 15 in self.rollvalues and 15 not in self.scored:
            if self.rollvalues[15] >= 15:
                self.change_scored((15, self.rollvalues[15], Scoresheet.standard_scores()[15][1]))
                self.has_taken = True
                return     
        missamount = 0    
        for i in range(1, 7):
            if i not in self.scored:
                missamount += 1
        if 1 in self.rollvalues:
            if missamount > 3 and self.difference > 3:
                self.change_scored((1, self.rollvalues[1], "ones"))
                self.has_taken = True
                return
        else:
            self.cross()
            return   
  
    
                
    def goformultiples(self, keepval):
        for i in self.mydice:
            if i.value == keepval:
                i.kept = True
        return
        
        
    
    def goforfullhouse(self):
        sthrow = set(self.throw)
        valamounts = list()
        for i in sthrow:
            valamounts.append((i, self.throw.count(i)))
        valamounts.sort(reverse=True)
        valamounts.sort(key = lambda y: y[1], reverse=True)
        if valamounts[0][1] == valamounts[1][1] == 2:
            for i in self.mydice:
                if i.value == valamounts[0][0] or i.value == valamounts[1][0]:
                    i.kept = True
            return
        elif valamounts[0][1] == 3 or valamounts[0][1] == 2:
            for i in self.mydice:
                if i.value == valamounts[0][0]:
                    i.kept = True
            return
    
    def goforstreet(self):
        sthrow = set(self.throw)
        keepers = list()
        for i in [2, 3, 4]:
            if i in sthrow:
                keepers.append(i)
        if len(keepers) == 3:
            if 5 in sthrow:
                keepers.append(5)
                for i in self.mydice:
                    if i.value in keepers:
                        i.kept = True
                return
        elif 3 not in sthrow:
            if 4 in keepers:
                if 2 in keepers:
                    keepers.remove(2)
                if 5 in sthrow:
                    keepers.append(5)
        for i in self.mydice:
            if i.value in keepers:
                i.kept = True
            return

    
    def goforhighscore(self):
        for i in self.mydice:
            if i.value >= 4:
                i.kept = True
        return
    
    def cross(self):
        values = 0
        keys = 0
        for i in range(1, 7):
            if i in self.scored:
                values += i
                keys += i
                
        if 1 not in self.scored and values/(keys + 1) >= 3:
            self.change_scored((1, "X", "ones"))
            self.has_taken = True
            return
        for i in [14, 10, 13, 1, 11, 12, 1, 2, 3, 4, 5, 6]:
            if i not in self.scored:
                self.change_scored((i, "X", Scoresheet.standard_scores()[i][1]))
                self.has_taken = True
                return

class Scoresheet:
    def __init__(self, standard=True):
        self.standard = standard
        if self.standard:
            self.maxrounds = 12
            
    @staticmethod
    def standard_scores():
        """Get a dictionary with formulas for each scoring option."""
        scores = {
            1: (
                lambda result: sum(
                    [x for x in result if x == 1 and result.count(1) > 0]
                ),
                "ones",
            ),
            2: (
                lambda result: sum(
                    [x for x in result if x == 2 and result.count(2) > 0]
                ),
                "twos",
            ),
            3: (
                lambda result: sum(
                    [x for x in result if x == 3 and result.count(3) > 0]
                ),
                "threes",
            ),
            4: (
                lambda result: sum(
                    [x for x in result if x == 4 and result.count(4) > 0]
                ),
                "fours",
            ),
            5: (
                lambda result: sum(
                    [x for x in result if x == 5 and result.count(5) > 0]
                ),
                "fives",
            ),
            6: (
                lambda result: sum(
                    [x for x in result if x == 6 and result.count(6) > 0]
                ),
                "sixes",
            ),
            7: (
                lambda result: sum(result) * 0,
                "total top",
            ),  # 7, 8, 15 are kind of stupid this way
            8: (lambda result: sum(result) * 0, "bonus"),
            9: (
                lambda result: sum(result)
                if [x for x in result if result.count(x) >= 3] != []
                else 0,
                "three of a kind",
            ),
            10: (
                lambda result: sum(result)
                if [x for x in result if result.count(x) >= 4] != []
                else 0,
                "four of a kind",
            ),
            11: (
                lambda result: 25
                if (
                    result.count(sorted(result)[0]) >= 2
                    and result.count(sorted(result)[-1]) >= 2
                    and result.count(sorted(result)[0])
                    + result.count(sorted(result)[-1])
                    >= 5
                )
                else 0,
                "full house",
            ),
            12: (
                lambda result: 30
                if [
                    x
                    for x in [1, 2, 3]
                    if x in result
                    and x + 1 in result
                    and x + 2 in result
                    and x + 3 in result
                ]
                != []
                else 0,
                "small street",
            ),
            13: (
                lambda result: 40
                if [
                    x
                    for x in [1, 2]
                    if x in result
                    and x + 1 in result
                    and x + 2 in result
                    and x + 3 in result
                    and x + 4 in result
                ]
                != []
                else 0,
                "big street",
            ),
            14: (lambda result: 50 if result.count(result[0]) == 5 else 0, "kniffel"),
            15: (lambda result: sum(result), "chance"),
            16: (lambda result: sum(result) * 0, "total"),
        }
        return scores
    
    @staticmethod
    def maxpoints():
        points = {1: (5, "ones"),
                  2: (10, "twos"),
                  3: (15, "threes"),
                  4: (20, "fours"),
                  5: (25, "fives"),
                  6: (30, "sixes"),
                  9: (30, "three of a kind"),
                  10: (30, "four of a kind"),
                  11: (25, "full house"),
                  12: (30, "small street"),
                  13: (40, "big street"),
                  14: (50, "kniffel"),
                  15: (30, "chance")}
        return points
        


class Dice:
    def __init__(self, index=0, value=None, kept=False):
        self.index = index
        self.value = value
        self.kept = kept

    def roll(self):
        """Assign a new value to individual die."""
        if self.kept == False:
            self.value = random.randrange(1, 7)

    def keep(self):
        """Change kept-status of individual die."""
        self.kept = not self.kept
