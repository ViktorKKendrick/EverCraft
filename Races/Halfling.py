from Character import *
from Modifiers import *


class Halfling(Character):
    def abilityModifier(self):
        self.Dexterity += 1
        self.Constitution -= 1

    def attack(self, target):
        attackRoll = 11 + self.attRollMod
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
                # Halflings are small and hard to hit
                if target.race != 'Halfling':
                    self.ac += 2
                #Halflings can't be evil
                if self.alignment == 'Evil':
                    print ('Halflings cannot be evil')
                self.getCharSheet()

            else:
                print('target is already dead, attack someone else you murderer!')
        else:
            print('fail')
