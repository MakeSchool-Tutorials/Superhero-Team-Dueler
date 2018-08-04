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
        print("{} attacks with {} damage".format(self._name, attack_damage))
        return attack_damage


class Ability:
    def __init__(self, name, attack):
        self._name = name
        self._attack = attack

    def attack(self):
        return self._attack

    def update_attack(self, attack):
        self._attack = attack


if __name__ == "__main__":
    hero = Hero("Wonder Woman")
    hero.attack()
    ability = Ability("Divine Speed", 300)
    hero.add_ability(ability)
    hero.attack()
    new_ability = Ability("Super Human Strength", 800)
    hero.add_ability(new_ability)
    hero.attack()
