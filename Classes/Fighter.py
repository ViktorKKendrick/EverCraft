import Character


class Fighter(Character):
    def __init__(self):
        self.hitPoints = 10  # 10HP per level
        # maxHitPoints = level * 10;
        self.charClass = 'Fighter'

    # Attack Method
    def attack(self, target):
        # attacks roll is increased by 1 for every level instead of every other level?
        attackRoll = 11
        if attackRoll == 20:
            target.hitPoints = target.hitPoints - 2
            print('critical hit')
        if attackRoll >= target.ac:
            target.hitPoints = target.hitPoints - 1
            print('hit')
        else:
            print('fail')
