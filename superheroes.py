import random

class Ability:
    def __init__(self, name, attack_strength):
        # Initialize starting values
        self.name = name
        self.attack_strength = attack_strength

    def attack(self):
        # Return attack value
        return random.randint(self.attack_strength//2, self.attack_strength)
        
    def update_attack(self, attack_strength):
        # Update attack value
        self.attack_strength = attack_strength


class Hero:
    def __init__(self, name, health=100):
        """Initialize starting values."""
        self.name = name
        self.health = health
        self.abilities = []
        self.armors = []
        self.kills = 0
        self.deaths = 0

    def add_ability(self, ability):
        """Add ability to abilities list"""
        self.abilities.append(ability)

    def attack(self):
        total = 0
        # Run attack() on every ability hero has
        for ability in self.abilities:
            total += ability.attack()
        return total
    
    def add_armor(self, Armor):
        self.armors.append(Armor)
    
    def defend(self, damage):
        defend_amt = 0
        for item in self.armors:
            defend_amt += item.defend()


class Weapon(Ability):
    def attack(self):
        """
        This method should should return a random value 
        between 0 and the full attack power of the weapon.
        """
        return random.randint(0, self.attack_strength)

class Armor():
    def __init__(self, name, defense):
        self.name = name
        self.defense = defense
    
    def defend(self):
        return random.randint(0, self.defense)

class Team:
    def __init__(self, team_name):
        """Instantiate resources."""
        self.name = team_name
        self.heroes = list()

    def add_hero(self, Hero):
        """Add Hero object to heroes list."""
        self.heroes.append(Hero)

    def remove_hero(self, name):
        """
        Remove hero from heroes list.
        If Hero isn't found return 0.
        """
        index = 0
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.pop(index)
            index += 1
        return 0

    def find_hero(self, name):
        """
        Find and return hero from heroes list.
        If Hero isn't found return 0.
        """
        for hero in self.heroes:
            if hero.name == name:
                return hero
        return 0

    def view_all_heroes(self):
        """Print out all heroes to the console."""
        print("Hello")
        for hero in self.heroes:
            print(hero.name)

    def attack(self, Team):
        total_attack = 0
        for hero in self.heroes:
            total_attack += hero.attack()
        Team.defend(total_attack)
    
    def defend(self, damage_amt):
        pass

if __name__ == "__main__":
    hero = Hero("Wonder Woman")
    print(hero.attack())
    ability = Ability("Divine Speed", 300)
    hero.add_ability(ability)
    print(hero.attack())
    new_ability = Ability("Super Human Strength", 800)
    hero.add_ability(new_ability)
    print(hero.attack())