---
title: Add Abilities and Armor to our Heroes
slug: add-ability-and-armor-classes
---

In this chapter we are going to add the classes we built for Armor and Abilities to our Hero class so each of our heroes is unique and each battle has the potential to have a different outcome.

- Some classes we will give you the code to use. Be sure to read through it and reference the comments so that you know what it is doing. This is important because...
- Other classes we will _NOT_ give you the code, and will only give you a docstring that describes what the code is supposed to do. Use this as a template and replace `pass` with your own code.
    - Use your prior learnings and the code we gave you to help build out the code needed for these classes

Here is an overview of what you built in the previous chapter:

* Ability Class
  1. `__init__`: Parameters: name: String, max_damage: Integer
  2. `attack`: No Parameters

* Armor Class
  1. `__init__`: Parameters: name: String, max_block: Integer
  2. `block`: Parameters: None

Now, we are going to expand our Hero class so that it is able to use the armor and abilities classes to make our heroes stronger! To do so, we will adjust the hero class to have the following design:

* Hero Class
  1. `__init__`: Parameters: name:String, starting_health:Int (default value: 100)
  2. `add_ability`: Parameters: ability:Ability Object
  3. `attack`:  No Parameters
  4. `defend`: incoming_damage: Integer
  5. `take_damage`: Parameters: damage
  6. `is_alive`: No Parameters
  7. `fight`: Parameters: opponent: Hero Class  

# Build out the Hero Class
Here we define what we want our `Hero` class to look like. Each hero should have a name and should be able to have several different abilities. Also a hero will need other attributes such as starting and current health. Let's set these as some starting value when we create each Hero in memory.

Let's walk through each method and smoke test them as we go.

> [action]
> First, in your project directory, return to the file that holds your Hero class
>
>
> Build out the Hero class constructor:
>
```python
from ability import Ability
from armor import Armor
>
class Hero:
>
    # We want our hero to have a default "starting_health",
    # so we can set that in the function header.
    def __init__(self, name, starting_health=100):
      '''Instance properties:
          abilities: List
          armors: List
          name: String
          starting_health: Integer
          current_health: Integer
      '''
>
        # abilities and armors don't have starting values,
        # and are set to empty lists on initialization
        self.abilities = list()
        self.armors = list()
        # we know the name of our hero, so we assign it here
        self.name = name
        # similarly, our starting health is passed in, just like name
        self.starting_health = starting_health
        # when a hero is created, their current health is
        # always the same as their starting health (no damage taken yet!)
        self.current_health = starting_health
```

Ok, we can initialize a hero! Now let's test it:

> [action]
>
> After completing the method, add a call to your newly created constructor at the bottom of the file. This will let you test what you just did.
>
> **Hint:** The bottom of your file should look like this:
>
```python
if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    my_hero = Hero("Grace Hopper", 200)
    print(my_hero.name)
    print(my_hero.current_health)
```

If you've done it correctly you should be able to set the values and see them in the terminal when running the file:

```
Grace Hopper
200
```

Note that we can still provide a value for `starting_health` which replaces the default value of 100 that we gave in the `__init__` method! If when we instantiated our hero we had just put `Hero("Grace Hopper")`, then their `current_health` would've been 100!

# Create an add_ability method

We have abilities and Heroes, but our Heroes can't yet use abilities. Let's give our heroes abilities they can use.

> [action]
>
> Use the append method to add a new ability to your hero's `abilities` list.

>
```python
def add_ability(self, ability):
    ''' Add ability to abilities list '''
>
    # We use the append method to add ability objects to our list.
    self.abilities.append(ability)
```

When your `add_ability` method is complete test it out this way:

```python
if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    ability = Ability("Great Debugging", 50)
    hero = Hero("Grace Hopper", 200)
    hero.add_ability(ability)
    print(hero.abilities)
```

You should see output similar to the following:

```
[<__main__.Ability object at 0x7f8debceeb00>]
```

This output may look confusing at first, but let's break it down.

Python uses brackets `[]` to denote a list. Our output is showing us that `hero.abilities` is a list with a single item. This item is an object with the class name Ability.

