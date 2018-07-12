from core import *


def test_new_gladiator():
    result = new_gladiator(75, 40, 15, 55, 100, 45)

    assert result == {
        'Health': 75,
        'Rage': 40,
        'Low Attack': 15,
        'High Attack': 55,
        'Precision': 100,
        'Mana': 45
    }


def test_new_gladiator_2():
    result = new_gladiator(100, 40, 1, 10, 100, 30)

    assert result == {
        'Health': 100,
        'Rage': 40,
        'Low Attack': 1,
        'High Attack': 10,
        'Precision': 100,
        'Mana': 30
    }


def test_new_gladiator_3():
    result = new_gladiator(0, 0, 0, 0, 0, 0)

    assert result == {
        'Health': 0,
        'Rage': 0,
        'Low Attack': 0,
        'High Attack': 0,
        'Precision': 0,
        'Mana': 0
    }


def test_attack():
    gladiator_a = new_gladiator(100, 15, 20, 50, 100, 25)
    gladiator_b = new_gladiator(80, 30, 15, 60, 100, 25)
    result = attack(gladiator_a, gladiator_b)
    assert result == gladiator_b['Health']


def test_attack_2():
    gladiator_a = new_gladiator(75, 55, 40, 70, 100, 25)
    gladiator_b = new_gladiator(100, 10, 10, 30, 100, 25)
    result = attack(gladiator_a, gladiator_b)
    assert result == gladiator_b['Health']


def test_attack_3():
    gladiator_a = new_gladiator(0, 0, 0, 0, 0, 0)
    gladiator_b = new_gladiator(0, 0, 0, 0, 0, 0)
    result = attack(gladiator_a, gladiator_b)
    assert result == None


def test_heal():
    gladiator_a = new_gladiator(100, 15, 20, 50, 100, 50)
    result = heal(gladiator_a)
    assert result == None


def test_heal_2():
    gladiator_a = new_gladiator(95, 15, 20, 50, 100, 35)
    result = heal(gladiator_a)
    assert result == gladiator_a['Health']


def test_heal_3():
    gladiator_a = new_gladiator(75, 55, 20, 50, 100, 35)
    result = heal(gladiator_a)
    assert result == gladiator_a['Health']


def test_heal_4():
    gladiator_a = new_gladiator(80, 5, 20, 50, 100, 35)
    result = heal(gladiator_a)
    assert result == None


def test_heal_5():
    gladiator_a = new_gladiator(99, 15, 20, 50, 100, 35)
    result = heal(gladiator_a)
    assert result == None


def test_heal_6():
    gladiator_a = new_gladiator(90, 10, 20, 50, 100, 35)
    result = heal(gladiator_a)
    assert result == gladiator_a['Health']


def test_enrage():
    gladiator = new_gladiator(20, 0, 10, 15, 100, 35)
    result = enrage(gladiator)
    assert result == None


def test_enrage2():
    gladiator = new_gladiator(100, 76, 10, 15, 100, 20)
    result = enrage(gladiator)
    assert result == gladiator['Rage']


def test_enrage3():
    gladiator = new_gladiator(0, 0, 10, 15, 100, 20)
    result = enrage(gladiator)
    assert result == None


def test_enrage4():
    gladiator = new_gladiator(100, 0, 10, 15, 100, 35)
    result = enrage(gladiator)
    assert result == gladiator['Rage']


def test_is_dead():
    gladiator_a = new_gladiator(0, 30, 20, 50, 100, 35)
    result = is_dead(gladiator_a)
    assert result == True


def test_is_dead_2():
    gladiator_a = new_gladiator(100, 30, 20, 50, 100, 15)
    result = is_dead(gladiator_a)
    assert result == None


def test_is_dead_3():
    gladiator_a = new_gladiator(10, 30, 20, 50, 100, 15)
    result = is_dead(gladiator_a)
    assert result == None


def test_is_dead_4():
    gladiator_a = new_gladiator(-10, 30, 20, 50, 100, 15)
    result = is_dead(gladiator_a)
    assert result == True
