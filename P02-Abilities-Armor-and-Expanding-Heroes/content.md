---
title: Build Ability and Armor Classes
slug: build-ability-and-armor-classes
---

> [action]
>

In this chapter we are going to make classes for Armor and Abilities so each of our heroes is unique and each battle has the potential to have a different outcome.

- Some classes we will give you the code to use. Be sure to read through it and reference the comments so that you know what it is doing. This is important because...
- Other classes we will _NOT_ give you the code, and will only give you a docstring that describes what the code is supposed to do. Use this as a template and replace `pass` with your own code.
    - Use your prior learnings and the code we gave you to help build out the code needed for these classes

Here is an overview of what you will build in this chapter:

* Ability Class
  1. `__init__`: Parameters: name: String, max_damage: Integer
  2. `attack`: No Parameters

* Armor Class
  1. `__init__`: Parameters: name: String, max_block: Integer
  2. `block`: Parameters: None

After we implemented the above classes, we are going to expand our Hero class so that it is able to use the armor and abilities classes to make our heroes stronger! To do so, we will adjust the hero class to have the following design:

* Hero Class
  1. `__init__`: Parameters: name:String, starting_health:Int (default value: 100)
  2. `add_ability`: Parameters: ability:Ability Object
  3. `attack`:  No Parameters
  4. `defend`: incoming_damage: Integer
  5. `take_damage`: Parameters: damage
  6. `is_alive`: No Parameters
  7. `fight`: Parameters: opponent: Hero Class  


# Every Hero Needs an Ability

Instead of remaking our `Hero` class first, let's start with the classes our `Hero` class will need to use.

Our hero will need an ability to be able to save the world. let's start by creating a class named `Ability` that our hero can use.

Let's give our `Ability` class two simple methods, `__init__`, and `attack`.

**First, in your project directory, make a file named 'ability.py' to contain all the code for the Ability class**

## Set initial values with a constructor

> [action]
>
> Use a constructor to set the name and attack strength for our `Ability` just like you did in the last section with `name` in our `Dog` class.
>
```python
class Ability:
    def __init__(self, name, max_damage):
        '''
       Initialize the values passed into this
       method as instance variables.
        '''
>
        # Assign the "name" and "max_damage"
        # for a specific instance of the Ability class
        self.name = name
        self.max_damage = max_damage
```

Our next task is to write the `attack` method. To make it more interesting we don't want our Hero to have the same attack value every time. We want to have some range of values that are possible when our Hero attacks. We'll use the random module for this functionality

> [action]
>
> Import `random` at the very top of your file using the following command.
>
```python
import random
```

The `random` module has a method called `randint()` that takes two values, a minimum and maximum value. It will return some random value between the two.

You can then call:

```python
random.randint(2, 7)
```

This will return back to you some value between and including 2 and 7.

> [action]
>
> Use this knowledge to return a random value between 0 and the strongest attack an ability can produce.
>
```python
class Ability:
>
# code for __init__ method
...
>
  def attack(self):
      ''' Return a value between 0 and the value set by self.max_damage.'''
>
      # Pick a random value between 0 and self.max_damage
      random_value = random.randint(0,self.max_damage)
      return random_value
```

## Test your code out

You don't want to write a bunch of code without testing to see if it runs.

> [action]
>
> When you finish the `Ability` class, you can test your work by calling your new methods at the end of the file like this:
>
```python
import random
>
class Ability:
# ability class code
...
>
if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    ability = Ability("Debugging Ability", 20)
    print(ability.name)
    print(ability.attack())
```

If your code is written correctly you should see a number between 0 and 20 appear in the terminal if you use this example to test with.

My code gives me the following:

```
Debugging Ability
4
```

But your values may be different since we're using a random number generator.

# Add Armors

**In your project directory make a file named 'armor.py' and placing the Armor class inside of it**

You can't go into battle unprepared. We need to give our heroes armor that they can use to defend themselves.

> [action]
>
> Create a new class called `Armor` that contains two methods: `__init__` and `block`.

The block method should return an integer between 0 and the max_block strength.

For this class, we will _not_ give you the code. Take your learnings from making the `Ability` class and apply them here, there are a lot of similarities. Remember to remove the `pass` line

