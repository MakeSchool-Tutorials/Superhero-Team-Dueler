---
title: Build Ability and Hero Classes
slug: abilihero
---

## Build Ability and Hero classes
Let's use what we've learned to build a couple classes in a file named `superheroes.py`.

Here is an overview of what you will build.
```python
class Ability:
    def __init__(self, name, attack_strength):
        # Initialize starting values

    def attack(self):
        # Return attack value

    def update_attack(self, attack_strength):
        # Update attack value


class Hero:
    def __init__(self, name):
        # Initialize starting values

    def add_ability(self, ability):
        # Add ability to abilities list

    def attack(self):
        # Run attack() on every ability hero has


if __name__ == "__main__":
    # If you run this file from the terminal this block is executed. 
```
### Ability Class
Let's give our `Ability` class three simple methods at first.

```python

class Ability:
    def __init__(self, name, attack_strength):
        # Initialize starting values

    def attack(self):
        # Return attack value

    def update_attack(self, attack_strength):
        # Update attack value
```

Use a constructor to set the name and attack strength for our `Ability` just like you did above with `name` in our `Dog` class.


```python
def __init__(self, name, attack_strength):
    # Set Ability name
    # Set attack strength
```
Our next task is to write the `attack` method. 

Import `random` at the very top of your file using

```python
import random
```

The `random` module has a method called `randint()` that takes two values, a minimum and maximum value. It will return some random value between the two. The trick we're going to add is to make the lowest possible attack value half of the highest possible attack value. 

We only want to work with integers so use the floor division operator `//` to do the math. 

So instead of using

```python
float_value = 20 / 8
```
use

```python
int_value = 20 // 8
```

The second example will return the integer `2` whereas the first example gives `2.5`. We don't need the precision of a floating point value so lets stick with integers to keep everything simple.


```python
def attack(self):
    # Calculate lowest attack value as an integer.
    # Use random.randint(a, b) to select a random attack value.
    # Return attack value.
```
Complete this function using the techniques you've learned so far.

You'll need to work with values that were instantiated in the constructor earlier.

Finally we should be able to update our attack value if we need to.

## Finish the update_attack Method
**TODO:**
Write your own implementation of the `update_attack` method. All it should do is update the value of the current attack strength with the new value passed in as a parameter.


## Build the Hero Class
Here we define what we want our `Hero` class to look like. Our hero should have a name and it should be able to store several different abilities. We'll store each of our hero's abilities as an element in a Python list. 

Let's start with the constructor for `Hero`. 

The constructor for `Hero` should look like this:
```python
def __init__(self, name):
    self.abilities = list()
    self.name = name
```
Here we create a new empty list that will store our abilities. We also need to save the ability name as an instance variable.

## Create add_ability method
```python
def add_ability(self, ability):
    # Append ability to self.abilities
```
Use the append method to add a new ability to our `abilities` list. 
*Hint*: We used the append method to add strings to a list in the Rainbow Checklist tutorial. 

Finally we'll need to allow our hero to use their abilities. We need to be able to run the `attack` method that exists in every ability in our list. 


## Create attack method
```python
def attack(self):
    # Call the attack method on every ability in our ability list
    # Total up and return the total of all attacks 
```
This method should iterate over our `abilities` list and call the `attack()` method on every ability. Total up the amount of every attack and return it at the end of the function. 

Use a Python `for` loop to iterate over the list of abilities. We've already seen how a `for` loop returns string values from a list of strings but it also works the same way with objects. The `for` loop will return our object that we can interact with just the way we would expect.

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


## Test it out
You can test out whether your `Hero` class is working properly by adding these tests to your file:
```python
    hero = Hero("Wonder Woman")
    print(hero.attack())
    ability = Ability("Divine Speed", 300)
    hero.add_ability(ability)
    print(hero.attack())
    new_ability = Ability("Super Human Strength", 800)
    hero.add_ability(new_ability)
    print(hero.attack())
```
These lines should be added after checking `__name__` this way:

```python
import random

class Hero:
    def __init__(self, name):
        # Initialize starting values

    def add_ability(self, ability):
        # Add ability to abilities list

    def attack(self):
        # Run attack() on every ability hero has


class Ability:
    def __init__(self, name, attack):
        # Initialize starting values

    def attack(self):
        # Return attack value

    def update_attack(self, attack):
        # Update attack value


if __name__ == "__main__":
    hero = Hero("Wonder Woman")
    print(hero.attack())
    ability = Ability("Divine Speed", 300)
    hero.add_ability(ability)
    print(hero.attack())
    new_ability = Ability("Super Human Strength", 800)
    hero.add_ability(new_ability)
    print(hero.attack())
```
**Note:** Don't replace your code with this block, it should only serve as a guide. 

You should see an output similar to:
```
0
293
709
```

## A Note on Scope and Encapsulation

Many languages allow you to enforce access restrictions to various properties and methods of your object in memory. This allows the developer to prevent people from trying to access areas of memory that shouldn't be accessed or edited arbitrarily.

In Python this functionality is not present. Since Python code can be read by anyone, trying to protect areas of memory from modification becomes an exercise in futility since anyone can read and edit the code before running it. This is one of the reasons that The Benevolent Dictator of Python, Guido Van Rossum, has decided that creating a way to restrict access to variables and methods in an interpreted language creates more problems than it's worth. 

Scope and encapsulation can be thought as useful features that allow us to compartmentalise code instead of providing a measure of security.

```python
def greeting():
    message = "Hello World!"
    return message

print(message)

```
If you were to run the above block of code separately you will encounter the error:
```
NameError: name 'message' is not defined
```

This is because `message` is declared inside our function `greeting`. It can only be accessed from within our function `greeting` because of **scope**. Our function `greeting` has a **local scope** that can't be accessed from outside.

We can however flip it around like this.

```python
message = "Hello World!"

def greeting():
    print(message)

greeting()
```

This bit of code will output:

```
Hello World!
```

In this example we have declared our message variable in the **global scope**. That means we have access to them inside our functions.


### The `self` Argument
You may be seeing `self` places in our code and wonder why on earth is it necessary? You may be able to deduce that `self` allows us access to things outside of a particular method. We can get some clue about what's going on if we leave it out and see what happens.

```python
class Dog:
    def bark():
        print("Woof")

mydog = Dog()
mydog.bark()
```
You'll see an error when the bark method is run.
```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: bark() takes 0 positional arguments but 1 was given
```

What is this error saying?

Here is the clue.
```
bark() takes 0 positional arguments but 1 was given
```

When we run a method, `bark()` in this case, Python will automatically pass in a reference to the instantiated object as the first parameter to the method. This allows us to access anything else inside our object. 

Here our `bark` method doesn't accept any parameters so it fails when Python tries to pass in the instantiated object. 

Many languages take care of passing a reference to the parent invisibly by using a reserved keyword such as `this`. The Python philosophy of "explicit is better than implicit" is one of the reasons that `self` is not handled automatically behind the scenes. By explicitly passing a reference to the instantiated object, Python bypasses the issue of what `this` refers to.

In Python the word `self` is not **reserved** like the word `this` is in other languages. Not only will Python allow you to use self anywhere you like, but it doesn't even require the first parameter to be named `self`.  

```python
class Dog:
    def bark(object):
        print("Woof")

if __name__ == "__main__":
    my_dog = Dog()
    my_dog.bark()
```
As you can see instead of `self` this block of code uses the word `object`. If you run this you'll see that the output will be:

```
Woof
```
In order to maintain code clarity and to comply with industry best practises we follow the PEP8 style guide. In this case our style guide is clear:

>Always use `self` for the first argument to instance methods.

So even though it's not enforced by the language it's still important to be consistent and always use `self` the way the style guide suggests. This will allow your code to be clear and consistent across multiple projects and will match the work done by other Python developers as well.