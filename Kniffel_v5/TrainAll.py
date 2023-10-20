import sys 
import MaxOnes, MaxTwos, MaxThrees, MaxFours, MaxFives, MaxSixes, MaxThreeOfAKind, MaxFourOfAKind, MaxFullHouse, MaxSmallStreet, MaxBigStreet, MaxKniffel, MaxChance





allrolls = list()
for i in range(1, 7):
    for j in range (1, 7):
        for k in range ( 1, 7):
            for l in range (1, 7):
                for m in range (1, 7):
                    roll = [i, j, k, l, m]
                    allrolls.append(roll)
                    
for index, i in enumerate(allrolls):
    i.sort()
    allrolls[index] = tuple(i)
    
allrolls = list(dict.fromkeys(allrolls))

#MaxOnes.golearn(allrolls)
#MaxTwos.golearn(allrolls)
#MaxTwos.contlearn(allrolls)
#MaxThrees.golearn(allrolls)
#MaxFours.golearn(allrolls)
#MaxFives.golearn(allrolls)
#MaxSixes.golearn(allrolls)
#MaxThreeOfAKind.golearn(allrolls)
#MaxFourOfAKind.golearn(allrolls)
#MaxFullHouse.golearn(allrolls)
#MaxFullHouse.contlearn(allrolls)

MaxSmallStreet.golearn(allrolls)
MaxBigStreet.golearn(allrolls)
MaxKniffel.golearn(allrolls)
MaxChance.golearn(allrolls)