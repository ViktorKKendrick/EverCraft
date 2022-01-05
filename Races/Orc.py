from Character import *
from Modifiers import *

class Orc(Character):
    def abilityModifier(self):
        self.Strength += 2
        self.Intelligence -= 1
        self.Wisdom -= 1
        self.Charisma -= 1

#Orcs have thick hides
    def attack(self, target):
        attackRoll = 11 + self.attRollMod
        self.ac += 2
        damage = ((1 + self.attMod)) if ((1 + self.attMod) > 1) else 1
        if attackRoll == 20:
            target.hitPoints = target.hitPoints - damage * 2
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
                if target.race != 'Halfling':
                    self.ac += 2
                self.getCharSheet()

            else:
                print('target is already dead, attack someone else you murderer!')
        else:
            print('fail')
