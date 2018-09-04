---
title: Team Attack and Defense
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
        """
        Return a random value between 0 and the 
        initialized defend strength.
        """
```
Our super heroes should have armor that they can wear to help defend themselves. Not only that, but they also need an amount of health that they can lose in a fight. Fortunately we have all the skill to do this.

Implement the defend method so that it returns a random integer between 0 and the full defend strength.

### Add health to Hero class
In the Hero class's constructor add a third parameter for health as such.

```python
class Hero:
    def __init__(self, name, health=100)
        # This should be the code you already have written.
        # ...

        self.armors = list()
        self.start_health = health
        self.health = health
        self.deaths = 0
        self.kills = 0
    
    def defend(self):
        """
        This method should run the defend method on each piece of armor and calculate the total defense. 
        
        If the hero's health is 0, the hero is out of play and should return 0 defense points.
        """

    def take_damage(self, damage_amt):
        """
        This method should subtract the damage amount from the 
        hero's health. 

        If the hero dies return 1 and update number of deaths.

        Otherwise return 0
        """
```
This third parameter we added has a default value of 100 so it's optional when instantiating our Hero class. We'll need to also be able to save the starting value as well as our current health. We'll just use `health` when referring our heroe's current health for the sake of clarity.

We will also track some statistics with the hero, specifically the number of kills and deaths. So these values will be initialized in our constructor and updated as they change.

There are also some new methods to implement in our Hero class that will calculate our hero's defense strength and update the health of our hero if damage is taken.

## Update Team Class With Attack and Defend Methods

```python
class Team:
    # Keep all your current code, but add these methods
    def attack(self, other_team):
        """
        This method should total our teams attack strength and call the defend() method on the rival team that is passed in.
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
        This method should reset all heroes health to their
        original starting value.
        """
    
    def stats(self):
        """
        This method should print the ratio of kills/deaths for each member of the team to the screen. 

        This data must be output to the terminal.
        """
```

Just as each hero needed a defend method, our Team needs to be able to coordinate our hero's attacks.

## Stretch Challenge
Make some heroes more heroic than others. They may take more of the damage for the team.

## Add fight statistics

## Stretch Challenges

### Different battle implementation
