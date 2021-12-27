import Character


class Rogue(Character):
    def __init__(self, alignment):
        # alignment CANNOT be Good
        self.alignment = 'Neutral' if alignment == 0 else 'Evil'
        self.charClass = 'Rogue'

    def attack(self, target):
        # attackRoll = randrange(1, 21, 2)
        attackRoll = 11
        if attackRoll == 20:
            target.hitPoints = target.hitPoints - 2 * 3
            print('critical hit')
        if attackRoll >= target.ac:
            target.hitPoints = target.hitPoints - 1
            print('hit')
        else:
            print('fail')
