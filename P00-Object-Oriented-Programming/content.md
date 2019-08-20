---
title: "Object Oriented Programming: Dogs"
slug: superhero-objects
---

## Superhero Dueler

![superhero](superhero-clipart.jpg)

### Wonders and Perils Await

There are times when the powers of good and evil come together in a mighty clash of force. When this happens, it's up to all of us to make sure that we make every one of our assets count. What better than a simulation to make sure you have the best team with you when the time comes to stand up to the evil forces of the galaxy's greatest foes.

Our task is to create a superhero team dueling application so we can be sure we've got the best people to fight evil with. This time we're going to use **Object Oriented Programming** to build our applications instead of relying completely on functions.

## Learning Outcomes
By the end of this tutorial, you should be able to...

1. Use an Object Oriented Programming pattern to manage a more complex piece of software
1. Define classes and instances of classes
1. Define static methods on those classes
1. Use inheritance and polymorphism to define superclasses and subclasses

# Taking a Step Back: Dogs

Every hero needs some help along their journey. We're going to enlist the help of humanity's greatest friend to help us understand the concepts behind **Object Oriented Programming**.

![dog](dog.jpg)

How does a dog help us with programming?

## Describing a Dog as an Object

We've seen and used objects in Python already. A Python list for example is an object that we've already encountered. Objects hold data (called **properties**) and code (called **methods**). Both properties and methods are similar to the **variables** and **functions** that we've already seen and written. The difference is that properties and methods are localized to the **scope** of their object.

Object oriented programming seeks to represent code similarly to the way you think of objects in the real world by describing the features - such as color, or breed, and actions such as bark and eat -- that are associated with the object. Before we can build an object however we need to create a **class** -- or the blueprint from which that object is constructed by the computer.

A **class** is like a set of instructions that tells the computer how to create your object in memory. A class describes the methods (functions) and properties (variables) that will exist in the object when it's created (or **instantiated**) in memory.

The `class` allows many objects to be created from a single definition just as a factory can produce many toy cars from a single set of designs. At the same time each object can store unique values associated with it just as each car from a factory can have different options (for example, its color, number of doors, and other features).

# Make a Dog Class

Let's make a simple class called `Dog`.

>[action]
>Make the file `dog.py`
>
>```$ touch dog.py```
>
> Now define a class using the `class` keyword in Python, and we're going to add one **property** to the Dog class called `name`:

```python
# dog.py
class Dog:
    def __init__(self, name):
        self.name = name
```

# Make an Instance of the Dog Class

Now to use this **Class** or _blueprint_ of a dog, we have to run it, which saves it into memory and allows us to use it to make instances of the dog class, called **instances**. The process of creating an object in memory from the class definition is called **instantiation**. We will make an instance of the Dog class called `my_dog`.

>[action]
> Instantiate a dog instance:
>
```python
# dog.py
class Dog:
    def __init__(self, name):
        self.name = name
>
my_dog = Dog("Rex")
print(my_dog)
print(my_dog.name)
```

<!-- -->

>[info]
>
>Properties of an instance are also called **instance variables**.

Now that we've defined the Class and then instantiated an instance of it we can run the whole file to see the print statements.

>[action]
>Run the `dog.py` file

>```$ python3 dog.py```

>What do you see?

Here's the solution:

>[solution]
>This will print:

>```bash
<__main__.Dog object at 0x101488278> # The Dog Class
Rex # your dog's name
```

# Add a Breed to your Dog

We can extend the **Properties** of your `Dog` class two ways, either on the fly, or upon **initialization**.

To add a new property on the fly, simply name it and attach it to a dog instance:

```python
# dog.py
class Dog:
    def __init__(self, name):
        self.name = name

my_dog = Dog("Rex")
my_dog.breed = "SuperDog"
print(my_dog.breed)
```

To add a property to the class upon **initialization** we update the `__init__` **constructor**. `__init__` is a special method called a **constructor**. It runs whenever a new instance of your class is created.

>[action]
>Here we go:
>
```python
# dog.py
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
>
my_dog = Dog("Rex", "SuperDog")
print(my_dog.breed)
```
>
>**Watch Out** - if you add a property upon initialization, it is REQUIRED and you will get an error. So only put required properties into __init__.
>
```
Traceback (most recent call last):
  File "dog.py", line 6, in <module>
    my_dog = Dog("Rex")
TypeError: __init__() missing 1 required positional argument: 'breed'
```

>Can you produce this error yourself by removing the breed argument "SuperDog" from your `Dog("Rex", "SuperDog")` call?

# Add an Instance Method

A class has really two parts: **properties** (data) which you've seen, and **methods** (actions) that that an instance of that class can do.

What are some actions a dog can take? How about barking? What other actions can a dog do?

