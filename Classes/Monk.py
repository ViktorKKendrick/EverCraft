import Character


class Monk(Character):
    def __init__(self, first, last, alignment):
        self.hitPoints = 6  # 6HP per level
        # maxHitPoints = level * 6;
        # if attackRoll >= target.ac:
        #     target.hitPoints = target.hitPoints - 3
