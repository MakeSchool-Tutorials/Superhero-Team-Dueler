---
title: Team Attack and Defense
slug: attack-defend
---
## Add Armors
We've got most everything together but we don't have the ability for our heroes to defend against attacks. We'll need another class and a few more properties in order to get this functionality. Because this is a game we will make our hero's block randomly generated every time it's called. 

The block method should return an integer between 0 and the max_block strength.

```python
class Armor:
    def __init__(self, name, max_block):
        '''Instantiate name and defense strength.'''
        self.name = name
        self.max_block = max_block
        pass

    def block(self):
        '''
        Return a random value between 0 and the 
        initialized max_block strength.
        '''
        pass
```

### Adding to the Hero class
Add additional properties to the hero class that will allow for equipping our hero's armor and also for saving fight statistics.

```python
class Hero:
    def __init__(self, name, health=100)
        # The code you have already written goes here.
        # ...
        self.armors = list()
        self.deaths = 0
        self.kills = 0

    def add_armor(self, armor):
        ''' Add armor to armors list.'''
    
    def defend(self):
        '''
        This method should run the block 
        method on each piece of armor and 
        calculate the total defense. 
        
        If the hero's health is 0
        return 0 
        '''
        pass

    def take_damage(self, damage_amt):
        ''' 
        Refactor this method to use the new
        defend method before updating the
        hero's health. 

        Update the number of deaths if the 
        hero dies in the attack.
        '''
        pass

    def add_kill(self, num_kills):
        '''
        This method should add the number 
        of kills to self.kills
        '''
        pass

    def fight(self, opponent):
        '''
        Refactor this method to update the 
        number of kills the hero has when 
        the opponent dies.
        '''
        pass

```

We will also track some statistics with the hero, specifically the number of kills and deaths. So these values will be initialized in our constructor and updated as they change.

There are also some new methods to implement in our Hero class that will calculate our hero's defense strength and update the health of our hero if damage is taken.

Any methods that already exist in your code simply need to be refactored to add the additional functionality instead of rewriting the entire method.

## Update Team Class With These Methods

```python
class Team:
    # Keep all your current code, but add these methods
    def attack(self, other_team):
        '''
        This function should randomly select 
        a living hero from each team and have 
        them fight until one or both teams 
        have no surviving heroes.

        Hint: Use the fight method in the Hero 
        class.
        '''
        pass

    def revive_heroes(self, health=100):
        '''
        This method should reset all heroes 
        health to their
        original starting value.
        '''
        pass
    
    def stats(self):
        '''
        This method should print the ratio of 
        kills/deaths for each member of the 
        team to the screen. 

        This data must be output to the console.
        '''
        pass
```

We have a way now for our teams to attack and defend. Now we just need a way for our users to make teams.

## Helpful tests

In this section you can verify your code with the tests provided in [this](https://github.com/MakeSchool-Tutorials/Superhero-Team-Dueler/blob/master/team_test.py) file. You'll want to make sure the file exists in the same folder as your `superheroes.py` file. 

You can run just the tests contained in this file by using the command:

```
pytest -x team_test.py
```
