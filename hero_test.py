import pytest
import superheroes

#Test Abilities
def test_ability_instance():
    # Test instantiation without error
    big_strength = superheroes.Ability("Overwhelming Strength", 300)
    assert big_strength

def test_ability_name():
    # Test for Correct Name
    big_strength = superheroes.Ability("Overwhelming Strength", 300)
    assert big_strength.name == "Overwhelming Strength"    

def test_ability_update_attack():
    big_strength = superheroes.Ability("Overwhelming Strength", 300)
    big_strength.update_attack(400)
    test_runs = 100
    attack = 0
    for _ in range(0, test_runs):
        attack += big_strength.attack()
    assert attack <= (400 * test_runs) and attack >= (200 * test_runs)

def test_ability_attack():
    # Test for correct attack value
    test_runs = 100
    big_strength = superheroes.Ability("Overwhelming Strength", 400)
    for _ in range(0, test_runs):
        attack = big_strength.attack()
        assert attack <= 400  and attack >= 200 

# Test Weapons
def test_weapon_instance():
    big_stick = superheroes.Weapon("Overwhelming Stick", 200)
    assert "Weapon" in str(big_stick)

def test_weapon_attack():
    big_stick = superheroes.Weapon("Overwhelming Stick", 200)
    test_runs = 100
    for _ in range(0, test_runs):
        attack = big_stick.attack()
        assert attack <= 200  and attack >= 0 

#Test Heroes
def test_hero_instance():
    Athena = superheroes.Hero("Athena")
    assert Athena

def test_hero_add_ability():
    big_strength = superheroes.Ability("Overwhelming Strength", 300)
    Athena = superheroes.Hero("Athena")
    assert len(Athena.abilities) == 0
    Athena.add_ability(big_strength)
    assert len(Athena.abilities) == 1
    #Check for correct type
    assert "Ability" in str(Athena.abilities[0])
    assert Athena.abilities[0].name == "Overwhelming Strength"

def test_hero_attack_ability():
    big_strength = superheroes.Ability("Overwhelming Strength", 300)
    Athena = superheroes.Hero("Athena")
    assert Athena.attack() == 0
    Athena.add_ability(big_strength)

def test_hero_attack_weapon():
    big_stick = superheroes.Weapon("Overwhelming Stick", 200)
    Athena = superheroes.Hero("Athena")
    Athena.add_ability(big_stick)
    test_runs = 100
    for _ in range(0, test_runs):
        attack = big_stick.attack()
        assert attack <= 200  and attack >= 0

def test_hero_multi_weapon_attack():
    big_stick = superheroes.Weapon("Overwhelming Stick", 200)
    sword_of_truth = superheroes.Weapon("Sword of Truth", 700)
    Athena = superheroes.Hero("Athena")
    Athena.add_ability(big_stick)
    Athena.add_ability(sword_of_truth)
    assert len(Athena.abilities) == 2

    test_runs = 100
    for _ in range(0, test_runs):
        attack = Athena.attack()
        assert attack <= 900  and attack >= 0    

def test_hero_weapon_ability_attack():
    quickness = superheroes.Ability("Quickness", 1300)
    sword_of_truth = superheroes.Weapon("Sword of Truth", 700)
    Athena = superheroes.Hero("Athena")
    Athena.add_ability(quickness)
    Athena.add_ability(sword_of_truth)
    assert len(Athena.abilities) == 2
    test_runs = 100
    for _ in range(0, test_runs):
        attack = Athena.attack()
        assert attack <= 2000  and attack >= 0

