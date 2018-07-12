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
        print(player_1_name.upper(), "'S STATS! \n Health:",
              player_1['Health'], '||| Rage:', player_1['Rage'],
              '||| Precision:', player_1['Precision'], '||| Mana:',
              player_1['Mana'])
        print('WHAT SHALL YOU DO!?')
        print('----[A]TTACK')
        print('----[H]EAL')
        print('----[M]AGIC')
        print('----[E]NRAGE')
        print('----[C]ONCENTRATE')
        print('----[P]ASS')
        print('----[Q]UIT')
        choice = input('CHOOSE NOW!').upper().strip()
        if choice == 'A':
            print(player_1_name.upper(), 'ATTACKS', player_2_name.upper(), '!')
            attack(player_1, player_2)
            print(player_1_name.upper(), "'S STATS!", player_1['Health'],
                  '|||', player_1['Rage'], '|||', player_1['Precision'])
            print(player_2_name, "'s Health!:", player_2['Health'])
            break
        elif choice == 'H':
            print(player_1_name.upper(), 'HEALS!')
            if player_1['Health'] > 100:
                player_1['Health'] = 100
            heal(player_1)
            print(player_1_name.upper(), "'S STATS!", player_1['Health'],
                  '|||', player_1['Rage'], '|||', player_1['Precision'])
            break
        elif choice == 'M':
            print(player_1_name.upper(), 'IS CASTING A SPELL!')
            spells = magic(player_1, player_2)
            print(spells)
            spell = input('What spell shall you cast?').upper()
            if spell == 'A':
                if player_1['Mana'] >= 5:
                    player_2['Health'] -= 10
                    player_2['Precision'] -= 5
                    player_1['Mana'] -= 5
                    print(player_1_name.upper(), 'CAST AARD!')
                    print('IT DEALT 10 DAMAGE AND CAUSED',
                          player_2_name.upper(), 'TO STUMBLE!')
            elif spell == 'I':
                if player_1['Mana'] >= 15:
                    player_2['Health'] -= 20
                    player_2['Precision'] -= 10
                    player_1['Mana'] -= 15
                    print(player_1_name.upper(), 'CAST IGNI!')
                    print(
                        'FLAMES BURST FROM YOUR HAND IGNITING', player_2_name,
                        '! THE FLAMES DISPERSE QUICKLY, SLIGHTLY DISRUPTING THEIR VISION AND DEALING 20 DAMAGE! '
                    )
            elif spell == 'G':
                if player_1['Mana'] >= 25:
                    player_1['Mana'] -= 25
                    player_1['Health'] += randint(25, 45)
                    print(player_1_name.upper(), 'CASTS GREAT HEAL!')
                    print(
                        'A HEAVENLY LIGHT DESCENDS GRANTING YOU RESTORED STRENGTH'
                    )
            elif spell == 'R':
                if player_1['Mana'] == 50:
                    player_1['Mana'] -= 50
                    player_1['Health'] -= randint(0, 100)
                    player_2['Health'] -= randint(0, 100)
                    print(player_1_name.upper(), 'HAS CAUSED THE RECKONING!')
                    print(
                        'WILL ANYONE SURVIVE AS THE HEAVENS CRASH AROUND YOU AND YOUR OPPONENT!?'
                    )
            else:
                print('Please choose an actual spell')
        elif choice == 'E':
            print(player_1_name.upper(), 'HAS BECOME ENRAGED!')
            enrage(player_1)
            print(player_1_name.upper(), "'S STATS!", player_1['Health'],
                  '|||', player_1['Rage'], '|||', player_1['Precision'])
            break
        elif choice == 'C':
            if player_1['Rage'] >= 15:
                print(player_1_name.upper(),
                      'HAS CHOSEN TO CONCENTRATE AND FOCUS HIS ENERGY!')
                player_1['Rage'] -= 15
                player_1['Mana'] += randint(15, 30)
                if player_1['Mana'] > 50:
                    player_1['Mana'] == 50
                break
            else:
                break

        elif choice == 'P':
            player_1['Rage'] += 5
            if player_1['Rage'] > 100:
                player_1['Rage'] = 100
            player_1['Precision'] += 5
            if player_1['Precision'] > 100:
                player_1['Precision'] = 100
            player_1['Mana'] += 5
            if player_1['Mana'] > 50:
                player_1['Mana'] == 50
            print(player_1_name.upper(), 'PASSES!')
            print(player_1_name.upper(), "'S STATS!", player_1['Health'],
                  '|||', player_1['Rage'], '|||', player_1['Precision'])
            break
        elif choice == 'Q':
            print(player_1_name.upper(), 'HAS FORFEITED THEIR LIFE')
            exit()
        else:
            print("PLEASE CHOOSE A VALID OPITON")


