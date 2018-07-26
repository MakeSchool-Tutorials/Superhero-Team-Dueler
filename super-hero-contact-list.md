# Super Hero Team Dueling
## Wonders and Perils Await
There are times in this world when the powers of good and evil come together in a mighty clash of force. When this happens, it's up to all of us to make sure that we make every one of our assets count. What better than a simulation to make sure you have the best team with you when the time comes to stand up to the evil forces of the galaxy's greatest foes.

Our task is to create a super hero team dueling application so we can be sure we're up to snuff.

## Procedural vs Object Oriented Programming
So far we've learned how to use functions to create code that is re-usable and maintainable. We've been able to leverage some of the power of objects but haven't yet jumped into creating them. 

Procedural programming has its uses but can be limiting in certain ways. **Object oriented programming** -- known as **OOP** -- seeks to develop strategies for organizing data loosely based on how we think of objects in the real world. 

## Classes vs Objects
We've seen and used objects in Python already. Objects are created according the the specifications described in a **class**. You can think of a class as the blueprint for the object that will exist in memory. You can create many objects from a single class just as a factory can produce many cars from a single set of specifications.

A class will describe which **methods** (blocks of code) should exist within an object along with any data that it needs to keep.

Data is stored as **properties** within the object that may be accessed either directly or through functions that can abstract away any complexities that may arise when setting a value.

Our methods and properties are a similar concept to functions and variables except now they exist inside our objects in memory.

### Class Definition
```python
class SampleClass:
    greeting = "Hello World
    def hello(self):
        print(self.greeting)
```
Here's an example of how you can define a simple class. We have here a method called `hello` and a property named `greeting`. The syntax is similar to the syntax that we've already seen when building functions but there are some key differences.

We can't just call `SampleClass.hello()` and expect something to happen though. We must first create the object in memory before we can use it. The process of creating an object in memory from the class definition is called **instantiation**. This is because we are creating an instance of the class that we made. Different instances may have different data as we will see.

```python
MyObject = SampleClass()
```
This line will take the class definition of SampleClass and **instantiate** a new object in memory. We can then refer to the object's memory address as the name `MyObject`.

Try this code out in your own file named `super-heroes.py`.

```python
class SampleClass:
    greeting = "Hello World
    def hello(self):
        print(self.greeting)


MyObject = SampleClass()
MyObject.hello()
```

If you run this file in the terminal you should see the following output.

```
Hello World
```

### Constructors
Many times you'll want to specify the data that should exist in your object when its instantiated. This is done with the use of a **constructor**. All a constructor does is setup your object with certain values when it's created.

We can add a constructor to our sample class as easily as this.

```python
class SampleClass:
    def __init__(self, greeting):
        self.greeting = greeting

    def hello(self):
        print(self.greeting)
```

We can then instantiate this class with its own default greeting this way.

```python
MyObject = SampleClass("Hello Make School")
MyObject.hello()
```

This will output

```
Hello Make School
```
in the terminal.

When we define the function `__init__` Python will run it automatically when it creates a new object.

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
