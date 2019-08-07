---
title: Build Ability and Hero Classes
slug: build-ability-and-hero-classes
---

## Build Ability and Hero classes

Let's use what we've learned to build a couple classes in a file named `superheroes.py`. Create that file right now.

Here is an overview of what you will build.

Each method below is labeled with a doc string that describes what it is supposed to do. Use this as a template and replace `pass` with your own code.

The basic structure of the file we'll be writing looks like this:

```python
class Hero:
    def __init__(self, name, starting_health=100):
        '''
        Initialize these values as instance variables:

        (Some of these values are passed in above,
        others will need to be set at a starting value.)

        abilities:List
        name: String
        starting_health: Integer
        current_health: Integer
         '''
         pass

    def add_ability(self, ability):
        ''' Add ability to abilities list '''
        pass

    def attack(self):
        '''
        Calculates damage from list of abilities.

        This method should call Ability.attack()
        on every ability in self.abilities and
        return the total.
        '''
        pass

    def take_damage(self, damage):
        '''
        This method should update self.current_health
        with the damage that is passed in.
        '''
        pass

    def is_alive(self):  
        '''
        This function will
        return true if the hero is alive
        or false if they are not.
        '''
        pass

    def fight(self, opponent):  
        '''
        Runs a loop to attack the opponent until someone dies.
        '''
        pass

class Ability:
    def __init__(self, name, max_damage):
        '''
        Initialize the values passed into this
        method as instance variables.
         '''
        pass

    def attack(self):
        '''
        Return a random attack value
        between 0 and max_damage.
        '''
        pass


if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    pass
```

## Every Hero Needs an Ability

Our hero will need an ability to be able to save the world. Lets start by creating the `Ability` class that our hero can use.

Let's give our `Ability` class two simple methods at first.

```python
class Ability:
    def __init__(self, name, attack_strength):
        ''' Initialize starting values '''
        pass

    def attack(self):
        '''
         Return attack value
         between 0 and the full attack.
         '''
        pass
```

Use a constructor to set the name and attack strength for our `Ability` just like you did in the last section with `name` in our `Dog` class.

```python
def __init__(self, name, attack_strength):
    # Set Ability name
    # Set attack strength
    pass
```

Our next task is to write the `attack` method. To make it more interesting we don't want our Hero to have the same attack value every time. We want to have some range of values that are possible when our Hero attacks. We'll use the random module for this functionality

Import `random` at the very top of your file using the following command.

```python
import random
```

The `random` module has a method called `randint()` that takes two values, a minimum and maximum value. It will return some random value between the two.

You can then call:

```random.randint(2, 7)```

This will return back to you some value between and including 2 and 7.

Use this knowledge to return a random value between 0 and the strongest attack an ability can produce.

```python
def attack(self):
    """
    Use random.randint(a, b) to select a random attack value.
    Return an attack value between 0 and the full attack.
    Hint: The constructor initializes the maximum attack value.
    """
    pass
```

Complete this function using the techniques you've learned so far.

## Test your code out
You don't want to write a bunch of code without testing to see if it runs. Write code that will run the methods you created after the line

```python
if __name__ == "__main__":
```

When you finish the `Ability` class, you can test your work by calling your new methods at the end of the file like this.

```python
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

Once your code works, push your code to GitHub.

## Build out the Hero Class
Here we define what we want our `Hero` class to look like. Each hero should have a name and should be able to have several different abilities. Also a hero will need other attributes such as starting and current health. Let's set these as some starting value when we create each Hero in memory.

We'll start with the constructor for `Hero`.

The constructor should look like this:

```python
def __init__(self, name, starting_health=100):
    self.name = name
    self.starting_health = starting_health
    self.current_health = starting_health
    self.abilities = list()
```

In addition to creating our initial values, we create a new empty list that will store all of the abilities that our heroes need.

Lets test out our new constructor.

Add a call to your new constructor at the bottom of the file to test what you just did.

Hint: The bottom of your file should look like this:

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

## Create an add_ability method

```python
def add_ability(self, ability):
    # Append ability to self.abilities
