import pytest
import io
import sys
import superheroes
import math
import random

# Helper Function


def capture_console_output(function_body):
    # _io.StringIO object
    string_io = io.StringIO()
    sys.stdout = string_io
    function_body()
    sys.stdout = sys.__stdout__
    return string_io.getvalue()

# Test Abilities Class


def test_ability_instance():
    # Test instantiation without error
    big_strength = superheroes.Ability("Overwhelming Strength", 300)
    assert big_strength


def test_ability_name():
    # Test for Correct Name
    big_strength = superheroes.Ability("Overwhelming Strength", 300)
    assert big_strength.name == "Overwhelming Strength"


def test_ability_attack():
    # Test for correct attack value
    test_runs = 400
    big_strength = superheroes.Ability("Overwhelming Strength", 400)
    for _ in range(0, test_runs):
        attack = big_strength.attack()
        assert attack >= 0 and attack <= 400

# Test Weapons Class


def test_weapon_instance():
    big_stick = superheroes.Weapon("Overwhelming Stick", 200)
    assert "Weapon" in str(big_stick)


def test_weapon_attack():
    big_stick = superheroes.Weapon("Overwhelming Stick", 200)
    test_runs = 100
    for _ in range(0, test_runs):
        attack = big_stick.attack()
        assert attack <= 200 and attack >= 100

# Test Heroes Class


def test_hero_instance():
    Athena = superheroes.Hero("Athena")
    assert Athena


def test_hero_add_ability():
    big_strength = superheroes.Ability("Overwhelming Strength", 300)
    Athena = superheroes.Hero("Athena")
    assert len(Athena.abilities) == 0
    Athena.add_ability(big_strength)
    assert len(Athena.abilities) == 1
    # Check for correct type
    assert "Ability" in str(Athena.abilities[0])
    assert Athena.abilities[0].name == "Overwhelming Strength"


def test_hero_add_multi_ability():
    big_strength = superheroes.Ability("Overwhelming Strength", 300)
    speed = superheroes.Ability("Lightning Speed", 500)
    Athena = superheroes.Hero("Athena")
    assert len(Athena.abilities) == 0
    Athena.add_ability(big_strength)
    assert len(Athena.abilities) == 1
    Athena.add_ability(speed)
    assert len(Athena.abilities) == 2
    # Check for correct type
    assert "Ability" in str(Athena.abilities[0])
    assert Athena.abilities[0].name == "Overwhelming Strength"


def test_hero_attack_ability():
    big_strength = superheroes.Ability("Overwhelming Strength", 30000)
    athena = superheroes.Hero("Athena")
    assert athena.attack() == 0
    athena.add_ability(big_strength)
    attack = athena.attack()
    assert attack <= 30000 and attack >= 0


def test_hero_ability_attack_mean_value():
    athena = superheroes.Hero("Athena")
    strength = random.randint(10, 30000)
    big_strength = superheroes.Ability("Overwhelming Strength", strength)
    athena.add_ability(big_strength)
    calculated_mean = strength // 2
    iterations = 6000

    sum_of_sqr = 0
    total_attack = 0

    for _ in range(iterations): 
        attack_value = athena.attack()
        assert attack_value >= 0 and attack_value <= strength
        total_attack += attack_value
        deviation = attack_value - calculated_mean
        sum_of_sqr += deviation * deviation
    

    actual_mean = total_attack / iterations
    print("Max Allowed Damage: {}".format(strength))
    print("Attacks Tested: {}".format(iterations))
    print("Mean -- calculated: {} | actual: {}".format(calculated_mean, actual_mean))
    print("Acceptable Min: {} | Acceptable Max: {}".format(actual_mean - 150, actual_mean + 150))
    print("Tested Result: {}".format(actual_mean))
    assert actual_mean <= calculated_mean + 150 and actual_mean >= calculated_mean - 150

def test_hero_weapon_equip():
    sans = superheroes.Hero("Comic Sans")
    weapon = superheroes.Weapon("Garlic Hot Sauce", 400)
    sans.add_ability(weapon)
    assert len(sans.abilities) == 1
    assert sans.abilities[0].name == "Comic Sans"