> [action]
>
> Try adding a second ability and see how it looks when you print it to the terminal.

# Create the attack method

Our hero has abilities, but can't yet use them.

Build an `attack` method in the Hero class that will use your hero's abilities.

This method should iterate over our `abilities` list and call the `attack()` method on every ability. Remember that our abilities return a random value so we have to total all those values up to get the total attack strength of all abilities. This is the total amount of damage done by the attack.

It's easiest to use a Python `for` loop to iterate over the list of abilities.

The `for` loop will return each object in the list, and you can call methods on those objects just like you would expect.  

The code snippet below shows how you might iterate over a list of dogs and call the method `bark()` on each of them.

```python
class Dog:
    def bark(self):
        print("Woof!")

my_dogs = list()

my_dogs.append(Dog())
my_dogs.append(Dog())

for dog in my_dogs:
    dog.bark()
```

You'll see the output in this code snippet is:

```
Woof!
Woof!
```

> [action]
>
> Use this pattern to find the attack of each ability, but total them all up to find the strength of your hero's attack.
>
```python
    def attack(self):
      '''Calculate the total damage from all ability attacks.
          return: total_damage:Int
      '''
>
      # start our total out at 0
      total_damage = 0
        # loop through all of our hero's abilities
        for ability in self.abilities:
            # add the damage of each attack to our running total
            total_damage += ability.attack()
        # return the total damage
        return total_damage
```

When you're ready, let's test it!

> [action]
>
> Test out your code using these method calls at the bottom of your file.
>
```Python
if __name__ == "__main__":
    # If you run this file from the terminal
    # this block of code is executed.
    ability = Ability("Great Debugging", 50)
    another_ability = Ability("Smarty Pants", 90)
    hero = Hero("Grace Hopper", 200)
    hero.add_ability(ability)
    hero.add_ability(another_ability)
    print(hero.attack())
```

You should see a value between 0 and 140 in the terminal.

# Add Armor

let's create a method that allows us to add armor.

This method should receive an armor object that should be added to the list `self.armors` that was instantiated in the constructor.

This time, you'll need to write the code!

> [action]
>
> Create the `add_armor` method in the Hero class:
>
> **HINT:** Use `add_ability` as a model for building this method
>
```python
def add_armor(self, armor):
  '''Add armor to self.armors
    Armor: Armor Object
  '''
  # TODO: Add armor object that is passed in to `self.armors`
```

# Defend Yourself

Our hero needs to be able to block. This function will use our armors to defend against any attacks.

Make sure to take into account that there may not be any armor objects in the list. Or that if a hero is dead (has no health) they should have 0 defense.

> [action]
>
> Build the `defend` method in the Hero class.
>
> **HINT:** How is it similar/different to the `attack` method?
>
```python
def defend(self):
  '''Calculate the total block amount from all armor blocks.
     return: total_block:Int
  '''
  # TODO: This method should run the block method on each armor in self.armors
```

# Take Damage

When a hero takes damage, their `self.current_health` should be decreased. While you can change a property directly, it's common practice to use a method to change this value instead. This is called a **setter** in software design. The job of a setter is to be in charge of updating the value of a specific property.  This allows for value verification and additional housekeeping that may be required every time the value is changed. This system offers the advantage of allowing your software to react to the changes of specific properties. For example, a hero might take less damage if they have a force field, or they might say "Ouch!" if they get hit harder, or they might fall over over if they run out of health.

In our case we want to call the defend method and change our hero's health based on the number and type of armors that our hero has.

>[info]
>
> Methods that handle changes in properties are called **setters**. Methods that return the value of a property are called **getters.**

Before we update `self.current_health` we need to call `self.defend` with the amount of damage that is being passed in. We can then subtract the defense from the amount coming in and subtract that number from the hero's health.

Let's walk through an example to make it clear:

  - `take_damage` receives 50 damage units coming in.
  - Calling `self.defend(50)` returns 10.
  - 40 points should be subtracted from `self.current_health`.

