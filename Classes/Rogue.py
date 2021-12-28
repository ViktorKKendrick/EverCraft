import Character
from Modifiers import *


class Rogue(Character):
    def __init__(self, alignment, Dexterity):
        # alignment CANNOT be Good
        self.alignment = 'Neutral' if alignment == 0 else 'Evil'
        self.charClass = 'Rogue'
        # adds Dexterity modifier to attacks instead of Strength
        self.attMod = modifiers[Dexterity]
        self.attRollMod = modifiers[Dexterity]

    # Attack Method
    def attack(self, target):
        attackRoll = 11 + self.attRollMod
        damage = ((1 + self.attMod) * 3) if ((1 + self.attMod)*3 > 1) else 1
        if attackRoll == 20:
            # does triple damage on critical hits
            target.hitPoints = target.hitPoints - damage
            print('critical hit')
        # ignores an opponents Dexterity modifier (if positive) to Armor Class when attacking
        target_ac = target.ac - modifiers[target.Dexterity] if modifiers[target.Dexterity] >= 0 else target.ac
        if attackRoll >= target_ac:
            if target.hitPoints > 0:
                target.hitPoints = target.hitPoints - (damage/3)
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
