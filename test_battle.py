import pytest
import superheroes

# Test Armor
def test_armor():
    jodie = superheroes.Hero("Jodie Foster")
    gauntlets = superheroes.Armor("Gauntlets", 30)
    jodie.add_armor(gauntlets)
    assert len(jodie.armors) == 1
    assert jodie.armors[0].name == "Gauntlets"

# Test hero defense
def test_hero_defense():
    jodie = superheroes.Hero("Jodie Foster")
    gauntlets = superheroes.Armor("Gauntlets", 30)
    jodie.add_armor(gauntlets)
    defense = jodie.defend(500)
    assert  defense >= 0 and defense <= 30


#Test Team Battle
def test_team_battle():
    team_one = superheroes.Team("One")
    jodie = superheroes.Hero("Jodie Foster")
    team_one.add_hero(jodie)
    team_two = superheroes.Team("Two")
    athena = superheroes.Hero("Athena")
    team_one.attack(team_two)