```

We have abilities and Heroes, but our Heroes can't yet use abilities. Lets give our heroes abilities they can use.

Use the append method to add a new ability to your hero's `abilities` list.

*Hint*: We used the append method to add strings to a list in the Rainbow Checklist tutorial. This time we're not adding strings, instead we'll add ability objects.

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

This output may look confusing at first, but lets break it down.

Python uses brackets `[]` to denote a list. Our output is showing us that hero.abilities is a list with a single item. This item is an object with the class name Ability.

Try adding a second ability and see how it looks when you print it to the terminal.

## Create the attack method

Our hero has abilites, but can't yet use them. Build an `attack` method that will use your hero's abilities.

```python
    def attack(self):
        '''
        Calculates damage from list of abilities.

        This method should call Ability.attack()
        on every ability in self.abilities and return the total of all attacks.
        '''
        pass
```

This method should iterate over our `abilities` list and call the `attack()` method on every ability. Remember that our abilites return a random value so we have to total all those values up to get the total attack strength of all abilities. This is the total amount of damage done by the attack.

It's easiest to use a Python `for` loop to iterate over the list of abilities. You've already seen a `for` loop return string values from a list of strings here you will be returning ability objects from the abilities list.

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

Use this pattern to find the attack of each ability, but total them all up to find the strength of your hero's attack.

Test out your code using these method calls at the bottom of your file.

```
if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    ability = Ability("Great Debugging", 50)
    another_ability = Ability("Smarty Pants", 90)
    hero = Hero("Grace Hopper", 200)
    hero.add_ability(ability)
    hero.add_ability(another_ability)
    print(hero.attack())
```

You should see a value between 0 and 140 in the terminal.

## Take Damage

When a hero takes damage, their `self.current_health` should be decreased. While you can change a property directly, it's common practice to use a method to change this value instead. This is called a "setter" in software design. The job of a setter is to be in charge of updating the value of a specific property.  This allows for value verification and additional housekeeping that may be required everytime the value is changed. This system offers the advantage of allowing your software to react to the changes of specific properties. For example, a hero might take less damage if they have a force field, or they might say "Ouch!" if they get hit harder, or they might fall over over if they run out of health.

>[info]
> Methods that handle changes in properties are called setters. Methods that return the value of a property are called getters.

Your job is to subtract the damage passed to `take_damage()` from the hero's `self.current_health`.

```python
def take_damage(self, damage):
    '''
    This method should update self.current_health
    with the damage that is passed in.
    '''
    pass
```

Test your method by calling it using these values:

```python
if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.

    hero = Hero("Grace Hopper", 200)
    hero.take_damage(50)
    print(hero.current_health)
```

When calling your code with these values you should see `150` output to the terminal.

## Are You still conscious?

Once a hero has been hit they might be knocked out! Or they might still be up, how will we know?

You'll use a function to decide.

Finish the `take_damage` method. This methods should check to see if the hero is still alive and return either `True` or `False` depending if the hero is alive or dead. You can determine the hero's state by checking their `current_health`.

```python
def is_alive(self):  
    '''
    This function will
    return true if the hero is alive
    or false if they are not.
    '''
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
    hero.take_damage(150)
    print(hero.is_alive())
```

If you did it right you should see the following output in the terminal:

```
True
False
```

## Fight!

It's time to get a one vs one battle happening! Your job is to create a method that will allow each hero to attack the other.

The `fight()` method will take an `opponent` as a parameter. An `opponent` is another instance of `Hero`.

A single attack usually won't knock a hero out. The hero and opponent will usually attack each other repeatedly before one of them is knocked!

Because we don't know how many times our hero will need to attack -- it's best to use a while loop to continue the attack until someone dies.

```python
def fight(self, opponent):  
    '''
    Runs a loop to attack opponent until someone dies.
    '''
    pass
```

You'll need to use the methods that we just built to complete this.

This function will need to take into account the possibility that both heroes may not have abilities and therefore will do no damage.

Use an `if` statement and check if to see that at least one hero has an ability. If no abilities exist print out "Draw"

When a hero dies print to the console.

```
HeroName died
```
Where HeroName is the name of the hero that died.

The core functionality for this method will come from calling methods that exist in the current instantiated object (using `self`) as well as calling methods on the object that is passed in as a parameter.

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
Dumbledore died
```

This is because the values of Wonder Woman's attack are much greater than Dumbledore's. Try changing the values and see what happens.

## Move to the Next Section

Now that we have the basic functionality that allows our heros to duel each other, we can begin to move to the next important feature of object oriented programming -- inheritance.
