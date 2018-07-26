import pytest
import team

def test_ability():
    #Test Correct Instantiation without error
    big_strength = team.Ability("Overwhelming Strength", 300, 300)
    assert big_strength

    #Test for Correct Name
    assert big_strength.get_name() == "Overwhelming Strength"

    #Test for correct update
    big_strength.update(400, 400)
    assert big_strength.stats().find("Overwhelming Strength (400/400)") > 0
    attack = big_strength.attack()
    assert attack <= 400 and attack >= 0
    defend = big_strength.defend()
    assert defend <= 400 and defend >= 0

    big_wallet = team.Ability("Vast Sums of Money", 1200, 0)
    assert big_wallet.stats().find("Overwhelming Strength (1200/0)")

    for _ in range(0,100):
        a = attack_ability(big_wallet) 
        d = defend_ability(big_wallet)

        assert a > 0 and a <= 1200
        assert d == 0
    
    bright_light = team.Ability("Bright Flashing Lights", 0, 100)
    for _ in range(0, 200):
        a = attack_ability(bright_light) 
        d = defend_ability(bright_light)

        assert a == 0
        assert d >= 0 and d <= 100


def test_relic():


def test_hero():
    big_strength = team.Ability("Overwhelming Strength", 300, 300)
    Athena = team.Hero("Athena")

    assert Athena

    Athena.add_ability(big_strength)

    with pytest.raises(Exception) as ability_e:
        Athena.add_ability("Lightning Speed")
        print(type(big_strength))
        print(big_strength.__class__)

    assert str(ability_e.value) == "Not an Ability"
    
    Zeus = team.Hero("Zeus")
    assert Zeus

    Mickey_Mouse = team.Hero("Mickey Mouse")
    assert Mickey_Mouse

    Jodie_Foster = team.Hero("Jodie Foster")
    assert Jodie_Foster


def test_team():
    marvel = team.Team("Marvel")
    assert marvel


def attack_ability(ability):
    return ability.attack()

def defend_ability(ability):
    return ability.defend()