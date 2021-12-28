import Character
from Modifiers import *


class Monk(Character):
    def __init__(self, first, last, alignment):
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
        attackRoll = 11 + self.attRollMod + self.attack_on_evil + 1 * self.level
        # +2 to attack and damage when attacking Evil characters
        damage = ((1 + self.attMod) * 2) + self.attack_on_evil if ((1 +
                                                                    self.attMod)*2 > 1) else 1 + self.attack_on_evil
        if attackRoll == 20:
            # does triple damage when critting on an Evil character
            if target.alignment == 'Evil':
                target.hitPoints = target.hitPoints - damage * 3
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
