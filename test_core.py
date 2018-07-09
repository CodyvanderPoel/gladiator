from core import *


def test_new_gladiator():
    result = new_gladiator(75, 40, 15, 55)

    assert result == {
        'Health': 75,
        'Rage': 40,
        'Low Attack': 15,
        'High Attack': 55
    }


def test_new_gladiator_2():
    result = new_gladiator(100, 40, 1, 10)

    assert result == {
        'Health': 100,
        'Rage': 40,
        'Low Attack': 1,
        'High Attack': 10
    }


def test_new_gladiator_3():
    result = new_gladiator(0, 0, 0, 0)

    assert result == {
        'Health': 0,
        'Rage': 0,
        'Low Attack': 0,
        'High Attack': 0
    }


def test_attack():
    gladiator_a = new_gladiator(100, 15, 20, 50)
    gladiator_b = new_gladiator(80, 30, 15, 60)
    result = attack(gladiator_a, gladiator_b)
    assert result == gladiator_b['Health']


def test_attack_2():
    gladiator_a = new_gladiator(75, 55, 40, 70)
    gladiator_b = new_gladiator(100, 10, 10, 30)
    result = attack(gladiator_a, gladiator_b)
    assert result == gladiator_b['Health']


def test_attack_3():
    gladiator_a = new_gladiator(0, 0, 0, 0)
    gladiator_b = new_gladiator(0, 0, 0, 0)
    result = attack(gladiator_a, gladiator_b)
    assert result == gladiator_b['Health']


def test_heal():
    gladiator_a = new_gladiator(100, 15, 20, 50)
    result = heal(gladiator_a)
    assert result == None


def test_heal_2():
    gladiator_a = new_gladiator(95, 15, 20, 50)
    result = heal(gladiator_a)
    assert result == gladiator_a['Health']


def test_heal_3():
    gladiator_a = new_gladiator(75, 55, 20, 50)
    result = heal(gladiator_a)
    assert result == gladiator_a['Health']


def test_heal_4():
    gladiator_a = new_gladiator(80, 5, 20, 50)
    result = heal(gladiator_a)
    assert result == None


def test_is_dead():
    gladiator_a = new_gladiator(0, 30, 20, 50)
    result = is_dead(gladiator_a)
    assert result == True


def test_is_dead_2():
    gladiator_a = new_gladiator(100, 30, 20, 50)
    result = is_dead(gladiator_a)
    assert result == None


def test_is_dead_3():
    gladiator_a = new_gladiator(10, 30, 20, 50)
    result = is_dead(gladiator_a)
    assert result == None
