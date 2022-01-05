from Character import * 
from Modifiers import * 

class Elf(Character):
    def abilityModifier(self):
        self.Dexterity += 1
        self.Constitution -= 1 

    # Attack Method
    def attack(self, target):
        attackRoll= 11 + self.attRollMod
        damage = ((1 + self.attMod)) if ((1 + self.attMod) > 1) else 1
        if attackRoll == 20:
            target.hitPoints = (target.hitPoints - damage * 2) + 1 #Elves have +1 to their attack when they roll a critical
            print('critical hit')
        if attackRoll >= target.ac:
            if target.hitPoints > 0:
                target.hitPoints = target.hitPoints - (damage)
                print('hit')
                self.exp += 10
                if (self.exp%1000) == 0:
                    self.levelUp()
                if target.hitPoints <= 0:
                    print('target is dead')
                    #Orcs have a harder time hiting elves for some reason 
                if target.race == 'Orc':
                    self.ac += 2
                self.getCharSheet()
                
            else:
                print('target is already dead, attack someone else you murderer!')
        else:
            print('fail')
