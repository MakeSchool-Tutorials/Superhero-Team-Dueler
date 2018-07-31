# Super Hero Team Dueling
## Wonders and Perils Await
There are times in this world when the powers of good and evil come together in a mighty clash of force. When this happens, it's up to all of us to make sure that we make every one of our assets count. What better than a simulation to make sure you have the best team with you when the time comes to stand up to the evil forces of the galaxy's greatest foes.

Our task is to create a super hero team dueling application so we can be sure we're up to snuff.

## Procedural vs Object Oriented Programming
So far we've learned how to use functions to create code that is re-usable and maintainable. We've been able to leverage some of the power of objects but haven't yet jumped into creating them. 

Procedural programming has its uses but can be limiting in certain ways. **Object oriented programming** -- known as **OOP** -- seeks to develop strategies for organizing data loosely based on how we think of objects in the real world. 

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
This line will take our class definition (Dog) and create an **instance** of it in memory. We can then refer to the object's memory address as the name `my_dog`.

Try this code out in your own file named `super-heroes.py`.

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

Can we just set the name in the class definition like this?

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

We can use a **constructor** to set any initial values at the time your object is created in memory. All this does is allow you to specify any initial setup steps involved when python creates your object.

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

If we run this we'll see

```
Annie
```

### Instance Variables

### Build Hero class

### The `self` Argument

### Scope and Encapsulation

### Build Sample class_instance.py

### Build Ability class

## Inheritance 

## Build relic and weapons classes in inheritance-polymorphism.py

## Build Team class

## Test Driven Development
Previously we've used user stories to visualize what our finished application should look like before we began to build it. Here instead of user stories we'll use automated tests in much the same way. Test Driven Development (commonly abbreviated as **TDD**) is another way of imagining the end result before you dive into coding. However, instead of writing narratives, with TDD we actually write *code* that verifies the behavior we want our program to perform.

## Install `pytest`

## Create your first test

## Pass your first test

## Add fight functionality

## Add fight statistics

# Stretch Challenges
## Build Interactive Menu
## Polymorphism
## Different battle implementation
