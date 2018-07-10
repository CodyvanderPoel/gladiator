from core import *


def get_name():
    name = input('Combatant One! What is your name?')
    print('WELCOME TO THE ARENA', name.upper(), '!')
    return name


def get_name_2():
    name = input('Combatant Two! What is your name?')
    print('WELCOME TO THE ARENA', name.upper(), '!')
    return name


def combatant_1_turn(name_a, user_a, name_b, user_b):

    while True:

        print(name_a.upper(), '! It is your turn!')
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
            print(name_a.upper(), 'PASSES!')
        elif choice == 'Q':
            exit()
        else:
            print("PLEASE CHOOSE A VALID OPITON")


def combatant_2_turn(name_a, user_a, name_b, user_b):

    while True:

        print(name_b.upper(), '! It is your turn!')
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
            print(name_b.upper(), 'PASSES!')
            pass
            break
        elif choice == 'Q':
            exit()
        else:
            print("PLEASE CHOOSE A VALID OPITON")


def battle(name_a, user_a, name_b, user_b):

    while True:
        if is_dead(user_a) == True:
            print(name_b.upper(), 'HAS FALLEN!')
            print(name_a.upper(), 'IS VICTORIOUS!')
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
    user_a = new_gladiator(100, 15, 20, 40)
    name_b = get_name_2()
    user_b = new_gladiator(100, 15, 20, 40)
    battle(name_a, user_a, name_b, user_b)


def main():
    game_play()


if __name__ == '__main__':
    main()
