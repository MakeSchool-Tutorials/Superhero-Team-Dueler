import random

class Hero:
    def __init__(self, name):
        self._abilities = []
        self._name = name

    def add_ability(self, ability):
        self._abilities.append(ability)

    def attack(self):
        attack_damage = 0
        for ability in self._abilities:
            attack_damage += ability.attack()
        return attack_damage


class Ability:
    def __init__(self, name, attack):
        self._name = name
        self.attack_strength = attack

    def attack(self):
        low_attack = self.attack_strength // 2
        return random.randint(low_attack, self.attack_strength)

    def update_attack(self, attack):
        self.attack_strength = attack


if __name__ == "__main__":
    hero = Hero("Wonder Woman")
    print(hero.attack())
    ability = Ability("Divine Speed", 300)
    hero.add_ability(ability)
    print(hero.attack())
    new_ability = Ability("Super Human Strength", 800)
    hero.add_ability(new_ability)
    print(hero.attack())
