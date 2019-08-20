---
title: Team Attack and Defense
slug: attack-defend
---

## Adding to the Hero class

Now we want to add additional properties and methods that will allow us to track fight statistics.

Here are the methods we will work on in the `Hero` class.

* `__init__` : We will need to add a couple new properties - `deaths`, and `kills` to track our statistics.
* `add_kill` : create a setter for new properties
* `fight` : Refactor this method to update the our statistics when things happen.

We will also track some statistics with the hero, specifically the number of kills and deaths. So these values will be initialized in our constructor and updated as they change.

There are also some new methods to implement in our Hero class that will calculate our hero's defense strength and update the health of our hero if damage is taken.

Any methods that already exist in your code simply need to be refactored to add the additional functionality instead of rewriting the entire method.

# Add properties to Hero method

let's start by adding a way to track statistics. Create these new properties in the constructor to allow us to do this.

> [action]
>
> Update the constructor for your Hero class to track deaths and kills:
>
```python
def __init__(self, name, health=100):
    # The code you have already written goes here.
    # ...
    self.deaths = 0
    self.kills = 0
```

# Add Kill statistics

Create this method that will act as a setter for `self.kills`.

> [action]
>
> Add the `add_kill` method to the Hero class:
>
```python
def add_kill(self, num_kills):
    ''' Update kills with num_kills'''
    # TODO: This method should add the number of kills to self.kills
    pass
```

# Add Death statistics

Create this method that will act as a setter for `self.deaths`.

> [action]
>
> Add the `add_deaths` method to the Hero class:
>
```python
def add_deaths(self, num_deaths):
    ''' Update deaths with num_deaths'''
    # TODO: This method should add the number of deaths to self.deaths
    pass
```

# Update Fight method

We want our fight method to update our statistics when things happen. Let's update `fight` to reflect what's happening during the battle.

> [action]
>
> Update the `fight` method in the Hero class to the following:
>
```python
    def fight(self, opponent):
        #... The code you already wrote should be here ...
>
        #TODO: Refactor this method to update the
        # number of kills the hero has when the opponent dies.
        # Also update the number of deaths for whoever dies in the fight
        pass
```

# Update Team Class With These Methods

We need to do some work to get our teams to battle each other.

> [action]
>
> Update your team class to fulfill the following `TODOs`:
>
```python
class Team:
    # Keep all your current code, but add these methods
    def attack(self, other_team):
        ''' Battle each team against each other.'''
        # TODO: Randomly select a living hero from each team and have
        # them fight until one or both teams have no surviving heroes.
        # Hint: Use the fight method in the Hero class.
        pass
>
    def revive_heroes(self, health=100):
        ''' Reset all heroes health to starting_health'''
        # TODO: This method should reset all heroes health to their
        # original starting value.
        pass
>
    def stats(self):
        '''Print team statistics'''
        # TODO: This method should print the ratio of kills/deaths for each
        # member of the team to the screen.
        # This data must be output to the console.
        # Hint: Use the information stored in each hero.
        pass
```

We have a way now for our teams to attack and defend. Now we just need a way for our users to make teams.

## Helpful tests

In this section you can verify your code with the tests provided in [this](https://github.com/MakeSchool-Tutorials/Superhero-Team-Dueler/blob/master/team_test.py) file. You'll want to make sure the file exists in the same folder as your `superheroes.py` file.

You can run just the tests contained in this file by using the command:

```
pytest -x team_test.py
```
