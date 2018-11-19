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


def create_armor():
    armors = [
        "Calculator",
        "Laser Shield",
        "Invisibility",
        "SFPD Strike Force",
        "Social Workers",
        "Face Paint",
        "Damaskus Shield",
        "Bamboo Wall",
        "Forced Projection",
        "Thick Fog",
        "Wall of Will",
        "Wall of Walls",
        "Obamacare",
        "Thick Goo"]
    name = armors[random.randint(0, len(armors) - 1)]
    power = random.randint(23, 700000)
    return superheroes.Armor(name, power)


def create_weapon():
    weapons = [
        "Antimatter Gun",
        "Star Cannon",
        "Black Hole Ram Jet",
        "Laser Sword",
        "Laser Cannon",
        "Ion Accellerated Disc Drive",
        "Superhuman Strength",
        "Blinding Lights",
        "Ferociousness",
        "Speed of Hermes",
        "Lightning Bolts"]
    name = weapons[random.randint(0, len(weapons) - 1)]
    power = random.randint(27, 700000)
    return superheroes.Weapon(name, power)


def create_ability():
    abilities = [
        "Alien Attack",
        "Science",
        "Star Power",
        "Immortality",
        "Grandmas Cookies",
        "Blinding Strength",
        "Cute Kittens",
        "Team Morale",
        "Luck",
        "Obsequious Destruction",
        "The Kraken",
        "The Fire of A Million Suns",
        "Team Spirit",
        "Canada"]
    name = abilities[random.randint(0, len(abilities) - 1)]
    power = random.randint(45, 700000)
    return superheroes.Ability(name, power)


def build_hero(num_of_weapons=0, num_of_armor=0, num_of_abilities=0):
    heroes = [
        "Athena",
        "Jodie Foster",
        "Christina Aguilera",
        "Gamora",
        "Supergirl",
        "Wonder Woman",
        "Batgirl",
        "Carmen Sandiego",
        "Okoye",
        "America Chavez",
        "Cat Woman",
        "White Canary",
        "Nakia",
        "Mera",
        "Iris West",
        "Quake",
        "Wasp",
        "Storm",
        "Black Widow",
        "San Luis Obispo",
        "Ted Kennedy",
        "San Francisco",
        "Bananas"]

    weapons = []
    armors = []

    for _ in range(num_of_weapons):
        weapons.append(create_weapon())

    for _ in range(num_of_armor):
        armors.append(create_armor())

    for _ in range(num_of_abilities):
        weapons.append(create_ability())

    name = random.choice(heroes)
    hero = superheroes.Hero(name)

    for item in weapons:
        hero.add_ability(item)

    for armor in armors:
        hero.add_armor(armor)

    return hero


def create_hero(max_strength=100, weapons=False, armors=False, health=False):

    heroes = [
        "Athena",
        "Jodie Foster",
        "Christina Aguilera",
        "Gamora",
        "Supergirl",
        "Wonder Woman",
        "Batgirl",
        "Carmen Sandiego",
        "Okoye",
        "America Chavez",
        "Cat Woman",
        "White Canary",
        "Nakia",
        "Mera",
        "Iris West",
        "Quake",
        "Wasp",
        "Storm",
        "Black Widow",
        "San Luis Obispo",
        "Ted Kennedy",
        "San Francisco",
        "Bananas"]
    name = heroes[random.randint(0, len(heroes) - 1)]
    if health:
        power = health
    else:
        power = random.randint(3, 700000)
    hero = superheroes.Hero(name, power)
    if weapons and armors:
        for weapon in weapons:
            hero.add_ability(weapon)
        for armor in armors:
            hero.add_armor(armor)
    if armors and not weapons:
        for armor in armors:
            hero.add_armor(armor)

    return hero


def create_team(heroes=[]):
    teams = [
        "Orchids",
        "Red",
        "Blue",
        "Cheese Steaks",
        "Warriors",
        "49ers",
        "Marvel",
        "DC",
        "Rat Pack",
        "The Little Red Riding Hoods",
        "Team One",
        "Generic Team",
        "X-men",
        "Team Two",
        "Golden Champions",
        "Vegan Protectors",
        "The Cardinals",
        "Winky Bears",
        "Steelsmiths",
        "Boilermakers",
        "Nincompoops"]

    name = teams[random.randint(0, len(teams) - 1)]
    team = superheroes.Team(name)
    if len(heroes) > 0:
        for member in heroes:
            team.add_hero(member)

    return team


def create_set():
    armor_pieces = random.randint(1, 300)
    weapon_pieces = random.randint(1, 300)
    ability_ct = random.randint(1, 300)
    armors = []
    abilities = []
    for _ in range(0, armor_pieces):
        armors.append(create_armor())
    for _ in range(0, weapon_pieces):
        abilities.append(create_weapon())
    for _ in range(0, ability_ct):
        abilities.append(create_ability())

    hero_set = {'weapons': abilities, 'armors': armors}
    return hero_set


def test_armor():
    armor = superheroes.Hero("The Ring", 200)
    for _ in range(0, 500):
        defense = armor.defend()
        assert (defense <= 200 and defense >= 0)


def test_hero_default_health():
    jodie = superheroes.Hero("Jodie Foster")
    assert jodie.current_health == 100


def test_hero_init_new_health():
    hero = superheroes.Hero("Jodie Foster", 600)
    assert hero.current_health == 600


