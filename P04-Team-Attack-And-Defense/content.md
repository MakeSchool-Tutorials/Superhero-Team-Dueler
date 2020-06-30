---
title: Team Attack and Defense
slug: attack-defend
---

## Adding to the Hero class

Now we want to add additional properties and methods that will allow us to track fight statistics.

Here are the methods we will work on in the `Hero` class:

- `__init__` : We will need to add a couple new properties to track our new statistics:
    - `deaths` : default value 0
    - `kills` : default value 0
- `add_kill` : Parameters: num_kills: Int
    - create a setter for our new `kill` property
- `add_death` : Parameters: num_deaths: Int
    - create a setter for our new `death` property
- `fight` : Refactor this method to update the our statistics when things happen.

Later we will work on the following methods in our `Team` class:

- `attack` : Parameters: other_team: Team
    - Randomly select a living hero from each team and have them fight until one or both teams have no surviving heroes.
- `revive_heroes` : Parameters: none
    - This method should reset all heroes health to their original `starting_health` value.
- `stats` : Parameters: none
    - This method should print the ratio of kills/deaths for each member of the team to the screen. This data must be output to the console.

Note that any methods that already exist in your code simply need to be refactored to add the additional functionality instead of rewriting the entire method.

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
    ''' Update self.kills by num_kills amount'''
    self.kills += num_kills
```

# Add Death statistics

You will do this one on your own. Create this method that will act as a setter for `self.deaths`.

> [action]
>
> Add the `add_death` method to the Hero class:
>
```python
def add_death(self, num_deaths):
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
        # TODO: Refactor this method to update the following:
        # 1) the number of kills the hero (self) has when the opponent dies.
        # 2) then number of kills the opponent has when the hero (self) dies
        # 3) the number of deaths of the opponent if they die    in the fight
        # 4) the number of deaths of the hero (self) if they die in the fight
        pass
```

# Update Team Class - stats

We need to do some work to get our teams to battle each other. Let's start by making our `stats` method:

> [action]
>
> Build the `stats` method for your `Team` class:
>
```Python
def stats(self):
    '''Print team statistics'''
    for hero in self.heroes:
        kd = hero.kills / hero.deaths
        print("{} Kill/Deaths:{}".format(hero.name,kd))
```

# Update Team Class - revive_heroes

This one you'll do on your own. Pay close attention to the `TODO` comment, as the pseudocode will help you in writing your real code:

> [action]
>
> Build the `revive_heroes` method for your `Team` class:
>
```python
def revive_heroes(self):
    ''' Reset all heroes health to starting_health'''
    # TODO: for each hero in self.heroes,
    # set the hero's current_health to their starting_health
    pass
```

# Update Team Class - attack

Alright, we got one more method to write! This one is a bit more challenging, so we've provided the first part of the function, but it will be up to you to fill in the rest:

> [action]
>
> Build the `attack` method for your `Team` class:
>
```python
    def attack(self, other_team):
        ''' Battle each team against each other.'''
>        
        living_heroes = list()
        living_opponents = list()
>
        for hero in self.heroes:
            living_heroes.append(hero)
>
        for hero in other_team.heroes:
            living_opponents.append(hero)
>
        while len(living_heroes) > 0 and len(living_opponents)> 0:
            # TODO: Complete the following steps:
            # 1) Randomly select a living hero from each team (hint: look up what random.choice does)
            # 2) have the heroes fight each other (Hint: Use the fight method in the Hero class.)
            # 3) update the list of living_heroes and living_opponents
            # to reflect the result of the fight
>
```

We have a way now for our teams to attack and track statistics! Now we just need a way for our users to make teams.

## Helpful tests

In this section you can verify your code with the tests provided in [this](https://github.com/MakeSchool-Tutorials/Superhero-Team-Dueler/blob/master/team_test.py) file. You'll want to make sure the file exists in the same folder as your `hero.py` file.

You can run just the tests contained in this file by using the command:

```
pytest -x team_test.py
```
