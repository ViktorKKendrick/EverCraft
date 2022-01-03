from random import randrange
from Modifiers import *
from Roll import *
from Weapon import *
from All_Weapons import *
# Character Class


class Character:
    level = 1
    Strength = 10
    Dexterity = 10
    Constitution = 10
    Wisdom = 10
    Intelligence = 10
    Charisma = 10
    ac = 10 + modifiers[Dexterity]
    hitPoints = 30 + \
        modifiers[Constitution] if modifiers[Constitution] >= 0 else 5 + 1
    exp = 0
    attRollMod = modifiers[Strength]
    attMod = modifiers[Strength]

    # Constructor
    def __init__(self, name, charClass, alignment, race='human'):
        self.race = race
        self.name = name
        self.charClass = charClass
        self.alignment = 'Neutral' if alignment == 0 else 'Evil' if alignment == -1 else 'Good'

    # Gets character name
    def getName(self):
        return self.name

    # Gets character alignment
    def getAlignment(self):
        return self.alignment

    # Changes Alignment
    def setAlignment(self, alignment):
        self.alignment = 'Good' if alignment == 1 else 'Evil' if alignment == -1 else 'Neutral'

    # Set up character sheet for readablility
    def getCharSheet(self):
        print(' ')
        print('''
        Name: ''' + self.name + Spaces(6) + 'Class: ' + self.charClass + Spaces(6) + 'Race: ' + self.race + '''
        Alignment: ''' + self.alignment + Spaces(11) + 'AC: ' + str(self.ac) + Spaces(12) + 'Hit Points: ' + str(self.hitPoints) + '''
        level: ''' + str(self.level) + Spaces(18) + 'exp: ' + str(self.exp) + ''''''
              )
        print('''
        Strength: ''' + str(self.Strength) + Spaces(16) + 'Modifier: ' + str(modifiers[self.Strength]) + '''
        Dexterity: ''' + str(self.Dexterity) + Spaces(15) + 'Modifier: ' + str(modifiers[self.Dexterity]) + '''
        Constitution: ''' + str(self.Constitution) + Spaces(12) + 'Modifier: ' + str(modifiers[self.Constitution]) + '''
        Wisdom: ''' + str(self.Wisdom) + Spaces(18) + 'Modifier: ' + str(modifiers[self.Wisdom]) + '''
        Intelligence: ''' + str(self.Intelligence) + Spaces(12) + 'Modifier: ' + str(modifiers[self.Intelligence]) + '''
        Charisma: ''' + str(self.Charisma) + Spaces(16) + 'Modifier: ' + str(modifiers[self.Charisma]) + '''
        ''')

    # Attack Method
    def attack(self, target):
        attackRoll = 11 + self.attRollMod
        weapon_name = self.weapon['name']
        print(weapon_name)
        damage = ((int(self.weapon['base_dam']) + self.attMod)) if (
            (int(self.weapon['base_dam']) + self.attMod) > 1) else 1
        if weapon_name == 'elven longsword':
            if (self.race == 'elf') and (target.race == 'orc'):
                # +5 to attack and damage when wielded by an elf and against orc
                damage += 11
                attackRoll += 6
            elif self.race == 'elf' or target.race == 'orc':
                # +2 to attack and damage when wielded by an elf or against an orc
                damage += 8
                attackRoll += 3
            else:
                # does 5 points of damage
                # +1 to attack and damage
                damage += 6
                attackRoll += 1
        if weapon_name == 'longsword':
            damage += 5
        if weapon_name == 'waraxe':
            # does 6 points of damage
            # +2 to damage
            damage += 8
            # +2 to attack
            attackRoll += 2
        if weapon_name == 'nunchucks':
            if self.charClass != 'monk':
                # when used by a non-monk there is a -4 penalty to attack
                atttackRoll -= 4
            # does 6 points of damage
            damage += 6

        if attackRoll == 20:
            # triple damage on a critical (quadruple for a Rogue)
            if weapon_name == 'waraxe' and self.charClass == 'Rogue':
                target.hitPoints = target.hitPoints - (damage*4)
                print('critical hit')
            elif weapon_name == 'waraxe':
                target.hitPoints = target.hitPoints - (damage*3)
                print('critical hit')
            else:
                target.hitPoints = target.hitPoints - (damage*2)
                print('critical hit')
        if attackRoll >= target.ac:
            if target.hitPoints > 0:
                target.hitPoints = target.hitPoints - (damage)
                print('hit')
                self.exp += 10
                if (self.exp % 1000) == 0:
                    self.levelUp()
                if target.hitPoints <= 0:
                    print('target is dead')
                self.getCharSheet()
                target.getCharSheet()
            else:
                print('target is already dead, attack someone else you murderer!')
        else:
            print('fail')

    # LevelUp Method
    def levelUp(self):
        self.level += 1
        self.hitPoints += (5 + modifiers[self.Constitution])
        if (self.level % 2) == 0:
            self.attRollMod += 1

    def equip(self, weapon_name):
        self.weapon = weapons[all_w[weapon_name]]
        print(self.weapon)
        # print(self.weapon[])
