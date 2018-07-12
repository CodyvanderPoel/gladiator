from random import randint


def new_gladiator(health, rage, damage_low, damage_high, precision, mana):
    '''Preconditions : Health must be in between 0 and 100!
                       Rage must be in between 0 and 100!
    '''
    gladiator = {
        'Health': health,
        'Rage': rage,
        'Low Attack': damage_low,
        'High Attack': damage_high,
        'Precision': precision,
        'Mana': mana
    }
    return gladiator


def paladin():
    paladin = new_gladiator(115, 0, 25, 40)
    return paladin


def barbarian():
    barbarian = new_gladiator(75, 50, 25, 35)
    return barbarian


def weapons_dic():
    weapons = {
        'Sword': 'Sword',
        'Sword Attack': 10,
        'Sword Rage': 5,
        'War Axe': 'War Axe',
        'War Axe Attack': 5,
        'War Axe Rage': 10
    }
    return weapons


def attack(attacker, defender):
    hit_chance = randint(0, 100)
    crit = randint(0, 100)
    if hit_chance <= attacker['Precision']:
        attack = randint(attacker['Low Attack'], attacker['High Attack'])
        if crit <= attacker['Rage']:
            attack = attack * 2
            attacker['Rage'] = attacker['Rage'] * 0
            attacker['Precision'] = attacker['Precision'] * .75
            defender['Precision'] = defender['Precision'] * .95
            print('CRITICAL!', attack, 'DAMAGE DONE!')
        else:
            attacker['Rage'] = attacker['Rage'] + 15
            print('THE ATTACK LANDED! IT DEALT THIS MUCH DAMAGE!', attack)
        health = defender['Health'] - attack
        defender['Health'] = max(health, 0)

        return defender['Health']
    else:
        print('THE ATTACK MISSED!')
        return None


def magic(attacker, defender):
    spells = [
        '[A]ard Requirements : 5 Mana', '[I]gni Requirements : 15 Mana',
        '[G]reat Heal Requirements: 25 Mana',
        '[R]eckoning Requirements: 50 Mana'
    ]
    return spells


def heal(gladiator):
    if gladiator['Rage'] >= 10 and gladiator['Health'] <= 95:
        gladiator['Rage'] = gladiator['Rage'] - 10
        health = gladiator['Health'] + 5
        gladiator['Health'] = min(100, health)
        return gladiator['Health']
    else:
        return None


def enrage(gladiator):
    if gladiator['Health'] >= 21:
        gladiator['Health'] -= 20
        enraged = randint(25, 75)
        gladiator['Rage'] += enraged
        if gladiator['Rage'] > 100:
            gladiator['Rage'] = 100
        return gladiator['Rage']
    else:
        return None


def is_dead(gladiator):
    if gladiator['Health'] <= 0:
        return True
