class Team:
    def __init__(self, name):
        self._name = name
        self._heroes = []
        self._k_d = {}

    def add_hero(self, name):
        self._heroes.append(name)

    def remove_hero(self, name):
        index = 0
        for hero in self._heroes:
            if hero.get_name() == name:
                self._heroes.pop(index)
            index += 1
 
    def find_hero(self, name):
        for hero in self._heroes:
            if hero.get_name() == name:
                return hero

    def view_all_heroes(self):
        print("Current Heroes in Team {}:".format(self._name))
        for hero in self._heroes:
            print(hero)
            # print(hero.get_name(), type(hero.get_name()))
            # print(hero.name, 'type:', type(hero.name))
            # if hero.name != hero.get_name():
            #     print('Hero name mismatch:', hero)

    def best(self, number):
        """
        This method will show the top n most effective team members.
        """
        pass

    def worst(self, number):
        """
        This method will show the n least effective team members.
        """
        pass

    def battle(self, other_team):
        pass


class Hero:
    def __init__(self, name, abilities=None, weapons=None, relics=None):
        self.name = name
        self._wins = 0
        self._losses = 0

        if abilities is None:
            abilites = []
        self._abilities = abilites
        if weapons is None:
            weapons = []
        self._weapons = weapons
        if relics is None:
            relics = []
        self._relics = relics

    def __repr__(self):
        arguments = ''
        if self._abilities:
            arguments += ', abilities={!r}'.format(self._abilities)
        if self._weapons:
            arguments += ', weapons={!r}'.format(self._weapons)
        if self._relics:
            arguments += ', relics={!r}'.format(self._relics)
        return 'Hero({!r}{})'.format(self.name, arguments)

    def __str__(self):
        powers = ''
        if self._abilities:
            abilites = ', '.join(str(ability) for ability in self._abilities)
            powers += '\n  {} abilities: {}'.format(len(self._abilities), abilites)
        if self._weapons:
            weapons = ', '.join(str(weapon) for weapon in self._weapons)
            powers += '\n  {} weapons: {}'.format(len(self._weapons), weapons)
        if self._relics:
            relics = ', '.join(str(relic) for relic in self._relics)
            powers += '\n  {} relics: {}'.format(len(self._relics), relics)
        return self.name + (' has:' + powers if len(powers) > 0 else '')

    def get_name(self):
        return self.name

    def add_ability(self, ability):
        self._abilities.append(ability)

    def view_abilities(self):
        for ability in self._abilities:
            print(ability.stats())

    def find_ability(self, ability):
        for ability in self._abilities:
            if ability.name == ability:
                return ability
        return False          

    def update_ability(self, name, attack, defense):
        ability = self.find_ability(name)
        if ability:
            ability.update(attack, defense)
        else:
            print("Ability not found!")     

    def remove_ability(self, name):
        index = 0
        for ability in self._abilities:
            if ability.name == name:
                self._abilities.pop(index)
                return 1
            index += 1

    def add_relic(self, relic):
        self._relics.append(relic)

    def view_relics(self):
        for relic in self._relics:
            print(relic.stats())

    def find_relic(self, name):
        for relic in self._relics:
            if relic.name == name:
                return relic
        return False

    def update_relic(self, name, attack, defend):
        relic = self.find_relic(name)
        relic.update(attack, defend)

    def remove_relic(self, name):
        index = 0
        for relic in self._relics:
            if relic.name == name:
                self._relics.pop(index)
            index += 1

    def add_weapon(self, weapon):
        self._weapons.append(weapon)

    def view_weapons(self):
        pass

    def find_weapon(self, name):
        for weapon in self._weapons:
            if weapon.name == name:
                return weapon
        print("Weapon not found!")

    def remove_weapon(self, name):
        index = 0
        for weapon in self._weapons:
            if weapon.get_name() == name:
                self._weapons.pop(index)
            index += 1

    def update_weapon(self, weapon):
        pass

    def stats(self):
        # print("Stats!")
        ...


class Ability:
    def __init__(self, name, attack_strength, defend_strength):
        self._name = name
        self._attack_strength = attack_strength
        self._defend_strength = defend_strength

    def __repr__(self):
        return '{}({!r}, {!r}, {!r})'.format(self.__class__.__name__, self._name,
                                             self._attack_strength, self._defend_strength)

    def __str__(self):
        return '{} ({}/{})'.format(self._name, self._attack_strength, self._defend_strength)

    def get_name(self):
        return self._name

    def attack(self):
        print(
            self._name + " deals "
            + str(self._attack_strength)
            + " damage."
        )

    def defend(self):
        print(
            self._name + " absorbs "
            + str(self._defend_strength)
            + " damage."
        )
    
    def update(self, attack, defense):
        self._attack_strength = attack
        self._defend_strength = defense

    def stats(self):
        print(self._name + " deals " + self._attack_strength + " and defends against " + self._defend_strength + " damage.")


class Relic(Ability):
    def __init__(self, name, attack_strength, defend_strength):
        Ability.__init__(self, name, attack_strength, defend_strength)

    def get_name(self):
        return self._name

    def defend(self):
        print(
            self._name + " deflects "
            + str(self._defend_strength)
            + " damage."
        )


class Weapon(Ability):
    def __init__(self, name, attack_strength):
        Ability.__init__(self, name, attack_strength, 0)

    def attack(self):
        print(self._name + " attacks for " + self._attack_strength + " damage.")


def get_user_input(prompt):
    user_input = input(prompt)
    return user_input