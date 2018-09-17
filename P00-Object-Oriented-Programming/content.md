---
title: Superhero Objects
slug: superhero-objects
---

## Superhero Team Dueling
![](superhero-clipart.jpg)

### Wonders and Perils Await
There are times when the powers of good and evil come together in a mighty clash of force. When this happens, it's up to all of us to make sure that we make every one of our assets count. What better than a simulation to make sure you have the best team with you when the time comes to stand up to the evil forces of the galaxy's greatest foes.

Our task is to create a superhero team dueling application so we can be sure we've got the best people to fight evil with. This time we're going to use **object oriented programming** to build our applications instead of relying completely on functions.

### Procedural vs Object Oriented Programming
We've learned how to use functions to create code that is re-usable and maintainable. We have already benefitted from some of the power that objects give us but haven't explored the depths that are available to us.

Procedural programming has its uses but it can be limiting in certain ways. **Object oriented programming** -- known as **OOP** -- seeks to develop strategies for organizing data loosely based on how we think of objects in the real world.

### Classes vs Objects
We've seen and used objects in Python already. A Python list for example is an object that we've already encountered. Objects hold data (called **properties**) and code (called **methods**). Both properties and methods are similar to the **variables** and **functions** that we've already seen and written. The difference is that properties and methods are localized to the **scope** of their object.

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

Here we have a `list` object that Python gives us. The `list` class contains methods such as `append()` that we can run to manipulate our list object.

## What is an Object?
An object is a collection of data (properties) and code (methods) somewhere in memory.

Above, our memory address is referred by the name `dogs`.

Through that memory address you can access the properties and methods within the object.

## What is a Class?
A **class** on the other hand is simply the specification that tells the computer what our object needs. A class describes the methods and properties that will exist in the object and the computer uses that specification to create (or **instantiate**) the object in memory.

You can think of a class as the blueprint for the object that will exist in memory. You can create many objects from a single class just as a factory can produce many cars from a single set of specifications. Each object can have unique values just as each car from a factory can have different properties (for example, its color).

A class will describe which **methods** (blocks of code) that should exist within an object along with any data that it needs to keep.

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
import dog
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

if __name__ == "__main__":
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
