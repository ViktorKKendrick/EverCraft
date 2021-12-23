from Character import *
from Modifiers import *
from Roll import *

char1 = Character('Main Character', 'Rogue', 1)
char2 = Character('Secondary Character', 'Knight', 0)
char3 = Character('Useless Character', 'Wizard', -1)

name = input('what is your name? ')
user_class = input('what is your class? ')
alignment = int(input('what is your alignment? '))

custom = Character(name, user_class, alignment)

custom.getCharSheet()

while 0 != 1:
    user_input = input()
    if user_input == 'attack':
        print('Attack who? ')
        target = input()
        target = char1 if target == 'char1' else char2 if target == 'char2' else char3 if target == 'char3' else 'empty'
        if target == 'empty':
            break
        custom.attack(target)
        
    elif user_input == 'exit':
        break