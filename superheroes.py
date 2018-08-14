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
    def __init__(self, name):
        """Initialize starting values."""
        self.name = name
        self.abilities = []

    def add_ability(self, ability):
        """Add ability to abilities list"""
        self.abilities.append(ability)

    def attack(self):
        total = 0
        # Run attack() on every ability hero has
        for ability in self.abilities:
            total += ability.attack()
        return total


class Weapon(Ability):
    def attack(self):
        """
        This method should should return a random value 
        between 0 and the full attack power of the weapon.
        """
        return random.randint(0, self.attack_strength)

class Team:
    def init(self, team_name):
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
        for hero in self.heroes:
            print(hero)

if __name__ == "__main__":
    hero = Hero("Wonder Woman")
    print(hero.attack())
    ability = Ability("Divine Speed", 300)
    hero.add_ability(ability)
    print(hero.attack())
    new_ability = Ability("Super Human Strength", 800)
    hero.add_ability(new_ability)
    print(hero.attack())