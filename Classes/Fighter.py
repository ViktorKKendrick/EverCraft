import Character


class Fighter(Character):
    def __init__(self, first, last, alignment):
        self.hitPoints = 10  # 10HP per level
        # maxHitPoints = level * 10;
