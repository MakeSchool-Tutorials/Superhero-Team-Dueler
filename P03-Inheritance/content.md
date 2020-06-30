---
title: Inheritance
slug: inheritance
---

One of the great features of object oriented programming is the idea of **inheritance**. Inheritance comes in handy because it allows for additional ways to reuse code.

Here is a simple demonstration of inheritance at work.

```python
class Animal:
    def __init__(self, name, sleep_duration):
        self.name = name
        self.sleep_time = sleep_time

    def sleep(self):
        print(
            "{} sleeps for {} hours {}".format(
                self.name,
                self.sleep_time))
```

let's say we have the above `Animal` class. We can instantiate a new animal object the same way we've already seen it done.

```python
dog = Animal("Sophie", 12)
dog.sleep()
```

Here we have our dog Sophie that needs 12 hours of sleep every night. If we call our sleep method we'll see this:

```
Sophie sleeps for 12 hours
```

Our dog here is simply an instance of our `Animal` class, but what if we want specific dog functionality that only dogs have.

We don't want to put a bark method in `Animal` because not every animal barks. We also don't want to have to duplicate every method that dogs and animals have in common.

let's use inheritance to make a `Dog` class that allows us to bark.

```python
class Animal:
    def __init__(self, name, sleep_duration):
        self.name = name
        self.sleep_duration = sleep_duration

    def sleep(self):
        print(
            "{} sleeps for {} hours".format(
                self.name,
                self.sleep_duration))

# Note that the class Dog takes in Animal as a parameter!
class Dog(Animal):
    def bark(self):
        print("Woof! Woof!")
```

Instantiate a new `Dog` object and call the sleep and bark methods this way.

```
my_dog = Dog("Sophie", 12)
my_dog.sleep()
my_dog.bark()
```

You should see this output in the terminal.

```
Sophie sleeps for 12 hours
Woof! Woof!
```

**You can see that we didn't have to create another sleep method again in order to use it.** Our `Dog` class **inherited** this method from our **superclass** `Animal`.

In this example `Dog` is our **subclass** and it will inherit everything from its superclass. This allows us to write specific functionality for `Dog` while keeping all the original functionality that was already given to us in `Animal`. This is also why we did _not_ need to write an `__init__` method for `Dog`: it just uses the same one as `Animal`!

> [info]
>
> Note the comment in the previous code snippet. Our `Dog` class takes in `Animal` as its parameter, which signals that `Dog` is a subclass of `Animal`, as all `Dogs` are created from `Animals`, and not just plain `objects`

Let's try this out ourselves now:

>[action]
>Create the file `animal.py` file
>
```bash
$ touch animal.py
```
>
> Create a `class` named `Animal` which has the methods `eat` and `drink` as well as the property `name`.
>
> The eat method should print the animal's name and "is eating"
>
> The drink method should print the animal's name and "is drinking"
>
> Once you do that, in the same file, create the `Frog` class, which is a subclass of `Animal`, and has the method `jump`, which prints the frog's name and "is jumping"
>
> Finally, test your code by instantiating one `Animal` and one `Frog`, and making sure that your `Frog` object can eat, drink, and jump, and that your `Animal` can eat and drink.

Once you've tried it, check your code against the provided solution below:

>[solution]
>
```py
#animal.py
class Animal:
  def __init__(self, name):
    self.name = name
>
  def eat(self):
    print('{} is eating'.format(self.name))
>
  def drink(self):
    print('{} is drinking'.format(self.name))
>
class Frog(Animal):
    def jump(self):
        print('{} is jumping'.format(self.name))
```

Let's use what we learned here to give our superheroes more options for attacking.

# Weapon Class
**In your project directory, make a file named 'weapon.py' to contain the Weapon class**

> [action]
>
> Re-open your `superheroes.py` file, we'll be using this for the remainder of this tutorial.

One of the powerful features of Object Oriented Programming has a large scary name but refers to a pretty simple concept: **Polymorphism**.

Polymorphism basically allows us to use different implementations of the same method.