> [action]
>
> Build the `take_damage` method for the Hero class:
>
> **HINT:** Reference the bullets above: calculate the `defense` amount, subtract it from the `damage` amount, and then subtract that result from `self.current_health`
>
```python
def take_damage(self, damage):
  '''Updates self.current_health to reflect the damage minus the defense.
  '''
  # TODO: Create a method that updates self.current_health to the current
  # minus the the amount returned from calling self.defend(damage).
```

Now time to test again!

> [action]
>
> Test your method by calling it using these values:
>
```python
if __name__ == "__main__":
    # If you run this file from the terminal
    # this block of code is executed.
>
    hero = Hero("Grace Hopper", 200)
    shield = Armor("Shield", 50)
    hero.add_armor(shield)
    hero.take_damage(50)
    print(hero.current_health)
```

When calling your code with these values you should have a `current_health` between 150 and 200 depending on how much was blocked by Grace.

# Are You still conscious?

Once a hero has been hit they might be knocked out! Or they might still be up, how will we know?

You'll use a function to decide.

Finish the `is_alive` method. This methods should check to see if the hero is still alive and return either `True` or `False` depending if the hero is alive or dead. You can determine the hero's state by checking their `current_health`.

> [action]
>
> Write the `is_alive` method for the Hero Class on your own:
>
> **HINT:** Follow the `TODO` instructions for guidance.
>
```python
def is_alive(self):  
  '''Return True or False depending on whether the hero is alive or not.
  '''
  # TODO: Check the current_health of the hero.
  # if it is <= 0, then return False. Otherwise, they still have health
  # and are therefore alive, so return True
  pass
```

Once your method is completed test it by calling it with these values:

```python
if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.

    hero = Hero("Grace Hopper", 200)
    hero.take_damage(150)
    print(hero.is_alive())
    hero.take_damage(15000)
    print(hero.is_alive())
```

If you did it right you should see the following output in the terminal:

```
True
False
```

# Fight!

It's time to get a one vs one battle happening! Your job is to create a method that will allow each hero to attack the other.

The `fight()` method will take an `opponent` as a parameter. An `opponent` is another instance of `Hero`.

A single attack usually won't knock a hero out. The hero and opponent will usually attack each other repeatedly before one of them is knocked!

Keep the following in mind when building this method:

- Because we don't know how many times our hero will need to attack -- it's best to use a `while` loop to continue the attack until someone dies.
- You'll need to use the methods that we just built to complete this.
- _This function will need to take into account the possibility that both heroes may not have abilities and therefore will do no damage._
    - Use an `if` statement and check to see that at least one hero has an ability. If no abilities exist print out "Draw"
- When a hero wins, print the following, replacing "HeroName" with the actual name of the hero who won the fight:

```
HeroName won!
```

The core functionality for this method will come from calling methods that exist in the current instantiated object (using `self`) as well as calling methods on the `opponent` object that is passed in as a parameter.

> [action]
>
> Build the `fight` method for the Hero class! Remove the current implemenation and take everything you've learned so far in this chapter and apply it to re-writing this method!
>
```python
def fight(self, opponent):  
  ''' Current Hero will take turns fighting the opponent hero passed in.
  '''
  # TODO: Fight each hero until a victor emerges.
  # Phases to implement:
  # 0) check if at least one hero has abilities. If no hero has abilities, print "Draw"
  # 1) else, start the fighting loop until a hero has won
  # 2) the hero (self) and their opponent must attack each other and each must take damage from the other's attack
  # 3) After each attack, check if either the hero (self) or the opponent is alive
  # 4) if one of them has died, print "HeroName won!" replacing HeroName with the name of the hero, and end the fight loop
  pass
```

## Continue To Test it out

You can test out whether your `Hero` class is working properly by adding these tests to your file:

```python
if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.

    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)
```

You should see an output similar to:

```
Wonder Woman won!
```

This is because the values of Wonder Woman's attack are much greater than Dumbledore's. Try changing the values and see what happens.

# Move to the Next Section

Now that we have the basic functionality that allows our heroes to duel each other, we can begin to move to the next important feature of object oriented programming -- **inheritance**.
