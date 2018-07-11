from core import *

#def choose_class(player_1_name, player_2_name, player_1, player_2, paladin, barbarian):
#    classes = [paladin, barbarian]
#    print classes
#    choice = input('CHOOSE YOUR CLASS').upper().strip()
#    if choice == 'PALADIN':
#        print('THE PALADIN! A WARRIOR OF THE LIGHT! FIGHTING FOR HIS FAITH HE STANDS HERE BEFORE YOU!')
#        print(paladin)
#        surety = input('Are you sure you want this class?').upper().strip()
#        if surety == "YES":
#            return paladin
#        elif surety == "NO":


def get_name():
    name = input('Combatant One! What is your name?')
    print('WELCOME TO THE ARENA', name.upper(), '!')
    return name


def get_name_2():
    name = input('Combatant Two! What is your name?')
    print('WELCOME TO THE ARENA', name.upper(), '!')
    return name


def choose_weapons(player_1_name, player_2_name, player_1, player_2, weapons):
    print(weapons)
    choice = input(f'{player_1_name} CHOOSE YOUR WEAPON!').upper().strip()
    if choice == 'SWORD':
        player_1['Low Attack'] += 10
        player_1['High Attack'] += 10
        player_1['Rage'] += 5
        print('The sword? It is a good choice')
    if choice == 'WARAXE':
        player_1['Low Attack'] += 5
        player_1['High Attack'] += 5
        player_1['Rage'] += 10

        print('The war axe you say? It can be devastating in the right hands')
    choice = input(f'{player_2_name} CHOOSE YOUR WEAPON!').upper().strip()
    if choice == 'SWORD':
        player_2['Low Attack'] += 10
        player_2['High Attack'] += 10
        player_2['Rage'] += 5

        print('The sword? It is a good choice')
    if choice == 'WARAXE':
        player_2['Low Attack'] += 5
        player_2['High Attack'] += 5
        player_2['Rage'] += 10
        print('The war axe you say? It can be devastating in the right hands')


def combatant_1_turn(player_1_name, player_1, player_2_name, player_2):

    while True:

        print(player_1_name.upper(), '! It is your turn!')
        print(player_1_name.upper(), "'S STATS!", player_1['Health'], '|||',
              player_1['Rage'])
        print('WHAT SHALL YOU DO!?')
        print('----[A]TTACK')
        print('----[H]EAL')
        print('----[E]NRAGE')
        print('----[P]ASS')
        print('----[Q]UIT')
        choice = input('CHOOSE NOW!').upper().strip()
        if choice == 'A':
            print(player_1_name.upper(), 'ATTACKS', player_2_name.upper(), '!')
            attack(player_1, player_2)
            print(player_2_name, "'s Health!:", player_2['Health'])
            break
        elif choice == 'H':
            print(player_1_name.upper(), 'HEALS!')
            heal(player_1)
            break
        elif choice == 'E':
            print(player_1_name.upper(), 'HAS BECOME ENRAGED!')
            enrage(player_1)
            break
        elif choice == 'P':
            player_1['Rage'] += 20
            print(player_1_name.upper(), 'PASSES!')
        elif choice == 'Q':
            print(player_1_name.upper(), 'HAS FORFEITED THEIR LIFE')
            exit()
        else:
            print("PLEASE CHOOSE A VALID OPITON")
        print(player_1_name.upper(), "'S STATS!", player_1['Health'], '|||',
              player_1['Rage'])


def combatant_2_turn(player_1_name, player_1, player_2_name, player_2):

    while True:

        print(player_2_name.upper(), '! It is your turn!')
        print(player_2_name.upper(), "'S STATS!", player_2['Health'], '|||',
              player_2['Rage'])
        print('WHAT SHALL YOU DO!?')
        print('----[A]TTACK')
        print('----[H]EAL')
        print('----[E]NRAGE')
        print('----[P]ASS')
        print('----[Q]UIT')
        choice = input('CHOOSE NOW!').upper().strip()
        if choice == 'A':
            print(player_2_name.upper(), 'ATTACKS', player_1_name.upper(), '!')
            attack(player_2, player_1)
            print(player_1_name, "'s Health!:", player_1['Health'])
            break
        elif choice == 'H':
            print(player_2_name.upper(), 'HEALS!')
            heal(player_2)
            break
        elif choice == 'E':
            print(player_2_name.upper(), 'HAS BECOME ENRAGED!')
            enrage(player_2)
            break
        elif choice == 'P':
            player_2['Rage'] += 20
            print(player_2_name.upper(), 'PASSES!')
            pass
            break
        elif choice == 'Q':
            print(player_2_name.upper(), 'HAS FORFEITED THEIR LIFE')
            exit()
        else:
            print("PLEASE CHOOSE A VALID OPTION")
            print(player_2_name.upper(), "'S STATS!", player_2['Health'],
                  '|||', player_2['Rage'])


def battle(player_1_name, player_1, player_2_name, player_2):

    while True:
        if is_dead(player_1) == True:
            print(player_1_name.upper(), 'HAS FALLEN!')
            print(player_2_name.upper(), 'IS VICTORIOUS!')
            break
            exit()
        combatant_1_turn(player_1_name, player_1, player_2_name, player_2)
        if is_dead(player_2) == True:
            print(player_2_name.upper(), 'HAS FALLEN!')
            print(player_1_name.upper(), 'IS VICTORIOUS!')
            break
            exit()
        combatant_2_turn(player_1_name, player_1, player_2_name, player_2)


def game_play():

    player_1_name = get_name()
    player_1 = new_gladiator(100, 15, 1, 40)
    player_2_name = get_name_2()
    player_2 = new_gladiator(100, 15, 1, 40)
    weapons = weapons_dic()
    choose_weapons(player_1_name, player_2_name, player_1, player_2, weapons)

    battle(player_1_name, player_1, player_2_name, player_2)


def main():
    game_play()


if __name__ == '__main__':
    main()
