---
title: Here There Be Dragons
slug: dragons
---
## Add fight functionality
We've got most everything together but we don't have the ability to have our teams duel each other just yet. We'll need another class and a few more properties in order to get this ability.

```python
class Armor:
    def __init__(self, name, defense):
        """Instantiate name and defense strength."""
        self.name = name
        self.defense = defense
    
    def defend(self):
        """Return a random value between 0 and the full defend strength."""
```
Our super heroes should have armor that they can wear to help defend themselves. Not only that, but they also need an amount of health that they can lose in a fight. Fortunately we have all the skill to do this.

Implement the defend method so that it returns a random integer between 0 and the full defend strength.

### Add health to Hero class
In the Hero class's constructor add a third parameter for health as such.

```python
class Hero:
    def __init__(self, name, health=100):
        # add the following to the code you already have written here
        self.armors = list()
        self.health = health
    
    def defend(self):
        """
        This method should run the defend method on each piece of armor and calculate the total defense. 
        """

    def take_damage(self, damage_amt):
        """
        This method should subtract the damage amount from the health. 

        If the hero dies return 1 and update number of deaths.

        Otherwise return 0
        """
```
We will need to implement a new methods in our Hero class that will calculate our hero's defense strength and update the health of our hero if damage is taken.

## Update Team Class with Attack and Defend Methods

```python
class Team:
    # Keep all your current code, but add these methods
    def attack(self, other_team:
        """
        This method should total our teams attack strength and 
        call the defend() method on the rival team that is passed in.
        """

    def defend(self, damage_amt):
        """
        This method should calculate our team's total defense.
        Any damage in excess of our team's total defense should be evenly distributed amongst all heroes with the deal_damage() method.
        """
    
    def deal_damage(self, damage):
        """
        Divide the total damage amongst all heroes.
        Return the number of heros that died in attack.
        """

    def revive_heroes(self, health=100):
        """
        This method should reset all heroes health.
        Stretch Challenge: Let heroes start with different amounts of health.
        """
    
    def stats(self):
        """
        This method should print the ratio of kills/deaths for each member of the team to the screen. 

        This data must be output to the terminal.
        """
```

Just as each hero needed a defend method, our Team needs to be able to coordinate our hero's attacks.









## Add fight statistics

## Stretch Challenges
### Build Interactive Menu
### Different battle implementation
