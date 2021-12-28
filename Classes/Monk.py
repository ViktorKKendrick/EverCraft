import Character
from Modifiers import *


class Monk(Character):
    def __init__(self, Dexterity, Wisdom):
        self.hitPoints = 6  # 6HP per level
        self.charClass = 'Monk'
        # adds Wisdom modifier (if positive) to Armor Class in addition to Dexterity
        self.ac = 10 + modifiers[Dexterity] + modifiers[Wisdom]

    def incr_att_by_level(level):
        # attack roll is increased by 1 every 2nd and 3rd level
        if level % 2 == 0 or level % 3 == 0:
            return 1 * level
        else:
            return 0

    # Attack Method
    def attack(self, target):
        attackRoll = 11 + self.attRollMod + self.inc_att_by_level(self.level)
        # does 3 points of damage instead of 1 when successfully attacking
        damage = ((3 + self.attMod) * 2) if ((3 + self.attMod)*2 > 1) else 3
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
        self.hitPoints += (6 + modifiers[self.Constitution])
        if (self.level%2) == 0 or self.level % 3 == 0:
            self.attRollMod += 1
