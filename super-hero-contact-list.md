# Super Hero Team Dueling
## Wonders and Perils Await
There are times in this world when the powers of good and evil come together in a mighty clash of force. When this happens, it's up to all of us to make sure that we make every one of our assets count. What better than a simulation to make sure you have the best team with you when the time comes to stand up to the evil forces of the galaxy's greatest foes.

Our task is to create a super hero team dueling application so we can be sure we're up to snuff.

## Procedural vs Object Oriented Programming
So far we've learned how to use functions to create code that is re-usable and maintainable. We've been able to leverage some of the power of objects but haven't yet jumped into creating them. 

Procedural programming has its uses but it can be limiting in certain ways. **Object oriented programming** -- known as **OOP** -- seeks to develop strategies for organizing data loosely based on how we think of objects in the real world. 

## Classes vs Objects
We've seen and used objects in Python already. Objects are created according the the specifications described in a **class**. You can think of a class as the blueprint for the object that will exist in memory. You can create many objects from a single class just as a factory can produce many cars from a single set of specifications.

**
TODO:
Give Examples...

A class will describe which **methods** (blocks of code) should exist within an object along with any data that it needs to keep.

bark

Data is stored as **properties** within the object that may be accessed either directly or through functions that can abstract away any complexities that may arise when setting a value.

name

Our methods and properties are a similar concept to functions and variables except now they exist inside our objects in memory.

### Class Definition
```python
class Dog:
    def bark(self):
        print("Woof!")
```
Here's an example of how to make a Dog class. Our Dog class has a method called `bark` that when called will print out `Woof!` to the terminal. The syntax is similar to the syntax that we've already seen when building functions but there are some key differences.

We can't just call `Dog.bark()` and expect something to happen though. That would be like asking all dogs to bark. Instead, you just want to ask *your* dog, Spot, to bark. 

First, we must create an **instance** of our Dog class in memory before we can use it. The process of creating an object in memory from the class definition is called **instantiation**. Our Dog class defines the instructions for Python to create a version or **instance** of it in memory.

```python
my_dog = Dog()
```
This line will take our class definition `Dog` and create an **instance** of it in memory. We can then refer to the object's memory address as the name `my_dog`.

Try this code out in your own file named `my-dogs.py`.

```python
class Dog:
    def bark(self):
        print("Woof!")


my_dog = Dog()
my_dog.bark()
```

If you run this file in the terminal you should see the following output.

```
Woof!
```

We first must define what an object should include with the class definition. Then we create an instance of it as an object in memory. The object is what we refer to when we want to run any code associated with it.

So far we can instantiate a Dog object which can bark, but our dog is missing a key component -- a name. Our dog exists at a memory addess that we've labeled `my_dog` but that is not our dog's name. Our anonymous dog may need to own certain unique values or **properties** that should be accessible by that object. Our dog object has no idea what we've decided to name the memory address where it lives so we can't count on the variable name to save this information. 

*Can we just set the name in the class definition like this?*

```python
class Dog:
    name = "Spot"

    def bark(self):
        print("Woof!")
```

This will work if all dogs were named Spot, but this obviously isn't the case. If I had a second dog that I wanted to name `Annie` I would have to change the class definition every time I instantiated another dog. This kind of thing is possible, but will inspire in you and your coworkers headaches and sadness.

We'll need another tool to accomplish this task.

### Constructors
Many times you'll want your object to include data associated with it. We've seen how to create a variable that all instantiated objects will share. This type of variable is called a **class variable** and it has some special features that may be surprising. Using a class variable to save a name is not the way we should approach this problem however. Fortunately we have other options available to us. 

We can use a **constructor** to set any initial values at the time your object is created in memory. All this does is allow you to specify any initial setup steps involved when Python creates your object.

This is how to add a constructor to your class.


```python
class Dog:
    greeting = "Woof!"

    def __init__(self, name):
        self.name = name

    def bark(self):
        print(self.greeting)
    
```

With a constructor we are able to specify a unique name for our dog this way.

```python
my_dog = Dog("Spot")
print(my_dog.name)
```

This will output

```
Spot
```
in the terminal.

If we want another dog we can create a new dog with the name Annie this way.

```python
my_other_dog = Dog("Annie")
print(my_other_dog.name)
```

If you run this you'll see the following.

```
Annie
```

### Instance Variables
```python
class Dog:
    greeting = "Woof!"

    def __init__(self, name):
        self.name = name

    def bark(self):
        print(self.greeting)
```
The constructor that we made earlier allows us to store different values for our dog's name. These values or **instance variables** allow us to have unique values for each instance in which they reside. Instance variables are contrasted with **class variables** which is what we call variables that are defined in the class definition.

The above example contains a class variable named `greeting` and an instance variable named `name`.

Run the above code using these function calls.

```python
my_first_dog = Dog("Annie")
my_second_dog = Dog("Wyatt")

print(my_first_dog.name)
print(my_second_dog.name)

my_first_dog.bark()
my_second_dog.bark()
```

You should see
```
Annie
Wyatt
Woof!
Woof!
```

Here our dogs' names are instance variables: they are unique to the instance they belong to. Our greeting however is set in the class definition and is shared amongst all of our Dog instances.

Most of the time however we'll find instance variables to be more useful than class variables. While instance variables and methods allow for some interesting advanced behavior, it's unlikely that such complexity will be required for most of what you'll need to do.

### Getters and Setters
Instance variables are usually managed by **getters** and **setters**. This can allow complicated actions to be simplified to a simple function call. This simplification of functionality is called **abstraction** and is one of the strengths of OOP. By abstracting complicated functionality behind a simple interface such as a method call we are able to keep our code modular and understandable. 

