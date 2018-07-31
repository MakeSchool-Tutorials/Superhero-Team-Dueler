class Ability:

    def __init__(self, name, attack_strength, defend_strength):
        self._name = name
        self._attack_strength = attack_strength
        self._defend_strength = defend_strength

    def attack(self):
        print("{} deals {} damage".format( self._name,self._attack_strength))

    def defend(self):
        print('{} absorbs {} damage'.format(self._name, self._defend_strength))


class Relic(Ability):
    def __init__(self, name, attack_strength, defend_strength):
        Ability.__init__(self, name, attack_strength, defend_strength)

    def defend(self):
        print("{} deflects {} damage".format(self._name, self._defend_strength))


MindWarp = Ability("Mind Warp", 50, 0)
MindWarp.attack()
MindWarp.defend()

Bracelet = Relic("Bracelet of Grandiosity", 3, 45)
Bracelet.attack()
Bracelet.defend()