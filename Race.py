# Defining races as a class


class Race:

    def __init__(self, raceName, language, maturity, lifespan, size, speed, specialTraits):
        self.raceName = raceName
        self.language = language
        self.maturity = maturity
        self.lifespan = lifespan
        self.size = size
        self.speed = speed
        self.specialTraits = specialTraits


dragonborn = Race(
    "Dragonborn",
    "Common and Draconic",
    15,
    80,
    "Medium",
    30,
    "Draconic Ancestry"
)
# draconic ancestry has 3 parts dragon type, damage type, and Breath Weapon
# ability score increase is str + 2 and Cha + 1
dwarf = Race(
    "Dwarf",
    "Common and Dwarvish",
    50,
    350,
    "Medium",
    25,
    "Darkvision, Dwarven Resilience, Dwarven Combat Training, Tool Proficiency, and Stonecunning"
)
# ability score increase is Con + 2
# has 2 sub races: Hill Dwarf and Mountain Dwarf
elf = Race(
    "Elf",
    "Common and Elvish",
    100,
    750,
    "Medium",
    30,
    "Darkvision, Keen Senses, Fey Ancestry, and Trance"
)
# ability score increase is Dex + 2
# 3 sub races: high elf, wood elf, and dark elf
gnome = Race(
    "Gnome",
    "Common and Gnomish",
    40,
    500,
    "Small",
    25,
    "Darvision and Gnome Cunning")
# ability score increase is Int + 2
# 2 sub races deep gnome and rock gnome
halfElf = Race(
    "Half-Elf",
    "Common, Elvish, and a language of your choice",
    20,
    180,
    "Medium",
    30,
    "Darkvision, Fey ancestry, and Skill Versatility")
# needs to be able to chose a language
# ability score increase is Cha + 2 and needs to be able to choose an ability to increase by 1
# hafling = Race()
# halfOrc = Race()
# human = Race()
# tiefling = Race()
# print(dragonborn)
