# Super Hero Team Dueling
## Wonders and Perils Await
There are times in this world when the powers of good and evil come together in a mighty clash of force. When this happens, it's up to all of us to make sure that we make every one of our assets count. What better than a simulation to make sure you have the best team with you when the time comes to stand up to the evil forces of the galaxy's greatest foes.

Our task is to create a super hero team dueling application so we can be sure we've got the best people to fight evil with. This time we're going to use **object oriented programming** to build our applications instead of relying completely on functions.

## Procedural vs Object Oriented Programming
We've learned how to use functions to create code that is re-usable and maintainable. We have already benefitted from some of the power that objects give us but haven't explored the depths that are available to us. 

Procedural programming has its uses but it can be limiting in certain ways. **Object oriented programming** -- known as **OOP** -- seeks to develop strategies for organizing data loosely based on how we think of objects in the real world. 

## Classes vs Objects
We've seen and used objects in Python already. A Python list for example is an object that we've already encountered. Objects hold data — called **properties** — and code which is organized in **methods** ( Similar to the functions that we've already written but localized to the scope of our object).

```python
dogs = list()
dogs.append("German Shepherd")
dogs.append("Poodle")
print(dogs)
```
If you run this you'll see the output:

```
['German Shepherd', 'Poodle']
```

Here we we have a list object that Python gives us. It contains methods such as `append()` that we can run to manipulate our list. 

An object exists in the computer's memory somewhere and is accessed through the object's memory address. Here our memory address is referred by the name `dogs`. A **class** on the other hand is simply the specification that tells the computer what our object needs. It describes the methods and properties that are to exist in the object and the computer uses it to build the object in memory.

You can think of a class as the blueprint for the object that will exist. You can create many objects from a single class just as a factory can produce many cars from a single set of specifications. Each object can have unique values just as each car from a factory can have different properties like color and such.

A class will describe which **methods** (blocks of code) should exist within an object along with any data that it needs to keep.

### Class Definition
```python
class Dog:
    def bark(self):
        print("Woof!")
```
Here's an example of how to make a simple class. Our Dog class has a method called `bark` that when called will print out `Woof!` to the terminal. The syntax is similar to the syntax that we've already seen when building functions but there are some key differences.

We can't just call `Dog.bark()` and expect something to happen. That would be like asking all dogs to bark. Instead, you just want to ask *your* dog, Spot, to bark. 

First, we must create an **instance** of our Dog class in memory before we can use it. The process of creating an object in memory from the class definition is called **instantiation**. Our Dog class defines the instructions for Python to create a version, known as an **instance**, of it in memory.

```python
my_dog = Dog()
```
This line will take our class definition `Dog` and create an **instance** of it in memory. We can then refer to the object's memory address as the name `my_dog`.

Try this code out in your own file named `dog.py`.

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

### Making Your Code Modular
Typically you'll want your code to be modular. We should be able to import our code into other projects without any issues. Python gives us a way to check where our code is being run with the built-in variable `__name__` which will come in handy.

At the bottom of your `dog.py` file add this line:
```python
print(__name__)
```
When run in the terminal this way `python ./dog.py` you should see
```
Woof!
__main__
```

Inside a different file named `my-dogs.py` write the following code.

```python
import dogs
```

The import statement allows us to "invoke the import machinery" according to the Python Software Foundation.

Import simply looks for a file with the specified name that also ends with `.py`. Here we have `Dog` described in our `dog.py` file. We had to import it using `import dog` in order for it to work properly. 

You'll notice that if you run `my-dogs.py` the following will display in the terminal

```
Woof!
dog
```
Can you see what's going on?

When we import our `dog.py` file, the value for `__name__` is `dog` — the filename in which it exists. Instead when we ran our `dog.py` file directly in the terminal the value for `__name__` was `__main__`.

Why is this a thing?

As you can see, when we imported our `dog` module it immediately ran code that really shouldn't be run when if we were going to use it as a proper module.

This means that we should check to see if our code is being run as a module or not if we want to to execute statements the way we did.

Add a check to your `dog.py` file to modularize it this way.

```python
class Dog:
    def bark(self):
        print("Woof!")

if __name__ == "__main__"
    my_dog = Dog()
    my_dog.bark()
```

You'll notice if you run the `python ./dog.py` you'll see the familiar output
```
Woof!
```
However, if you run `python ./my-dogs.py` there won't by any output.

We now have behavior the plays well with modularization.

### Properties
We've seen how to instantiate a Dog object which can bark, but our dog is missing a key component -- a name. Our dog exists at a memory addess that we've labeled `my_dog` but that's not our dog's name. Our anonymous dog may need to own certain unique values or **properties** that should be accessible by that object. Our dog object has no idea what we've decided to name the memory address where it lives so we can't count on the variable name to save this information. 

*Can we just set the name in the class definition like this?*

```python
class Dog:
    name = "Spot"

    def bark(self):
        print("Woof!")
```

This will work if all dogs were named Spot, but this obviously isn't the case. If I had a second dog that I wanted to name `Annie` I would have to change the class definition every time I instantiated another dog. This kind of thing is possible, but will inspire in you and your coworkers headaches and sadness down the road.

We'll need another tool to accomplish this task.

### Constructors
Many languages give you the ability to specify your own method for instantiating a class as an object in memory. This special method is called a **constructor** because it constructs your object in memory. Specifying a constructor allows us to initialize our object with unique values at creation.

The variable `name` above is defined in the class and shared by all objects instantiated by this class. This type of variable is called a **class variable** and it has some special features that may be surprising. Using a class variable to save a name is not the way we should approach this problem however. 

We should use the python method `__init__` to set any initial values at the time our object is created in memory.  All this does is allow you to specify any initial setup steps involved when Python creates your object.

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

## Build Ability and Hero classes
Let's use what we've learned to build a couple classes in a file named `super-heroes.py`.

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
    hero.attack()
    ability = Ability("Divine Speed", 300)
    hero.add_ability(ability)
    hero.attack()
    new_ability = Ability("Super Human Strength", 800)
    hero.add_ability(new_ability)
    hero.attack()
```
**Note:** Don't replace your code with this block, it should only serve as a guide. 

You should see an output similar to:
```
0
293
709
```
## A Note on Scope and Encapsulation
**Note**: Encapsulation - collecting values together

Many languages allow you to enforce access restrictions to various properties and methods of your object in memory. This allows the developer to prevent people from trying to access areas of memory that shouldn't be accessed or edited arbitrarily.

In Python this functionality is not present. Since Python is not compiled and distributed in a form that is incomprehinsible by anyone other than a computer, trying to protect areas of memory from modification becomes an exercise in futility. Since Python is interpreted instead of compiled, anyone can read and edit the code before running it. This is one of the reasons that The Benevolent Dictator of Python, Guido Van Rossum, has decided that creating a way to restrict access to variables and methods in an interpreted language creates more problems than it's worth. 

The idea of encapsulation 


### Getters and Setters
**Note** update getters and setters, describe why it's not useful in python.

Instance variables are usually managed by **getters** and **setters**. This can allow complicated actions to be simplified to a simple function call. This simplification of functionality is called **abstraction** and is one of the strengths of OOP. By abstracting complicated functionality behind a simple interface such as a method call we are able to keep our code modular and understandable. 

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
        self.sleep_time = sleep_time

    def sleep(self):
        print(
            "{} sleeps for {} hours {}".format(
                self.name,
                self.sleep_duration))


class Dog(Animal):
    def __init__(self, name, sleep_duration, sleep_time):
        super().__init__(self, name, sleep_duration, sleep_time)

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

Lets use what we learned here to give our super heroes abilities they can use.

## Weapon Class
We've already built an `Ability` class that will give our super heroes a way to fight, but many superheroes have more than just abilities. Let's give our superheroes weapons they can use.

We can reuse the functionality in `Ability` so that we don't need to duplicate code. Lets say that weapons aren't as effective as super hero abilities so we should rewrite our attack function to allow for greater variability in attack strength. Lets make our weapons attack power range between 0 ( a miss ) to the full attack value of the weapon. 

Here are the methods that you'll need to write for our new `Weapon` class.

```python
class Weapon(Ability):
    def __init__(self, ...):
        # This method should initialize all required
        # values in Ability. Use super() to call init with 
        # the required intialized values.

    def attack(self):
        # This method should should return a random value 
        # between 0 and the full attack power of the weapon.
```
Here we've defined a method that already exists in our inherited `Ability` class. 

This is called **method overriding** and allows you to specify a different functionality for methods that are inherited from the superclass. When we call `attack()` on our `Weapon` object it will run the `attack` method specified in the `Weapon` class and not the one in `Ability`.

## Build Team class
Super heroes should be team players, so lets create a team class that can manage all of our super heroes.


```python
class Team:
    def init(self, name):
        """Instantiate resources."""
        self.name = name
        self.heroes = list()

    def add_hero(self, name):
        """Add hero to team."""
        pass

    def remove_hero(self, name):
        """Remove hero from team."""
        pass
 
    def find_hero(self, name):
        """Return hero object."""
        pass

    def view_all_heroes(self):
        """Print out all heroes."""
        pass

```

These are some of the methods you'll need to implement.

 The Team class saves hero objects in a list. You'll need to use methods that exist in the built-in Python list (`self.heroes`) to add and remove heroes to the team. This code is going to be very similar to the code that you wrote in Rainbow Checklist except that instead of add strings to our list, we want to add `Hero` objects.

### find_hero




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
