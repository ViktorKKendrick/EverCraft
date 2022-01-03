# from All_Weapons import *
# import Character

# class Weapon(Character):
#     # Constructor
#     def __init__(self, weapon_name, base_dam, att_bonus=0, dam_bonus=0):
#         self.weapon_name = weapon_name
#         self.base_dam = base_dam
#         self.att_bonus = att_bonus
#         self.dam_bonus = dam_bonus

#     def waraxe_crit_bonus(self, weapon_name):
#         # WARAXE: triple damage on a critical (quadruple for a Rogue)
#         if weapon_name == "waraxe":
#             if self.charClass == 'Rogue':
#                 return 4
#             else:
#                 return 3
