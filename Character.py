from random import randrange
# Character Class

class Character:
    # Constructor
    def __init__(self, first, last, charClass, alignment):
        self.first = first
        self.last = last
        self.charClass = charClass
        self.ac = 10
        self.hitPoints = 5
        self.exp = 0
        self.alignment = 'Neutral' if alignment == 0 else 'Evil' if alignment == -1 else 'Good'
    
    # Gets character name
    def getName(self):
        return '{} {}'.format(self.first, self.last)
    
    # Gets character alignment
    def getAlignment(self):
        return self.alignment

    # Changes Alignment
    def setAlignment(self, alignment):
        self.alignment = 'Neutral' if alignment == 0 else 'Evil' if alignment == -1 else 'Good'
    
    # Set up character sheet for readablility 
    def getCharSheet(self):
        print(' ')
        print('Name: ' + self.getName())
        print('Class: ' + self.charClass)
        print('Alignment: ' + self.alignment)
        print('AC: ' + str(self.ac))
        print('Hit Points: ' + str(self.hitPoints))
        print(' ')
    
    # Attack Method
    def attack(self, target):
        # attackRoll = randrange(1, 21, 2)
        attackRoll= 11
        if attackRoll == 20:
            target.hitPoints = target.hitPoints - 2
            print('critical hit')
        if attackRoll >= target.ac:
            target.hitPoints = target.hitPoints - 1
            print('hit')
        else:
            print('fail')

# Test Cases
char1 = Character('Main', 'Character', 'Rogue', 1)
char2 = Character('Secondary', 'Character', 'Knight', 0)
char3 = Character('Useless', 'Character', 'Wizard', -1)
char1.getCharSheet()
# char1.attack(char2)
char2.getCharSheet()
char3.getCharSheet()

# Input
while 0 != 1:
    if input() == 'attack':
        print('Attack who? ')
        target = input()
        target = char1 if target == 'char1' else char2 if target == 'char2' else char3
        char1.attack(target)
        target.getCharSheet()