from core import *


def choose_class(paladin, barbarian):
    classes = [paladin, barbarian]
    print classes
    choice = input('CHOOSE YOUR CLASS').upper().strip()
    if choice == 'PALADIN':
        print('THE PALADIN! A WARRIOR OF THE LIGHT! FIGHTING FOR HIS FAITH HE STANDS HERE BEFORE YOU!')
        print(paladin)
        surety = input('Are you sure you want this class?').upper().strip()
        if surety == "YES":
            return paladin
        elif surety == "NO":
            



def get_name():
    name = input('Combatant One! What is your name?')
    print('WELCOME TO THE ARENA', name.upper(), '!')
    return name


def get_name_2():
    name = input('Combatant Two! What is your name?')
    print('WELCOME TO THE ARENA', name.upper(), '!')
    return name


def choose_weapons(name_a, name_b, user_a, user_b, weapons):
    print(weapons)
    choice = input(f'{name_a} CHOOSE YOUR WEAPON!').upper().strip()
    if choice == 'SWORD':
        user_a['Low Attack'] += 10
        user_a['High Attack'] += 10
        user_a['Rage'] += 5
        print('The sword? It is a good choice')
    if choice == 'WARAXE':
        user_a['Low Attack'] += 5
        user_a['High Attack'] += 5
        user_a['Rage'] += 10

        print('The war axe you say? It can be devastating in the right hands')
    choice = input(f'{name_b} CHOOSE YOUR WEAPON!').upper().strip()
    if choice == 'SWORD':
        user_b['Low Attack'] += 10
        user_b['High Attack'] += 10
        user_b['Rage'] += 5

        print('The sword? It is a good choice')
    if choice == 'WARAXE':
        user_b['Low Attack'] += 5
        user_b['High Attack'] += 5
        user_b['Rage'] += 10
        print('The war axe you say? It can be devastating in the right hands')


def combatant_1_turn(name_a, user_a, name_b, user_b):

    while True:

        print(name_a.upper(), '! It is your turn!')
        print(name_a.upper(), "'S STATS!", user_a['Health'], '|||',
              user_a['Rage'])
        print('WHAT SHALL YOU DO!?')
        print('----[A]TTACK')
        print('----[H]EAL')
        print('----[P]ASS')
        print('----[Q]UIT')
        choice = input('CHOOSE NOW!').upper().strip()
        if choice == 'A':
            print(name_a.upper(), 'ATTACKS', name_b.upper(), '!')
            attack(user_a, user_b)
            print(name_b, "'s Health!:", user_b['Health'])
            break
        elif choice == 'H':
            print(name_a.upper(), 'HEALS!')
            heal(user_a)
            break
        elif choice == 'P':
            user_a['Rage'] += 20
            print(name_a.upper(), 'PASSES!')
        elif choice == 'Q':
            print(name_a.upper(), 'HAS FORFEITED THEIR LIFE')
            exit()
        else:
            print("PLEASE CHOOSE A VALID OPITON")
        print(name_a.upper(), "'S STATS!", user_a['Health'], '|||',
              user_a['Rage'])


def combatant_2_turn(name_a, user_a, name_b, user_b):

    while True:

        print(name_b.upper(), '! It is your turn!')
        print(name_b.upper(), "'S STATS!", user_b['Health'], '|||',
              user_b['Rage'])
        print('WHAT SHALL YOU DO!?')
        print('----[A]TTACK')
        print('----[H]EAL')
        print('----[P]ASS')
        print('----[Q]UIT')
        choice = input('CHOOSE NOW!').upper().strip()
        if choice == 'A':
            print(name_b.upper(), 'ATTACKS', name_a.upper(), '!')
            attack(user_b, user_a)
            print(name_a, "'s Health!:", user_a['Health'])
            break
        elif choice == 'H':
            print(name_b.upper(), 'HEALS!')
            heal(user_b)
            break
        elif choice == 'P':
            user_b['Rage'] += 20
            print(name_b.upper(), 'PASSES!')
            pass
            break
        elif choice == 'Q':
            print(name_b.upper(), 'HAS FORFEITED THEIR LIFE')
            exit()
        else:
            print("PLEASE CHOOSE A VALID OPTION")
            print(name_b.upper(), "'S STATS!", user_b['Health'], '|||',
                  user_b['Rage'])


def battle(name_a, user_a, name_b, user_b):

    while True:
        if is_dead(user_a) == True:
            print(name_a.upper(), 'HAS FALLEN!')
            print(name_b.upper(), 'IS VICTORIOUS!')
            break
            exit()
        combatant_1_turn(name_a, user_a, name_b, user_b)
        if is_dead(user_b) == True:
            print(name_b.upper(), 'HAS FALLEN!')
            print(name_a.upper(), 'IS VICTORIOUS!')
            break
            exit()
        combatant_2_turn(name_a, user_a, name_b, user_b)


def game_play():

    name_a = get_name()
    user_a = new_gladiator(100, 15, 1, 40)
    name_b = get_name_2()
    user_b = new_gladiator(100, 15, 1, 40)
    weapons = weapons_dic()
    choose_weapons(name_a, name_b, user_a, user_b, weapons)

    battle(name_a, user_a, name_b, user_b)


def main():
    game_play()


if __name__ == '__main__':
    main()
