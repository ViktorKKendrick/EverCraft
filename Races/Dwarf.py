from Character import * 
from Modifiers import * 

class Dwarf:
    def abilityModifier(self):
        self.constitution = 11
        self.charisma = 9 

     # Attack Method
    def attack(self, target):
        attackRoll= 11 + self.attRollMod
        damage = ((1 + self.attMod) * 2) if ((1 + self.attMod)*2 > 1) else 1
        if attackRoll == 20:
            target.hitPoints = target.hitPoints - damage
            print('critical hit')
        if attackRoll >= target.ac:
            if target.hitPoints > 0:
                target.hitPoints = target.hitPoints - (damage/2)
                print('hit')
                self.exp += 1000
                if (self.exp%1000) == 0:
                    self.levelUp()
                if target.hitPoints <= 0:
                    print('target is dead')
                if target.race == 'Orc':
                    damage = attackRoll + 2
                self.getCharSheet()
                
            else:
                print('target is already dead, attack someone else you murderer!')
        else:
            print('fail')


    def levelUp(self):
        self.hitPoints += (5 + (2 * (modifiers[self.constitution])))