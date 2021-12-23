import Character


class Monk(Character):
    def __init__(self, first, last, alignment):
        self.hitPoints = 8  # 8HP per level
        self.alignment = 'Good'
        # maxHitPoints = level * 8;
        # if attackRoll >= target.ac:
        #   if target.alignment == 'Evil'
        #     target.hitPoints = target.hitPoints - 3
