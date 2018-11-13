---
title: Inheritance
slug: inheritance
---

## Inheritance
One of the great features of object oriented programming is the idea of **inheritance**. Inheritance comes in useful because it allows for additional ways to reuse code.

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

Lets say we have the above `Animal` class. We can instantiate a new animal object the same way we've already seen it done.

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

Lets use inheritance to make a `Dog` class that allows us to bark.

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

You can see that we didn't have to create another sleep method again in order to use it. We have **inherited** this method from our **superclass** `Animal`.

In this example `Dog` is our **subclass** and it will inherit everything from its superclass. This allows us to write specific functionality for `Dog` while keeping all the original functionality that was already given to us in `Animal`.

Lets use what we learned here to give our superheroes more options for attack.

## Weapon Class
We've already built an `Ability` class that will give our superheroes a way to fight, but many superheroes have more than just abilities. Let's give our superheroes weapons they can use by adding another class to our `superheroes.py` file.

We can reuse the functionality in `Ability` so that we can prevent code duplication. Lets say that weapons aren't as effective as superhero abilities so we should rewrite our attack function to allow for greater variability in attack strength. Lets make our weapons attack power range between 0 ( a miss ) to the full attack value of the weapon.

Here are the methods that you'll need to write for our new `Weapon` class.

```python
class Weapon(Ability):
    def attack(self):
        """
        This method should should return a random value
        between one half to the full attack power of the weapon.
        Hint: The attack power is inherited.
        """
```

Here we've re-defined a method that already exists in our inherited `Ability` class.

This is called **method overriding** and allows you to specify a different functionality for methods that are inherited from the superclass. When we call `attack()` on our `Weapon` object it will run the `attack` method specified in the `Weapon` class and not the one in `Ability`.

Everything else that was created in the `Ability` class will work the same.

Create a new implementation of attack that returns a random value between the full attack power and half of the full attack power. 

If for example the maximum attack value is 80 then this attack method should return a value between 40 and 80.

Make sure to use integer division ( Using the `//` operator) to be certain that you return an integer.

## Build Team class
Superheroes should be team players, so lets create a team class that can manage all of our superheroes.

Implement the following methods using everything we've learned so far.

```python
class Team:
    def __init__(self, team_name):
        '''Instantiate resources.'''
        self.name = team_name
        self.heroes = list()

    def add_hero(self, hero):
        '''Add Hero object to heroes list.'''
        pass

    def remove_hero(self, name):
        '''
        Remove hero from heroes list.
        If Hero isn't found return 0.
        '''
        pass

    def view_all_heroes(self):
        '''Print out all heroes to the console.'''
        pass

```

These are some of the methods you'll need to implement.

You'll need to use methods that exist in the built-in Python list (`self.heroes`) to add and remove heroes to the team. This code is going to be very similar to the code that you wrote in Rainbow Checklist except that instead of adding strings to our list, we want to add `Hero` objects.

## Test Driven Development
Previously we've used user stories to visualize what our finished application should look like before we began to build it. Here instead of user stories we'll use automated tests in much the same way.

Test Driven Development (commonly abbreviated as **TDD**) is another way of imagining the end result before you dive into coding. However, instead of writing narratives, with TDD we actually write *code* that verifies the behavior we want our program to perform before we even write the program.

By writing the test first you focus on functionality first instead of implementation. In the spirit of TDD you'll be provided with tests that your class methods must pass.

## Install `pytest`
We'll use the automated testing tool **pytest** to verify the code.

Pytest must be installed into your system first before you can use it.

To install, open your terminal and type:

```
pip install pytest
```

You should be able to verify that pytest is installed by checking which version you have.

```
pytest --version
```

You should see something similar to this output.

```
This is pytest version 3.2.1, imported from /anaconda3/lib/python3.6/site-packages/pytest.py
```

## Pass Your First Test
Tests have been provided to help you with this assignment.

You can download the test [here](https://github.com/MakeSchool-Tutorials/Superhero-Team-Dueler/blob/master/hero_test.py) and place it in the same folder as heroperoes.py

To run the provided tests `cd` into to the project directory in the terminal

```
cd Super-Hero-Battle
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

This will run all tests in hero_test.py and stop after the first failure.

For additional `pytest` options see their documentation [here](https://docs.pytest.org/en/latest/usage.html).

Make sure all the tests in the `hero_test.py` file pass.

## A Note About Python 2 vs Python 3
One of the exciting features about python3 is that it supports unicode! This is great but it can cause compatibility issues when running python2. 

If you receive an error saying that there's a unicode error you'll need to force pytest to use python3 this way.

`python3 -m pytest`