Let's add a getter and setter to `greeting`.

We don't want `greeting` to be tied to our class definition though so we'll give it a default value when it's instantiated by updating our `Dog` class this way.

```python
class Dog:
    def __init__(self, name):
        self.name = name
        self._greeting = "Woof!"

    def bark(self):
        print(self._greeting)

    def get_greeting(self):
        return self._greeting
    
    def set_greeting(self, new_greeting):
        self._greeting = new_greeting
```

By setting `_greeting` in the constructor we're making sure it's an instance variable and not a class variable.

Call your new `Dog` class with the following lines:

```python 
first_dog = Dog("Annie")
second_dog = Dog("Wyatt")

print(first_dog.name)
print(second_dog.name)

second_dog.set_greeting("Yap! Yap!")

first_dog.bark()
second_dog.bark()
```

You should see the output:
```
Annie
Wyatt
Yap! Yap!
Woof!
```
You'll notice that `greeting` has been refactored to `_greeting`. 

Many languages allow you to specify **private properties** which cannot be accessed by anything outside of its object. This is handy for making sure that their values are controlled by the methods that are in charge of their management and not directly by some outside force. 

Python doesn't give us this feature so its common practice to prefix properties that should be considered private with an underscore. This is why `greeting` was refactored to `_greeting`.

Lets try working on our first classes: `Hero` and `Ability`.

## Build Hero and Ability classes
Lets build our project in a new file named `super-heroes.py`.

It should look like this.
```python
class Hero:
    def __init__(self, name):
        # Initialize starting values

    def add_ability(self, ability):
        # Add ability to abilities list

    def attack(self):
        # Run attack() on every ability hero has


class Ability:
    def __init__(self, name, attack_strength):
        # Initialize starting values

    def attack(self):
        # Return attack value

    def update_attack(self, attack_strength):
        # Update attack value


if __name__ == "__main__":
    # Any code here gets run if your file is run in the terminal. 
    # It won't run if your code is imported into another project.
```
Here we define what we want our hero to look like. Our hero should have a name and should be able to have various different abilities. We'll store each of our hero's abilities as an element in a Python list. Each ability will be its own object that will keep track of its own properties.

Let's start with the constructor for `Hero`. 

We'll need to save our hero's name when our object is first created. Along with our hero's name, we'll also need to create an empty Python list that will be able to hold our abilities when we add them later. 

The constructor for `Hero` should look like this:
```python
def __init__(self, name):
    self._abilities = []
    self._name = name
```

We also need to be able to add an ability to our abilities list. Since `self._abilities` is a Python list, we can use the `append` method that comes with it.

Your `add_ability` method should look like this:
```python
def add_ability(self, ability):
    self._abilities.append(ability)
```


Finally we'll need to allow our hero to use their abilities. We need to be able to run the `attack` method that exists in every ability in our list. 

**Proofreader's Note**: This example may be giving out too much code. Advise if student should build method to specification instead.
```python
def attack(self):
    attack_damage = 0
    for ability in self._abilities:
        attack_damage += ability.attack()
    print("{} attacks with {} damage".format(self._name, attack_damage))
    return attack_damage
```
This method iterates over our entire list and adds up the returned values from every run of `attack()`. It then returns the total of all attacks.

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

The constructor should set the name and attack strength for our `Ability`.

Use the `Hero` class above as an example for how to set the ability name and attack strength in our `Ability` constructor.

```python
def __init__(self, name, attack_strength):
    # Instantiate Ability name
    # Instantiate attack strength
```
Our next important function is the `attack` method. All this will need to do right now is return our maximum attack value. Later on we can tweak this for additional fun so we don't always get the same value back.
```python
def attack(self):
    return self._attack
```
Get this method to work with your instantiated variables from the constructor you just made.

Finally we should be able to update our attack value if we need to.

**TODO:**
Write your own implementation of the `update_attack` method. It should update the value of the current attack strength with the new value passed in as a parameter.

## Test it out
Make sure that you're able to create heroes with abilities that work with the following lines:
```python
    hero = Hero("Wonder Woman")
    hero.attack()
    ability = Ability("Divine Speed", 300)
    hero.add_ability(ability)
    hero.attack()
    new_ability = Ability("Super Human Strength", 800)
    hero.add_ability(new_ability)
    hero.attack()
```
These lines should be added after checking `__name__` this way:

```python
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
    hero.attack()
    ability = Ability("Divine Speed", 300)
    hero.add_ability(ability)
    hero.attack()
    new_ability = Ability("Super Human Strength", 800)
    hero.add_ability(new_ability)
    hero.attack()
```
**Note:** Don't replace your code with this block, it should only serve as a guide. 

You should get the following output when running the file in the terminal:
```
Wonder Woman attacks with 0 damage
Wonder Woman attacks with 300 damage
Wonder Woman attacks with 1100 damage
```

### The `self` Argument

### Scope and Encapsulation

## Inheritance 

## Build relic and weapons classes in inheritance-polymorphism.py

## Build Team class

## Test Driven Development
Previously we've used user stories to visualize what our finished application should look like before we began to build it. Here instead of user stories we'll use automated tests in much the same way. Test Driven Development (commonly abbreviated as **TDD**) is another way of imagining the end result before you dive into coding. However, instead of writing narratives, with TDD we actually write *code* that verifies the behavior we want our program to perform.

## Install `pytest`

## Create your first test

## Pass your first test

## Run additional Tests

## Add fight functionality

## Add fight statistics

# Stretch Challenges
## Build Interactive Menu
## Polymorphism
## Different battle implementation
