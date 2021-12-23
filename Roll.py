from random import randrange
import operator
# list(map(operator.add, first,second))
# attackRoll = randrange(1, 21, 2)
def rollStats():
    rolls=[]
    for y in range(6):
        rolls.append(rollStat())
    print(rolls)

def rollStat():
    rolls=[]
    for x in range(4):
        rolls.append(randrange(1, 7))

    while 1 in rolls:
        rolls[rolls.index(1)] = randrange(1, 7)

    result = sum(rolls) - min(rolls)
    return result

def Spaces(num):
    s=''
    for x in range(num):
        s+=' '
    return s
# rollStats()
# rollStat()