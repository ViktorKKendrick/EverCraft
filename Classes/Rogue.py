import Character


class Rogue(Character):
    def __init__(self, first, last, alignment):
        self.alignment = 'Neutral' if alignment == 0 else 'Evil'
        # if attackRoll == 20
        #   target.hitPoints = target.hitPoints - 2 * 3
        # alignment CANNOT be Good