def combatant_2_turn(player_1_name, player_1, player_2_name, player_2):

    while True:

        print(player_2_name.upper(), '! It is your turn!')
        print(player_2_name.upper(), "'S STATS!\nHealth:", player_2['Health'],
              '||| Rage:', player_2['Rage'], '||| Precision:',
              player_2['Precision'], '||| Mana:', player_2['Mana'])
        print('WHAT SHALL YOU DO!?')
        print('----[A]TTACK')
        print('----[H]EAL')
        print('----[M]AGIC')
        print('----[E]NRAGE')
        print('----[C]ONCENTRATE')
        print('----[P]ASS')
        print('----[Q]UIT')
        choice = input('CHOOSE NOW!').upper().strip()
        if choice == 'A':
            print(player_2_name.upper(), 'ATTACKS', player_1_name.upper(), '!')
            attack(player_2, player_1)
            print(player_2_name.upper(), "'S STATS!", player_2['Health'],
                  '|||', player_2['Rage'], '|||', player_2['Precision'])
            print(player_1_name, "'s Health!:", player_1['Health'])
            break
        elif choice == 'H':
            print(player_2_name.upper(), 'HEALS!')
            if player_2['Health'] > 100:
                player_2['Health'] = 100
            heal(player_2)
            print(player_2_name.upper(), "'S STATS!", player_2['Health'],
                  '|||', player_2['Rage'], '|||', player_2['Precision'])
            break
        elif choice == 'M':
            print(player_2_name.upper(), 'IS CASTING A SPELL!')
            spells = magic(player_1, player_2)
            print(spells)
            spell = input('What spell shall you cast?').upper()
            if spell == 'A':
                if player_2['Mana'] >= 5:
                    player_1['Health'] -= 10
                    player_1['Precision'] -= 5
                    player_2['Mana'] -= 5
                    print(player_2_name.upper(), 'CAST AARD!')
                    print('IT DEALT 10 DAMAGE AND CAUSED',
                          player_1_name.upper(), 'TO STUMBLE!')
                    break
            elif spell == 'I':
                if player_2['Mana'] >= 15:
                    player_1['Health'] -= 20
                    player_1['Precision'] -= 10
                    player_2['Mana'] -= 15
                    print(player_2_name.upper(), 'CAST IGNI!')
                    print(
                        'FLAMES BURST FROM YOUR HAND IGNITING', player_1_name,
                        '! THE FLAMES DISPERSE QUICKLY, SLIGHTLY DISRUPTING THEIR VISION AND DEALING 20 DAMAGE! '
                    )
                    break
            elif spell == 'G':
                if player_2['Mana'] >= 25:
                    player_2['Mana'] -= 25
                    player_2['Health'] += randint(25, 45)
                    print(player_2_name.upper(), 'CASTS GREAT HEAL!')
                    print(
                        'A HEAVENLY LIGHT DESCENDS GRANTING YOU RESTORED STRENGTH'
                    )
                    break
            elif spell == 'R':
                if player_2['Mana'] == 50:
                    player_2['Mana'] -= 50
                    player_2['Health'] -= randint(0, 100)
                    player_1['Health'] -= randint(0, 100)
                    print(player_2_name.upper(), 'HAS CAUSED THE RECKONING!')
                    print(
                        'WILL ANYONE SURVIVE AS THE HEAVENS CRASH AROUND YOU AND YOUR OPPONENT!?'
                    )
                    break
            else:
                print('Please choose an actual spell')
        elif choice == 'E':
            print(player_2_name.upper(), 'HAS BECOME ENRAGED!')
            if player_2['Rage'] > 100:
                player_2['Rage'] = 100
            enrage(player_2)
            print(player_2_name.upper(), "'S STATS!", player_2['Health'],
                  '|||', player_2['Rage'], '|||', player_2['Precision'])
            break
        elif choice == 'C':
            if player_1['Rage'] >= 15:
                print(player_2_name.upper(),
                      'HAS CHOSEN TO CONCENTRATE AND FOCUS HIS ENERGY!')
                player_2['Rage'] -= 15
                player_2['Mana'] += randint(15, 30)
                if player_2['Mana'] > 50:
                    player_2['Mana'] == 50
                break
            else:
                break
        elif choice == 'P':
            player_2['Rage'] += 5
            if player_2['Rage'] > 100:
                player_2['Rage'] = 100
            player_2['Precision'] += 5
            if player_2['Precision'] > 100:
                player_2['Precision'] = 100
            player_2['Mana'] += 5
            if player_2['Mana'] > 50:
                player_2['Mana'] == 50
            print(player_2_name.upper(), 'PASSES!')
            print(player_2_name.upper(), "'S STATS!", player_2['Health'],
                  '|||', player_2['Rage'], '|||', player_2['Precision'])
            break
        elif choice == 'Q':
            print(player_2_name.upper(), 'HAS FORFEITED THEIR LIFE')
            exit()
        else:
            print("PLEASE CHOOSE A VALID OPTION")


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
    player_1 = new_gladiator(100, 15, 1, 15, 50, 10)
    player_2_name = get_name_2()
    player_2 = new_gladiator(100, 15, 1, 15, 50, 10)
    weapons = weapons_dic()
    choose_weapons(player_1_name, player_2_name, player_1, player_2, weapons)

    battle(player_1_name, player_1, player_2_name, player_2)


def main():
    game_play()


if __name__ == '__main__':
    main()
