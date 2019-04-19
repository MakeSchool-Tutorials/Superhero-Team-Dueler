---
title: Object Oriented Programming Dogs
slug: superhero-objects
---

## Superhero Team Dueling

![](superhero-clipart.jpg)

### Wonders and Perils Await

There are times when the powers of good and evil come together in a mighty clash of force. When this happens, it's up to all of us to make sure that we make every one of our assets count. What better than a simulation to make sure you have the best team with you when the time comes to stand up to the evil forces of the galaxy's greatest foes.

Our task is to create a superhero team dueling application so we can be sure we've got the best people to fight evil with. This time we're going to use **Object Oriented Programming** to build our applications instead of relying completely on functions.

### Procedural vs Object Oriented Programming

We've learned how to use functions to create code that is re-usable and maintainable. We have already benefitted from some of the power that objects give us but haven't explored the depths that are available to us.

Procedural programming has its uses but it can be limiting in certain ways. **Object oriented programming** -- known as **OOP** -- seeks to develop strategies for organizing data loosely based on how we think of objects in the real world.

# Dog Object vs. Dog Class

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

> ## What is an Object?

>An object is a collection of data (properties) and code (methods) somewhere in memory.

>Above, our memory address is referred by the name `dogs`.

>Through that memory address you can access the properties and methods within the object.

# Define a Dog Class

```python
class Dog:
    def bark(self):
        print("Woof!")
```

Here's an example of how to make a simple class. Our Dog class has a method called `bark` that when called will print out `Woof!` to the terminal. The syntax is similar to the syntax that we've already seen when building functions but, there are some key differences.

> ## What is a Class?

>A **class** on the other hand is simply the specification that tells the computer what our object needs. A class describes the methods and properties that will exist in the object and the computer uses that specification to create (or **instantiate**) an object in memory.

>You can think of a class as the blueprint for the object that will exist in memory. You can create many objects from a single class just as a factory can produce many cars from a single set of specifications. Each object can store unique values in it's properties just as each car from a factory can have different options (for example, its color).

>A class describes the **methods** (blocks of code) that should exist within an object along with any **properties** (data) that it needs to store.


The `bark()` method is nested within in a class definition: `class Dog:`. This defines the `bark()` method as a member of the `Dog` class.

We can't just call `Dog.bark()` and expect something to happen. That would be like asking all dogs to bark. Or maybe more accurately, asking the defintition/description or blueprint of a dog to bark! Rather than asking one of the dogs created from that blueprint to bark.

Instead, you just want to ask *your* dog, Spot, to bark. Wait, you don't have a dog named spot, you'll have to make one.

You need to create an **instance** of your Dog class in memory before you can use it. The process of creating an object in memory from the class definition is called **instantiation**. The Dog class defines the instructions for Python to create an object, known as an **instance**, in memory.

```python
my_dog = Dog()
```

This line will take our class definition `Dog` and create an **instance** of it in memory. We can then refer to the object's memory address with the name `my_dog`.

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

Typically you'll want your code to be modular. We should be able to import our code into other projects without any issues. Python gives us a way to check where our code is being run with the built-in variable `__name__`. This variable will come in handy later.

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

What is going on here?

As you may have seen, importing the `dog` module immediately ran code that really shouldn't be run if we were going to use it as a proper module.

This means that we should check to see if our code is being run as a module or not before executing statements the way we did.

Think about it like this, you can use the file defining the `Dog` to hold the definition of `Dog` and create an instance named `my_dog` and tell it to bark. Other times, you may want to use the defintion of the Dog class in another project that doesn't want to create the instance `my_dog`.

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

> [info]
> A module is a file containing Python definitions and statements.

### Properties

We've seen how to instantiate a Dog object which can bark, but our dog is missing a key component -- a name. Our dog exists at a memory addess that we've labeled `my_dog` but that's not our dog's name. Our anonymous dog may need to own certain unique values called **properties** that should be accessible by that object.

All properties must be assigned to an instance and should be set when the instance is created. For this purpose there is the **constructor** function.

### Constructors

Many languages give you the ability to specify your own method for instantiating a class as an object in memory. This special method is called a **constructor** because it constructs an object in memory. Specifying a constructor allows us to initialize our object with unique values at creation.

We should use the python method `__init__` to set any initial values at the time our object is created in memory.  This allows you to specify any initial setup steps involved when Python creates your object. The most common task that will occur in the constructor is initiallizing instance variables.

Add a constructor function to the Dog class like this:

```python
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(self.name+" says: woof!")
```

With a constructor we are able to specify a unique name for your dog and store it in an instance variable. Instance variables, also called properties, store data that is unique to each object.

Test it for yourself.

```python
my_dog = Dog("Spot")
print(my_dog.name)
my_dog.bark()
```

This will output:

```
Spot
Spot says: woof!
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

### Class Variables

Class variables are different from instance variables. Remember there is only one class, while you can make create any number of instacnes from that class. Class variables represent a value that is owned by the class itself and is not stored with each instance.

Imagine that all dogs say "Woof!" when they bark. You might store this string with the class like this:

```python
class Dog:
    greeting = "Woof!"

    def __init__(self, name):
        self.name = name

    def bark(self):
        print(self.name+" says:"+Dog.greeting)
```

Here the variable `greeting` is defined in the class block, and is accessed from the `Dog` class itself: `Dog.greeting`.

Class varaibles are not as useful as instance variables, you will use them seldom. On the other hand, ervery class you create will use one or more instance variables.

### Instance Variables

Instance variables are stored with each instance, and each instance can have it's own unique values. Instance variables are also called properties.

Instance variables should be defined in the constructor.

### Compare instance variables with class variables

You like dogs! Try these challenges:

1. Make three more dogs
1. Give each a new name
1. Tell each of your dogs to bark

Notice how each dog displays it's unique name when you call the bark method. Why is this?

Notice how each dog makes the same sound "Woof!" whne it barks. Why is this?

Now try this:

1. Add this line of code at the bottom: `Dog.greeting = "Woah"`
1. Now ask the dogs to bark again by calling the bark method on each instance.

What happened?