def test_hero_weapon_attack_mean_value():
    kkrunch = superheroes.Hero("Kaptain Krunch")
    strength = random.randint(10, 30000)
    min_attack = strength // 2
    big_strength = superheroes.Weapon("Sword of Whimsy", strength)
    kkrunch.add_ability(big_strength)
    calculated_mean = (strength - min_attack) // 2 + min_attack
    iterations = 6000

    sum_of_sqr = 0
    total_attack = 0

    for _ in range(iterations): 
        attack_value = kkrunch.attack()
        assert attack_value >= min_attack and attack_value <= strength
        total_attack += attack_value
        deviation = attack_value - calculated_mean
        sum_of_sqr += deviation * deviation

    actual_mean = total_attack / iterations
    standard_dev = math.sqrt(sum_of_sqr/float(iterations))
    print("Max Allowed Damage: {}".format(strength))
    print("Attacks Tested: {}".format(iterations))
    print("Standard Deviation: {}".format(standard_dev))
    print("Mean -- calculated: {} | actual: {}".format(calculated_mean, actual_mean))
    print("Acceptable Min: {} | Acceptable Max: {}".format(actual_mean - 300, actual_mean + 300))
    print("Tested Result: {}".format(actual_mean))
    assert actual_mean <= calculated_mean + 150 and actual_mean >= calculated_mean - 150


def test_hero_attack_weapon():
    big_strength = superheroes.Ability("Overwhelming Strength", 200)
    Athena = superheroes.Hero("Athena")
    Athena.add_ability(big_strength)
    test_runs = 100
    for _ in range(0, test_runs):
        attack = big_strength.attack()
        assert attack <= 200 and attack >= 0


def test_hero_multi_weapon_attack():
    strength = superheroes.Weapon("Overwhelming Strength", 200)
    sword_of_truth = superheroes.Weapon("Sword of Truth", 700)
    Athena = superheroes.Hero("Athena")
    Athena.add_ability(strength)
    Athena.add_ability(sword_of_truth)
    assert len(Athena.abilities) == 2

    test_runs = 100
    for _ in range(0, test_runs):
        attack = Athena.attack()
        assert attack <= 900 and attack >= 0


def test_hero_weapon_ability_attack():
    quickness = superheroes.Ability("Quickness", 1300)
    sword_of_truth = superheroes.Weapon("Sword of Truth", 700)
    Athena = superheroes.Hero("Athena")
    Athena.add_ability(quickness)
    Athena.add_ability(sword_of_truth)
    assert len(Athena.abilities) == 2
    attack_avg(Athena, 0, 2000)


def attack_avg(object, low, high):
    test_runs = 100
    for _ in range(0, test_runs):
        attack = object.attack()
        assert attack <= high and attack >= low

# Test Teams


def test_team_instance():
    team = superheroes.Team("One")
    assert team


def test_team_name():
    team = superheroes.Team("One")
    assert team.name == "One"


def test_team_hero():
    team = superheroes.Team("One")
    jodie = superheroes.Hero("Jodie Foster")
    team.add_hero(jodie)
    assert len(team.heroes) == 1
    assert team.heroes[0].name == "Jodie Foster"


def test_team_remove_hero():
    team = superheroes.Team("One")
    jodie = superheroes.Hero("Jodie Foster")
    team.add_hero(jodie)
    assert team.heroes[0].name == "Jodie Foster"
    team.remove_hero("Jodie Foster")
    assert len(team.heroes) == 0


def test_team_remove_unlisted():
    # Test that if no results found return 0
    team = superheroes.Team("One")
    jodie = superheroes.Hero("Jodie Foster")
    team.add_hero(jodie)
    code = team.remove_hero("Athena")
    assert code == 0


def test_team_remove_empty_list():
    team = superheroes.Team("One")
    assert team.remove_hero("Athena") == 0


def test_print_heroes():
    team = superheroes.Team("One")
    jodie = superheroes.Hero("Jodie Foster")
    team.add_hero(jodie)
    athena = superheroes.Hero("Athena")
    team.add_hero(athena)
    output_string = capture_console_output(team.view_all_heroes)

    assert "Jodie Foster" in output_string
    assert "Athena" in output_string