For example, we've already built an `Ability` class that will give our superheroes a way to fight, but many superheroes have more than just abilities. Let's give our superheroes weapons they can use by adding another class to our `superheroes.py` file.

We can reuse the functionality in `Ability` so that we can prevent code duplication. let's say that weapons aren't as effective as superhero abilities so we should rewrite our attack function to allow for greater variability in attack strength. let's make our weapons attack power range between half of the `max_damage` value, to the full `max_damage` value of the weapon.

For example, if the Weapon has a `max_damage` value of 80, then the Weapon's attack method should return a value between 40 and 80.

**NOTE:** Make sure to use integer division ( Using the `//` operator) to be certain that you return an integer. This way if the `max_damage` value was 57, it will return 28 instead of 28.5

> [action]
>
> Write the `attack` method for our new `Weapon` class. Use what you learned for the `attack` method in the `Ability` class if you get stuck.
>
```python
class Weapon(Ability):
    def attack(self):
        """  This method returns a random value
        between one half to the full attack power of the weapon.
        """
        # TODO: Use integer division to find half of the max_damage value
        # then return a random integer between half of max_damage and max_damage
        pass
```

Now that we have a weapon, we need to allow heroes to add a weapon for them to use. You will do this one on your own as well, refer to your other `add` methods for guidance.

**Make sure to import the Weapon class into your Hero class**

> [action]
>
> Add the following to the Hero class:
>
```python
from weapon import Weapon

class Hero:
    # The code you have already written should be here.  
    # Add the following method to your hero class...
>
    def add_weapon(self, weapon):
        '''Add weapon to self.abilities'''
        # TODO: This method will append the weapon object passed in as an
        # argument to self.abilities.
        # This means that self.abilities will be a list of
        # abilities and weapons.
        pass
    ....
```

Use these tests to make sure you implemented `Weapon` correctly:

> [action]
>
> Test out your code using these method calls at the bottom of your file.
>
```python
if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    hero = Hero("Wonder Woman")
    weapon = Weapon("Lasso of Truth", 90)
    hero.add_weapon(weapon)
    print(hero.attack())
```

Your output should be a number between 45 and 90.

Congrats, you've re-defined a method that already exists in our inherited `Ability` class!

This is called **method overriding** and it is a form of **Polymorphism. It allows you to specify a different functionality for methods that are inherited from the superclass.** When we call `attack()` on our `Weapon` object it will run the `attack` method specified in the `Weapon` class and not the one in `Ability`.

# Build A Team class

**In your project directory, make a 'team.py' file to contain the Team class**

Superheroes should be team players, so let's create a team class that can manage all of our superheroes.

Here's an overview of some of the methods we'll need.

1. `__init__`: Parameters: name: String
1. `add_hero`: Parameters: hero:String
1. `remove_hero`: Parameters name: String
1. `view_all_heroes`: Parameters: None

You'll need to use methods that exist in the built-in Python list (`self.heroes`) to add and remove heroes to the team. This code is going to be very similar to the code that you wrote in Rainbow Checklist except that instead of adding strings to our list, we want to add `Hero` objects.

## Aggregation Vs Inheritance

Before we move forward, let's review what we just said about the `Team` class: it will contain a list of `Hero` objects. An important distinction here is that **`Team` does not inherit from the `Hero` class, and `Hero` does not inherit from the `Team` class.**

Rather, the `Team` class **contains** `Hero` objects (using a list), see below for a visualized example:

![hero_team](assets/hero_visual.png)

In a similar manner, your `Hero` has a list of abilities and armors. This does not mean your `Hero` has `Ability` or `Armor` methods or properties, but that the `Hero` can contain `Ability` or `Armor` objects that have their own methods/properties, and can only be used/accessed by the `Ability` or `Armor` objects

> [info]
>
> This concept is known as **Aggregation** in OOP. Another way to think about it is that inheritance vs aggregation is "isa" vs. "hasa".
>
>For example, a `Weapon` "is a(n)" `Ability`, whereas a `Team` "has a" list of `Hero` objects