def test_hero_start_health():
    hero = superheroes.Hero("Jodie Foster", 300)
    assert hero.starting_health == 300


def test_hero_defense():
    jodie = superheroes.Hero("Jodie Foster")
    gauntlets = superheroes.Armor("Gauntlets", 30)
    jodie.add_armor(gauntlets)
    defense = jodie.defend()
    assert defense >= 0 and defense <= 30


def test_hero_defense_mean_value():
    athena = superheroes.Hero("Athena")
    strength = random.randint(400, 30000)
    big_strength = superheroes.Armor("Overwhelming Shield", strength)
    athena.add_armor(big_strength)
    calculated_mean = strength // 2
    iterations = 8000
    total_attack = 0
    accepted_window = 400
    for _ in range(iterations):
        attack_value = athena.defend()
        assert attack_value >= 0 and attack_value <= strength
        total_attack += attack_value

    actual_mean = total_attack / iterations
    print("Max Allowed: {}".format(strength))
    print("Defenses Tested: {}".format(iterations))
    print("Mean -- calculated: {} | actual: {}".format(calculated_mean, actual_mean))
    print(
        "Acceptable deviation from mean: {} | Current deviation from mean: {}".format(
            accepted_window, abs(
                calculated_mean - actual_mean)))
    print(
        "Acceptable Min: {} | Acceptable Max: {}".format(
            actual_mean -
            accepted_window,
            actual_mean +
            accepted_window))
    assert actual_mean <= calculated_mean + \
        accepted_window and actual_mean >= calculated_mean - accepted_window


def test_hero_defense_standard_deviation():
    willow_waffle = superheroes.Hero("Willow Waffle")
    strength = random.randint(400, 30000)
    willow = superheroes.Armor("Willowness", strength)
    willow_waffle.add_armor(willow)
    defenses = list()
    total_defend = 0
    number_tests = 100
    for _ in range(number_tests):
        defense = willow_waffle.defend()
        defenses.append(defense)
        total_defend += defense
    mean = total_defend / number_tests

    # Get Square Deviations
    for index, value in enumerate(defenses):
        defenses[index] = math.pow(value - mean, 2)

    standard_dev = math.sqrt(sum(defenses) / len(defenses))
    print("Hero Armor must block with random value.")
    print("Standard Deviation Cannot be 0.")
    assert standard_dev != 0.0


def test_dead_hero_defense():
    hero = superheroes.Hero("Vlaad", 0)
    garlic = superheroes.Armor("Garlic", 30000)
    hero.add_ability(garlic)
    assert hero.defend() == 0


def test_hero_equip_armor():
    jodie = superheroes.Hero("Jodie Foster")
    gauntlets = superheroes.Armor("Gauntlets", 30)
    jodie.add_armor(gauntlets)
    assert len(jodie.armors) == 1
    assert jodie.armors[0].name == "Gauntlets"


def test_hero_defend_multi_armor():
    jodie = superheroes.Hero("Jodie Foster")
    gauntlets = superheroes.Armor("Gauntlets", 4000)
    science = superheroes.Armor("Science", 9000)
    jodie.add_armor(gauntlets)
    jodie.add_armor(science)
    defend = jodie.defend()
    assert defend <= 13000 and defend >= 0


# Test Team


def test_team_attack():
    team_one = superheroes.Team("One")
    jodie = superheroes.Hero("Jodie Foster")
    aliens = superheroes.Ability("Alien Friends", 10000)
    jodie.add_ability(aliens)
    team_one.add_hero(jodie)
    team_two = superheroes.Team("Two")
    athena = superheroes.Hero("Athena")
    socks = superheroes.Armor("Socks", 10)
    athena.add_armor(socks)
    team_two.add_hero(athena)
    assert team_two.heroes[0].current_health == 100

    team_one.attack(team_two)

    assert team_two.heroes[0].current_health <= 0


def test_team_attack_kills():
    team_one = superheroes.Team("One")
    jodie = superheroes.Hero("Jodie Foster")
    aliens = superheroes.Ability("Alien Friends", 10000)
    jodie.add_ability(aliens)
    team_one.add_hero(jodie)
    team_two = superheroes.Team("Two")
    athena = superheroes.Hero("Athena")
    socks = superheroes.Armor("Socks", 10)
    athena.add_armor(socks)
    team_two.add_hero(athena)
    assert team_one.heroes[0].kills == 0
    team_one.attack(team_two)
    assert team_one.heroes[0].kills == 1


def test_team_attack_deaths():
    team_one = superheroes.Team("One")
    jodie = superheroes.Hero("Jodie Foster")
    aliens = superheroes.Ability("Alien Friends", 10000)
    jodie.add_ability(aliens)
    team_one.add_hero(jodie)
    team_two = superheroes.Team("Two")
    athena = superheroes.Hero("Athena")
    socks = superheroes.Armor("Socks", 10)
    athena.add_armor(socks)
    team_two.add_hero(athena)
    assert team_two.heroes[0].deaths == 0
    team_one.attack(team_two)
    assert team_two.heroes[0].deaths == 1


def test_revive_heroes():
    heroes = []
    for _ in range(0, 20):
        heroes.append(build_hero(4, 4, 4))

    team_one = superheroes.Team("One")
    for hero in heroes:
        team_one.add_hero(hero)

    for hero in team_one.heroes:
        hero.current_health == 12
    team_one.revive_heroes()

    for hero in team_one.heroes:
        assert hero.current_health == 100
