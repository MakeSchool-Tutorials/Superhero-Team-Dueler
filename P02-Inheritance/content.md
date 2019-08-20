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

Here's the solution:

>[solution]
>
```py
class Animal:
  def __init__(self, name):
    self.name = name
>
  def eat(self):
    print('{} is eating'.format(self.name))
>
  def drink(self):
    print('{} is drinking'.format(self.name))
```

Let's use what we learned here to give our superheroes more options for attack.

# Weapon Class

One of the powerful features of Object Oriented Programming has a large scary name but refers to a pretty simple concept: **Polymorphism**.

Polymorphism basically allows us to use different implementations of the same method.

For example, we've already built an `Ability` class that will give our superheroes a way to fight, but many superheroes have more than just abilities. Let's give our superheroes weapons they can use by adding another class to our `superheroes.py` file.

We can reuse the functionality in `Ability` so that we can prevent code duplication. Lets say that weapons aren't as effective as superhero abilities so we should rewrite our attack function to allow for greater variability in attack strength. Lets make our weapons attack power range between 0 ( a miss ) to the full attack value of the weapon.

If for example the maximum attack value is 80 then this attack method should return a value between 40 and 80.

Make sure to use integer division ( Using the `//` operator) to be certain that you return an integer.

> [action]
>
> Here are the methods that you'll need to write for our new `Weapon` class.
>
```python
class Weapon(Ability):
    def attack(self):
        """  This method returns a random value
        between one half to the full attack power of the weapon.
        """
        # TODO: Use what you learned to complete this method.
        pass
```

Here we've re-defined a method that already exists in our inherited `Ability` class.

This is called **method overriding** and it is a form of **Polymorphism**. It basically allows you to specify a different functionality for methods that are inherited from the superclass. When we call `attack()` on our `Weapon` object it will run the `attack` method specified in the `Weapon` class and not the one in `Ability`.

# Build Team class

Superheroes should be team players, so let's create a team class that can manage all of our superheroes.

Here's an overview of some of the methods we'll need.


• Team Class
    1. __init__: Parameters: name: String
    2. add_hero: Parameters: hero:String
    3. remove_hero: Parameters name: String
    4. view_all_heroes: Parameters: None

You'll need to use methods that exist in the built-in Python list (`self.heroes`) to add and remove heroes to the team. This code is going to be very similar to the code that you wrote in Rainbow Checklist except that instead of adding strings to our list, we want to add `Hero` objects.

## Build the Constructor

> [action]
>
> Build the constructor for the Team class:
>
```py
def __init__(self, name):
    ''' Initialize your team with its team name
    '''
    # TODO: Implement this constructor by assigning the name and heroes, which should be an empty list
    pass
````

# Remove a Hero from the Team
This method should find a Hero by its name and remove them from the team's list of Heroes.

> [action]
>
> Build the `remove_hero` method for the Team class:
>
```python
    def remove_hero(self, name):
        '''Remove hero from heroes list.
        If Hero isn't found return 0.
        '''
        # TODO: Implement this method to remove the hero from the list given their name.
        pass
```

# View the teams heroes

This method should print a list of all the teams heroes to the terminal.

> [action]
>
> Build the `view_all_heroes` function for the Team class:
>
```python
def view_all_heroes(self):
        '''Prints out all heroes to the console.'''
        # TODO: Loop over the list of heroes and print their names to the terminal.
        pass
```

# Add Hero to Team

We need to add heroes to our team. Let's create a method to do that. This will be similar to the methods we already wrote when adding armors to our hero.

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

By writing the test first you focus on functionality first instead of implementation. In the spirit of TDD you'll be provided with tests that your class methods must pass.

## Install `pytest`

We'll use the automated testing tool **pytest** to verify the code.

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

This will run all tests in `hero_test.py` and stop after the first failure.

For additional `pytest` options see their documentation [here](https://docs.pytest.org/en/latest/usage.html).

> [action]
>
> Make sure all the tests in the `hero_test.py` file pass.

## A Note About Python 2 vs Python 3
One of the exciting features about python3 is that it supports unicode! This is great but it can cause compatibility issues when running python2.

If you receive an error saying that there's a unicode error you'll need to force pytest to use python3 this way.

`python3 -m pytest`
