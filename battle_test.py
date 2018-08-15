import pytest
import superheroes

# Test Armor


def test_armor():
    jodie = superheroes.Hero("Jodie Foster")
    gauntlets = superheroes.Armor("Gauntlets", 30)
    jodie.add_armor(gauntlets)
    assert len(jodie.armors) == 1
    assert jodie.armors[0].name == "Gauntlets"

# Test Hero Health


def test_hero_health():
    jodie = superheroes.Hero("Jodie Foster")
    assert jodie.health == 100
    hermes = superheroes.Hero("Hermes", 300)
    assert hermes.health == 300

# Test hero defense


def test_hero_defense():
    jodie = superheroes.Hero("Jodie Foster")
    gauntlets = superheroes.Armor("Gauntlets", 30)
    jodie.add_armor(gauntlets)
    defense = jodie.defend()
    assert defense >= 0 and defense <= 30

# Test defense with multiple armors


def test_defend_multiple():
    jodie = superheroes.Hero("Jodie Foster")
    gauntlets = superheroes.Armor("Gauntlets", 300)
    science = superheroes.Armor("Science", 200)
    jodie.add_armor(gauntlets)
    jodie.add_armor(science)
    defend = jodie.defend()
    assert defend <= 500 and defend >= 0

# Test Team Battle

def test_team_attack():
    team_one = superheroes.Team("One")
    jodie = superheroes.Hero("Jodie Foster")
    aliens = superheroes.Ability("Alien Friends", 10000)
    jodie.add_ability(aliens)
    team_one.add_hero(jodie)
    team_two = superheroes.Team("Two")
    athena = superheroes.Hero("Athena")
    dagger = superheroes.Weapon("Dagger", 10)
    athena.add_ability(dagger)
    team_two.add_hero(athena)
    result = team_one.attack(team_two)
    
    #Check for console output
    # Require team.attack() to print out 
    # Damage Done
    # Number of Heroes died
    
    assert result == 1

def test_team_battle():
    team_one = superheroes.Team("One")
    jodie = superheroes.Hero("Jodie Foster")
    team_one.add_hero(jodie)
    team_two = superheroes.Team("Two")
    athena = superheroes.Hero("Athena")
    team_two.add_hero(athena)
    result = team_one.attack(team_two)
    #Team with no weapons should fail attack
    assert result == False


