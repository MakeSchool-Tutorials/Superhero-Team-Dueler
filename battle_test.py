import pytest
import superheroes
import random
import io
import sys

#Helper Functions
def capture_console_output(function_body):
    # _io.StringIO object
    string_io = io.StringIO()
    sys.stdout = string_io
    function_body()
    sys.stdout = sys.__stdout__
    return string_io.getvalue()

def create_armor():
    armors = ["Calculator", "Laser Shield", "Invisibility", "SFPD Strike Force", "Social Workers", "Face Paint", "Damaskus Shield", "Bamboo Wall", "Forced Projection", "Thick Fog", "Wall of Will", "Wall of Walls", "Obamacare", "Thick Goo"]
    name = armors[random.randint(0, len(armors)-1)]
    power = random.randint(23, 700000)
    return superheroes.Armor(name, power)

def create_weapon():
    weapons = ["Antimatter Gun", "Star Cannon", "Black Hole Ram Jet", "Laser Sword", "Laser Cannon", "Ion Accellerated Disc Drive", "Superhuman Strength", "Blinding Lights", "Ferociousness", "Speed of Hermes", "Lightning Bolts"]
    name = weapons[random.randint(0, len(weapons)-1)]
    power = random.randint(27, 700000)
    return superheroes.Weapon(name, power)

def create_ability():
    abilities = ["Alien Attack", "Science", "Star Power", "Immortality", "Grandmas Cookies", "Blinding Strength", "Cute Kittens", "Team Morale", "Luck", "Obsequious Destruction", "The Kraken", "The Fire of A Million Suns", "Team Spirit", "Canada"]
    name = abilities[random.randint(0, len(abilities)-1)]
    power = random.randint(45, 700000)
    return superheroes.Ability(name, power)

def create_hero(weapons=False, armor=False):
    heroes = ["Athena", "Jodie Foster", "Christina Aguilera", "Gamora", "Supergirl", "Wonder Woman", "Batgirl", "Carmen Sandiego", "Okoye", "America Chavez", "Cat Woman", "White Canary", "Nakia", "Mera", "Iris West", "Quake", "Wasp", "Storm", "Black Widow", "Yemaya", "San Luis Obispo", "Ted Kennedy", "San Francisco", "Bananas" ]
    name = heroes[random.randint(0, len(heroes)-1)]
    power = random.randint(3, 700000)
    hero = superheroes.Hero(name, power)
    if weapons and armor:
        for weapon in weapons:
            hero.add_ability(weapon)
        for armor in armor:
            hero.add_armor(armor)
    return hero

def create_team(heroes=[]):
    teams = ["Orchids", "Red", "Blue", "Cheese Steaks", "Warriors", "49ers", "Marvel", "DC", "Rat Pack", "The Little Red Riding Hoods", "Team One", "Generic Team", "X-men", "Team Two", "Golden Champions", "Vegan Protectors", "The Cardinals", "Winky Bears", "Steelsmiths", "Boilermakers", "Nincompoops"]
    name = teams[random.randint(0, len(teams)-1)]
    team = superheroes.Team(name)
    if len(heroes)>0:
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


# Test Armor
def test_armor():
    armor = superheroes.Hero("The Ring", 200)
    for _ in range(0, 500):
        defense = armor.defend() <= 200
        assert (defense <= 200 and defense >= 0)



# Test Hero Health


def test_hero_default_health():
    jodie = superheroes.Hero("Jodie Foster")
    assert jodie.health == 100


def test_hero_init_new_health():
    hero = superheroes.Hero("Jodie Foster", 600)
    assert hero.health == 600


def test_hero_start_health():
    hero = superheroes.Hero("Jodie Foster", 300)
    assert hero.start_health == 300

def test_hero_equip_armor():
    jodie = superheroes.Hero("Jodie Foster")
    gauntlets = superheroes.Armor("Gauntlets", 30)
    jodie.add_armor(gauntlets)
    assert len(jodie.armors) == 1
    assert jodie.armors[0].name == "Gauntlets"

def test_hero_attack():
    flash = superheroes.Hero("The Flash")
    assert flash.attack() == 0
    pesto = superheroes.Ability("Pesto Sauce", 8000)
    flash.add_ability(pesto)
    attack = flash.attack()
    assert attack <= 8000 and attack >= 4000


def test_hero_defense():
    jodie = superheroes.Hero("Jodie Foster")
    gauntlets = superheroes.Armor("Gauntlets", 30)
    jodie.add_armor(gauntlets)
    defense = jodie.defend()
    assert defense >= 0 and defense <= 30


def test_dead_hero_defense():
    hero = superheroes.Hero("Vlaad", 0)
    garlic = superheroes.Armor("Garlic", 30000)
    hero.add_ability(garlic)
    assert hero.defend() == 0


def test_hero_defend_multi_armor():
    jodie = superheroes.Hero("Jodie Foster")
    gauntlets = superheroes.Armor("Gauntlets", 4000)
    science = superheroes.Armor("Science", 9000)
    jodie.add_armor(gauntlets)
    jodie.add_armor(science)
    defend = jodie.defend()
    assert defend <= 13000 and defend >= 0

# Test Team Battle


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
    result = team_one.attack(team_two)

    assert result == 1


def test_team_battle():
    
    heroes = []

    for _ in range(0, 500):
        hero_set = create_set()
        heroes.append(create_hero(hero_set["weapons"], hero_set["armors"]))
    
    team_one = create_team(heroes)

    heroes = []

    for _ in range(0, 500):
        hero_set = create_set()
        heroes.append(create_hero(hero_set["weapons"], hero_set["armors"]))


    team_two = create_team(heroes)

    team_one.battle(team_two)

