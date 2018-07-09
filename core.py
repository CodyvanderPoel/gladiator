from random import randint


def new_gladiator(health, rage, damage_low, damage_high):
    gladiator = {
        'Health': health,
        'Rage': rage,
        'Low Attack': damage_low,
        'High Attack': damage_high
    }
    return gladiator


def attack(attacker, defender):
    crit = randint(0,100)
    attack = attacker.randint(['Low Attack'],['High Attack'])
    if crit is <= attacker['Rage']:
        attack = attack * 2
        attacker['Rage'] = attacker['Rage'] * 0
    else:
        attacker['Rage']  = attacker['Rage'] + 15
    defender['Health'] = defender['Health'] - attack




def heal(gladiator):
    if gladiator['Rage'] > 10 and gladiator['Health'] <= 95:
        gladiator['Rage'] = gladiator['Rage'] - 10
        gladiator['Health'] = gladiator['Health'] + 5
    else:
        print('No can do amigo!')


def is_dead(gladiator):
    if gladiator['Health'] == 0:
        return True
