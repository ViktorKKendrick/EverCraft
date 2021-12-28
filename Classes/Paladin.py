import Character
from Modifiers import *


class Paladin(Character):
    def __init__(self):
        self.hitPoints = 8  # 8HP per level
        self.charClass = 'Paladin'
        # can only have Good alignment
        self.alignment = 'Good'

    def attack_on_evil(target):
        if target.alignment == 'Evil':
            return 2
        else:
            return 0

    # Attack Method
    def attack(self, target):
        # attacks roll is increased by 1 for every level instead of every other level
        attackRoll = 11 + self.attRollMod + self.attack_on_evil(target)
        # +2 to attack and damage when attacking Evil characters
        damage = ((1 + self.attMod) * 2) + self.attack_on_evil if ((1 + self.attMod)*2 > 1) else 1 + self.attack_on_evil
        if attackRoll == 20:
            # does triple damage when critting on an Evil character
            if target.alignment == 'Evil':
                target.hitPoints = target.hitPoints - (damage/2) * 3
                print('critical critical hit')
            else:
                target.hitPoints = target.hitPoints - damage
                print('critical hit')
        if attackRoll >= target.ac:
            if target.hitPoints > 0:
                target.hitPoints = target.hitPoints - (damage/2)
                print('hit')
                self.exp += 1000
                if (self.exp % 1000) == 0:
                    self.levelUp()
                if target.hitPoints <= 0:
                    print('target is dead')
                self.getCharSheet()
            else:
                print('target is already dead, attack someone else you murderer!')
        else:
            print('fail')
            
    # LevelUp Method
    def levelUp(self):
        self.level += 1
        self.hitPoints += (8 + modifiers[self.Constitution])
        # attacks roll is increased by 1 for every level instead of every other level
        self.attRollMod += 1
