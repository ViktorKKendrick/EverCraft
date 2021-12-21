#Character Class

class Character:
    # Constructor
    def __init__(self, first, last, charClass):
        self.first = first
        self.last = last
        self.charClass = charClass

    def fullName(self):
        return '{} {}'.format(self.first, self.last)
    


# Test Case
char1 = Character('Main', 'Character', 'Rogue')
print('Name: ' + char1.fullName())
print('Class: ' + char1.charClass)
