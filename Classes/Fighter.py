import Character
from Modifiers import *


class Fighter(Character):
    def __init__(self, Strength, level):
        self.hitPoints = 10  # 10HP per level
        self.charClass = 'Fighter'

    # Attack Method for Fighter
    def attack(self, target, level):
        attackRoll = 11 + self.attRollMod + level
        damage = ((1 + self.attMod) * 2) if ((1 + self.attMod)*2 > 1) else 1
        if attackRoll == 20:
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
        self.hitPoints += (10 + modifiers[self.Constitution])
        # attacks roll is increased by 1 for every level instead of every other level
        self.attRollMod += 1