> [action]
>
> Build the Constructor
>
```python
class Armor:
    def __init__(self, name, max_block):
        '''Instantiate instance properties.
            name: String
            max_block: Integer
        '''
        # TODO: Create instance variables for the values passed in.
        pass
```

Let's create a method that we can call that will calculate the amount we will block with.

> [action]
>
> Build the `block` method for the Armor class
>
```python
def block(self):
    '''
    Return a random value between 0 and the
    initialized max_block strength.
    '''
    pass
```

When you're done, add to the test code you wrote earlier to check your answer:

> [action]
>
> Create an instance of `Armor` and check that your properties and methods work correctly:
>
```python
if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    armor = Armor("Debugging Shield", 10)
    print(armor.name)
    print(armor.block())
```

If your code is written correctly you should see a number between 0 and 10 appear in the terminal if you use this example to test with.

My code gives me the following:

```
Debugging Shield
7
```

# Build out the Hero Class
Here we define what we want our `Hero` class to look like. Each hero should have a name and should be able to have several different abilities. Also a hero will need other attributes such as starting and current health. Let's set these as some starting value when we create each Hero in memory.

Let's walk through each method and smoke test them as we go.

> [action]
>
> Build out the Hero class constructor:
>
```python
from ability import Ability
from armor import Armor

class Hero:
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
    # We used the append method to add strings to a list
    # in the Rainbow Checklist tutorial. This time,
    # we're not adding strings, instead we'll add ability objects.
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

It's easiest to use a Python `for` loop to iterate over the list of abilities. You've already seen a `for` loop return string values from a list of strings. Here you will be returning ability objects from the abilities list.

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
```python
def add_armor(self, armor):
  '''Add armor to self.armors
    Armor: Armor Object
  '''
  # TODO: Add armor object that is passed in to `self.armors`
```

# Defend Yourself

Our hero needs to be able to block. This function will use our armors to defend against any attacks.

Make sure to take into account that there may not be any armor objects in the list.

> [action]
>
> Build the `defend` method in the Hero class. How is it similar/different to the `attack` method?:
>
```python
def defend(self, damage_amt):
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
> Methods that handle changes in properties are called setters. Methods that return the value of a property are called **getters.**

Before we update `self.current_health` we need to call `self.defend` with the amount of damage that is being passed in. We can then subtract the defense from the amount coming in and subtract that number from the hero's health.

Let's walk through an example to make it clear:

  - If `take_damage` receives 50 damage units coming in.
  - If calling `self.defend(50)` returns 10.
  - 40 points should be subtracted from `self.current_health`.

> [action]
>
> Build the `take_damage` method for the Hero class:
>
```python
def take_damage(self, damage):
  '''Updates self.current_health to reflect the damage minus the defense.
  '''
  # TODO: Create a method that updates self.current_health to the current
  # minus the the amount returned from calling self.defend(damage).
    defense = self.defend()    
    self.current_health -= damage - defense

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

    hero = Hero("Grace Hopper", 200)
    shield = Armor("Shield", 50)
    hero.add_armor(shield)
    hero.take_damage(50)
    print(hero.current_health)
```

When calling your code with these values you should a range between 150 and 200 depending on how much was blocked by Grace.

# Are You still conscious?

Once a hero has been hit they might be knocked out! Or they might still be up, how will we know?

You'll use a function to decide.

Finish the `is_alive` method. This methods should check to see if the hero is still alive and return either `True` or `False` depending if the hero is alive or dead. You can determine the hero's state by checking their `current_health`.

> [action]
>
> Write the `is_alive` method for the Hero Class on your own:
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
- Use an `if` statement and check if to see that at least one hero has an ability. If no abilities exist print out "Draw"
- When a hero wins, print the following, replacing "HeroName" with the actual name of the hero who won the fight:

```
HeroName won!
```

The core functionality for this method will come from calling methods that exist in the current instantiated object (using `self`) as well as calling methods on the `opponent` object that is passed in as a parameter.

> [action]
>
> Build the `fight` method for the Hero class! Take everything you've learned so far in this chapter and apply it to creating this method!
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

Great work on building out your first few classes! Now that we have the basic functionality that allows our heroes to duel each other, we can begin to move to the next important feature of object oriented programming -- **inheritance**.
