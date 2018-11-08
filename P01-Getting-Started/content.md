---
title: Build Ability and Hero Classes
slug: build-ability-and-hero-classes
---

## Build Ability and Hero classes
Let's use what we've learned to build a couple classes in a file named `superheroes.py`.

Here is an overview of what you will build.

Each method below is labeled with a doc string that describes what it is supposed to do. Use this as a template and replace `pass` with your own code.

```python
class Hero:
    def __init__(self, name, starting_health=100):
        ''' 
        Initialize these values as instance variables:
        (Some of these values are passed in above, others will need to be set at a starting value.)
        abilities:List
        name:
        starting_health:
        current_health:
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

## Build the Hero Class
Here we define what we want our `Hero` class to look like. Our hero should have a name and should be able to have several different abilities. Also our hero will need other attributes such as starting and current health. We'll need to set these at some starting value when we create our Hero in memory.

Let's start with the constructor for `Hero`.

The constructor for `Hero` should look like this:

```python
def __init__(self, name, starting_health=100):
    self.name = name
    self.starting_health = starting_health
    self.current_health = starting_health
    self.abilities = list()
```

In addition to creating our initial values, we create a new empty list that will store our heroes' multiple abilities.

## Create an add_ability method

```python
def add_ability(self, ability):
    # Append ability to self.abilities
```

Our hero will need abilties. Later on we'll see exactly what those will entail. For now we can assume that there is a class called Ability. An instance of this class -- known as an object -- will be passed into this method. 

Use the append method to add a new ability to our `abilities` list.

*Hint*: We used the append method to add strings to a list in the Rainbow Checklist tutorial. This time we're not adding strings, instead we'll add ability objects.

Finally we'll need to allow our hero to use their abilities. We need to be able to run the `attack` method that exists in every ability object that exists in our list.

## Create the attack method

```python
    def attack(self):
        ''' 
        Calculates damage from list of abilities.

        This method should call Ability.attack() 
        on every ability in self.abilities and
        return the total.
        '''
        pass
```

This method should iterate over our `abilities` list and call the `attack()` method on every ability. The method should total up the amount of every attack and return it at the end.

It's easiest to use a Python `for` loop to iterate over the list of abilities. We've already seen how a `for` loop returns string values from a list of strings but it also works the same way with objects. The `for` loop will return our object that we can interact with just the way we would expect.

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

## Take Damage

There are many ways that damage can be controlled. It's common practice to use a method to handle updating values within an object instead of just setting them directly. These are commonly referred to as getters and setters. They allow us to later on decide whether our hero will take the full damage amount or perhaps a different amount. 

Right now though lets just update our hero's current health to reflect the damage amount passed in to this method.

```python
def take_damage(self, damage):
    ''' 
    This method should update self.current_health 
    with the damage that is passed in.
    '''
    pass
```
## Are You Alive?
Let's create a function that will return a boolean value to this question.
Create Hero.is_alive() and have it return true when the hero is alive and false when they are not.

```python
def is_alive(self):  
    '''
    This function will 
    return true if the hero is alive 
    or false if they are not. 
    '''
    pass
```

## Fight!

It's time to get a one vs one battle happening! Create a method that will allow each hero to attack the other.

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

When a hero dies print to the console.

```
HeroName died
```
Where HeroName is the name of the hero that died.

The core functionality for this method will come from calling methods that exist in the current instantiated object (using self) as well as calling methods on the object that is passed in. 


## Test it out
You don't want to write a bunch of code without testing to see if it runs. Write code that will run the methods you create after the line

```python
if __name__ == "__main__":
```

You can test out whether your `Hero` class is working properly by adding these tests to your file:

```python
    hero = Hero("Wonder Woman")
    print(hero.attack())
```
This should give you:

```
0
```

Create the ability class and don't be afraid to add as many calls to your methods as necessary to make sure that your code is functioning.

### Ability Class
Let's give our `Ability` class three simple methods at first.

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

Use a constructor to set the name and attack strength for our `Ability` just like you did above with `name` in our `Dog` class.

```python
def __init__(self, name, attack_strength):
    # Set Ability name
    # Set attack strength
    pass
```

Our next task is to write the `attack` method.

Import `random` at the very top of your file using

```python
import random
```

The `random` module has a method called `randint()` that takes two values, a minimum and maximum value. It will return some random value between the two.

You'll need to use the module name in order to use this method properly.

```random.randint(2, 7)```

Will return back to you some value between and including 2 and 7.



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

You'll need to work with values that were instantiated in the constructor earlier.


## Continue To Test it out
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
    '''
    Methods not shown here for clarity
    '''
    pass


class Ability:
    '''
    Methods not shown here for clarity
    '''
    pass


if __name__ == "__main__":
    hero = Hero("Wonder Woman")
    print(hero.attack())
    ability = Ability("Divine Speed", 20)
    hero.add_ability(ability)
    print(hero.attack())
    new_ability = Ability("Super Human Strength", 30)
    hero.add_ability(new_ability)
    print(hero.attack())
    hero2 = Hero("Jodie Foster")
    ability2 = Ability("Science", 800)
    hero2.add_ability(ability2)
    hero.fight(hero2)
```

**Note:** Don't replace your code with this block, it should only serve as a guide.

You should see an output similar to:

```
0
12
39
Wonder Woman died
```

## A Note on Scope and Encapsulation

Many languages allow you to enforce access restrictions to various properties and methods of your object in memory. This allows the developer to prevent people from trying to access areas of memory that shouldn't be accessed or edited arbitrarily.

In Python this functionality is not present. Since Python code can be read by anyone, trying to protect areas of memory from modification becomes an exercise in futility since anyone can read and edit the code before running it. This is one of the reasons that the former "Benevolent Dictator of Python for Life", Guido Van Rossum, had decided that creating a way to restrict access to variables and methods in an interpreted language creates more problems than it's worth.

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

What is this error saying? Here is the clue:

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