# Build the Constructor

> [action]
>
> Build the constructor for the Team class:
>
```py
class Team:
    def __init__(self, name):
        ''' Initialize your team with its team name and an empty list of heroes
        '''
        self.name = name
        self.heroes = list()
````

# Remove a Hero from the Team

This method should find a Hero by its name and remove them from the team's list of Heroes. If you cannot find a hero, return 0

> [action]
>
> Build the `remove_hero` method for the Team class:
>
```python
def remove_hero(self, name):
    '''Remove hero from heroes list.
    If Hero isn't found return 0.
    '''
    foundHero = False
    # loop through each hero in our list
    for hero in self.heroes:
        # if we find them, remove them from the list
        if hero.name == name:
            self.heroes.remove(hero)
            # set our indicator to True
            foundHero = True
    # if we looped through our list and did not find our hero,
    # the indicator would have never changed, so return 0
    if not foundHero:
        return 0
```

# View the teams heroes

You'll build this one on your own. This method should print a list of all the teams heroes to the terminal.

> [action]
>
> Build the `view_all_heroes` function for the Team class:
>
```python
def view_all_heroes(self):
        '''Prints out all heroes to the console.'''
        # TODO: Loop over the list of heroes and print their names to the terminal one by one.
        pass
```

# Add Hero to Team

You will build this one on your own as well. We need to add heroes to our team. Let's create a method to do that. This will be similar to the methods we already wrote when adding armors to our hero.

> [action]
>
> Build the `add_hero` method for the the Team Class:
>
```python
def add_hero(self, hero)
  '''Add Hero object to self.heroes.'''
  # TODO: Add the Hero object that is passed in to the list of heroes in
  # self.heroes
  pass
```

# Test Driven Development

Previously we've used user stories to visualize what our finished application should look like before we began to build it. Here instead of user stories we'll use automated tests in much the same way.

Test Driven Development (commonly abbreviated as **TDD**) is another way of imagining the end result before you dive into coding. However, instead of writing narratives, with TDD we actually write *code* that verifies the behavior we want our program to perform before we even write the program.

By writing the test first you focus on functionality first instead of implementation. In the spirit of TDD, we wrote some tests already for you to use, which your class methods must pass.

## Install `pytest`

We'll use the automated testing tool [pytest](https://docs.pytest.org/en/latest/) to verify the code.

Pytest must be installed into your system first before you can use it. While you don't need pytest to run the tests included in this project, pytest gives a lot of additional helpful tools and loggin.

> [action]
>
> To install, simply open your terminal and type:
>
```bash
$ pip3 install pytest
```

You should be able to verify that pytest is installed by checking which version you have.

```bash
pytest --version
```

You should see something similar to this output.

```bash
This is pytest version 5.1.0, imported from /usr/local/lib/python3.7/site-packages/pytest.py
```

# Pass Your First Test
Tests have been provided to help you with this assignment.

You can download the test [here](https://github.com/MakeSchool-Tutorials/Superhero-Team-Dueler/blob/master/hero_test.py) and place it in the same folder as `superheroes.py`

To run the provided tests `cd` into to the project directory in the terminal

```
cd name-of-project-dir
```

 then run

```
pytest
```

This command will automatically look at any file that contains `test` in the filename then run any function that begins with `test_`.

Fortunately `pytest` has options that allow us to specify which tests to run and how many tests to focus on.

If you want pytest to stop after the first failure you can use this command instead.

```
pytest -x
```

This will run all tests in `hero_test.py` and stop after the first failure.

For additional `pytest` options see their documentation [here](https://docs.pytest.org/en/latest/usage.html).

> [action]
>
> Make sure all the tests in the `hero_test.py` file pass.

## A Note About Python 2 vs Python 3
One of the exciting features about python3 is that it supports unicode! This is great but it can cause compatibility issues when running python2.

If you receive an error saying that there's a unicode error you'll need to force pytest to use python3 this way.

`python3 -m pytest`
