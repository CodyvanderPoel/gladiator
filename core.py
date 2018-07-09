from random import randint


def new_gladiator(health, rage, damage_low, damage_high):
    '''Preconditions : Health must be in between 0 and 100!
                       Rage must be in between 0 and 100!
    '''
    gladiator = {
        'Health': health,
        'Rage': rage,
        'Low Attack': damage_low,
        'High Attack': damage_high
    }
    return gladiator


def attack(attacker, defender):
    crit = randint(0, 100)
    attack = randint(attacker['Low Attack'], attacker['High Attack'])
    if crit <= attacker['Rage']:
        attack = attack * 2
        attacker['Rage'] = attacker['Rage'] * 0
    else:
        attacker['Rage'] = attacker['Rage'] + 15
    defender['Health'] = defender['Health'] - attack
    return defender['Health']


def heal(gladiator):
    if gladiator['Rage'] > 10 and gladiator['Health'] <= 95:
        gladiator['Rage'] = gladiator['Rage'] - 10
        gladiator['Health'] = gladiator['Health'] + 5
        return gladiator['Health']
    else:
        return None


def is_dead(gladiator):
    if gladiator['Health'] == 0:
        return True