> [action]
>
> Let's define our first method called `bark`. This will let us call something like this: `my_dog.bark()`. And then we can print "Woof!"
>
```python
# dog.py
class Dog:
    # Required properties are defined inside the __init__ constructor method
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    # Methods are defined as their own named functions inside the class
    def bark(self):
        print("Woof!")
>
my_dog = Dog("Rex", "SuperDog")
my_dog.bark()
```

Our `Dog` class has a method called `bark` that when called will print out `Woof!` to the terminal. The syntax is similar to the syntax that we've already seen when building functions but, there are some key differences.

>[action]
>Run the `dog.py` file

>```$ python3 dog.py```

>What do you see?

The `bark()` method is nested within in a class definition: `class Dog:`. This defines the `bark()` method as a member of the `Dog` class.

We can't call this method on the class. We can't call `Dog.bark()` and expect something to happen. That would be like asking all dogs to bark. Or maybe more accurately, asking the blueprint of a dog to bark. That does't make sense! Instead we need to make an **Instance** of the `Dog` model and then ask that instance to bark. That is why methods defined in this way are called **Instance Methods**.

>[info]
>Remember classes are groups of data and actions, data attached to classes are key-value pairs called **Properties**, and the actions that class can take are called **Methods**.

# So Far... Procedural vs Object Oriented Programming

So far most code you've written is probably **Procedural** meaning it is written as a **series of unconnected steps** executed by the computer.

When software becomes very complex, procedural programming can become too cumbersome. As a solution to this complexity, software engineers looked for logical and intuitive ways to **group together various data and actions**. There are multiple ways to accomplish this, but the most popular is **Object Oriented Programming** or **OOP**, which you will encounter again and again in your career as a software engineer.

We've learned how to use functions to create code that is re-usable and maintainable. We also have already benefitted from some of the power that objects give us but haven't explored the depths that are available to us.

# Importing Your Class Module

Well crafted code should always be modular, meaning each of its reusable parts is separated into its own file.

Classes are very modular, since you can write a class in one file, and then use it elsewhere using the Python keyword `import`. Let's make our code modular and separate the class code from the code that instantiates a dog and calls its methods.

Let's import the Dog class into a new file were we'll make some instances of Dog.

>[action]
>Make a new file called `my-dogs.py`. Inside there write the following code.
>
```python
# my-dogs.py
import dog
```

Import simply looks for a file with the specified name that also ends with `.py`. So this import statement will run the file `dog.py` and put it into memory for us to use.

You'll notice that if you run `my-dogs.py` the following will display in the terminal

```
Woof!
```

> [action]
>
> Next let's move our code that calls the Dog class out of the `dog.py` file and into the `my-dogs.py` file.
>
```python
# dog.py
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
>
    def bark(self):
        print("Woof!")
>
# my-dogs.py
import dog # we need to specify exactly what we want
>
my_dog = dog.Dog("Rex", "SuperDog")
my_dog.bark()
```

Now run `$ python3 my-dogs.py`. You should see no difference.

> [challenge]
>
> How could we clean this up?
>
> **hint:** use [from](https://realpython.com/absolute-vs-relative-python-imports/#syntax-of-import-statements)

<!-- -->

>[info]
>You just **Refactored** your code. That means that you changed the way it was written to be cleaner and more modular, but it is functionally equivalent to before. Great work!

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

This is because `message` is declared inside our function `greeting`. Our function greeting has a 'lexical scope' which means the values are only available from within that function.

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

In this example we have declared our message variable in a 'global scope'. That means that any functions we declare will also have access to the 'global scope'. The variables that exist within the function however have a 'local scope' that is not available in the global context.


# Make Another Dog

If we want another dog we can create a new dog with the name Annie this way.

```python
# my-dogs.py
import dog
...

my_other_dog = dog.Dog("Annie", "SuperDog")
print(my_other_dog.name)
```

If you run this you'll see the following.

```
Annie
```

# What You Can Do Now

After just this step you can do some awesome stuf with classes and their instances. We'll use all of this as we start to build our superhero dueler!

You can...

* Define a class
* Define a class's properties
* Use a `__init__` **Constructor** to specify the required properties of a class instance
* Define a class's methods
* Use the class instance inside its own methods
* Import a python module into any file

Great work! Let's make this superhero dueler!

# Dog Stretch Challenges & Review Questions

Want more practice? Complete the following to sharpen your skills in this chapter!

> [challenge]
>
> You like dogs! Try these challenges:
>
> 1. Make three dogs with fun names and breeds
> 1. Write two new methods to have the dogs sit and roll over (just print "<<DOG'S NAME>> sits", "<<DOG'S NAME>> rolls over").
> 1. Have one dog bark, one sit, and one roll over.
>
> Notice how each dog displays it's unique name when you call the bark method. Do you remember why this is?
>
> Notice how each dog makes the same sound "Woof!" when it barks. Why is this?
>
> Now try this:
>
> 1. Add this line of code at the bottom: `Dog.greeting = "Woah"`
> 1. Now ask the dogs to bark again by calling the bark method on each instance.
>
> What happened?
