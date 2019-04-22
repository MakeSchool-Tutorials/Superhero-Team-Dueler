---
title: "Object Oriented Programming: Dogs"
slug: superhero-objects
---

## Superhero Dueler

![](superhero-clipart.jpg)

### Wonders and Perils Await

There are times when the powers of good and evil come together in a mighty clash of force. When this happens, it's up to all of us to make sure that we make every one of our assets count. What better than a simulation to make sure you have the best team with you when the time comes to stand up to the evil forces of the galaxy's greatest foes.

Our task is to create a superhero team dueling application so we can be sure we've got the best people to fight evil with. This time we're going to use **Object Oriented Programming** to build our applications instead of relying completely on functions.

In this tutorial you will learn how to:

1. Use a **Object Oriented Programming** pattern to manage a more complex piece of software
1. Define classes and instances of classes
1. Define static methods on those classes
1. Use **inheritance** to define superclasses and subclasses

# Taking a Step Back: Dogs

Building a superhero dueler is going to get kinda complex, so let's start by exploring how **Classes** and **Object Oriented Programming** works using a simpler idea: Dogs.

![](dog.jpg)

Dogs are great. And we can use them as a simple example of Classes.

# Make a Dog Class & Dog Instance

A **class** is like a blueprint or an object. A class describes the methods and properties that will exist in the object and the computer uses that specification to create (or **instantiate**) an object in memory.

You can think of a class as the blueprint for the object that will exist in memory. You can create many objects from a single class just as a construction company can produce many buildings from a single set of blueprints. At the same time each object can store unique values in it's properties just as each car from a factory can have different options (for example, its color, model, make, date of production, previous owners etc).

### Make a Dog Class

Let's make a simple class called `Dog`.

>[action]
>Make the file `dog.py`

>```$ touch dog.py```

> Now define a class using the `class` keyword in Python, and we're going to already add one **Method** called `bark`:

>```python
# dog.py
class Dog:
    def __init__(self, name):
        self.name = name
```

# Make an Instance of the Dog Class

Now to use this **Class** or _blueprint_ of a dog, we have to run it, which saves it into memory and allows us to use it to make instances of the dog class, called **instances**. The process of creating an object in memory from the class definition is called **instantiation**. We will make an instance of the Dog class called `my_dog`.

>[action]
> Instantiate a dog instance:

>```py
# dog.py
class Dog:
    def __init__(self, name):
        self.name = name

my_dog = Dog.("Rex")
print(my_dog)
print(my_dog.name)
```

>[info]
>Properties of an instance are also called **instance variables**.

Now that we've defined the Class and then instantiated an instance of it we can run the whole file to see the print statements.

>[action]
>Run the `dog.py` file

>```$ python3 dog.py```

>What do you see?

>[solution]
>This will print:

>```bash
<__main__.Dog object at 0x101488278> # The Dog Class
Rex # your dog's name
```

# Add a Breed to your Dog

We can extend the **Properties** of your `Dog` class two ways, either on the fly, or upon **initialization**.

To add a new property on the fly, simply name it and attach it to a dog instance:

```py
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
>```
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

my_dog = Dog("Rex", "SuperDog")
print(my_dog.breed)
```

>[warning]
>**Watch Out** - if you add a property upon initialization, it is REQUIRED and you will get an error. So only put required properties into __init__.
>```
Traceback (most recent call last):
  File "dog.py", line 6, in <module>
    my_dog = Dog("Rex")
TypeError: __init__() missing 1 required positional argument: 'breed'
```
>Can you produce this error yourself by removing the breed argument "SuperDog" from your `Dog("Rex", "SuperDog")` call?

# Add an Instance Method

A class has really two parts: **properties** (data) which you've seen, and **methods** (actions) that that an instance of that class can do.

What are some actions a dog can take? How about barking? What other actions can a dog do?

Let's define our first method called `bark`. This will let us call something like this: `my_dog.bark()`. And then we can print "Woof!"

```python
class Dog:
    # Properties are defined inside the __init__ method
    def __init__(self, name):
        self.name = name
    # Methods are defined as their own named functions inside the class
    def bark(self):
        print("Woof!")

Dog("Rex")
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

When software becomes very complex, procedural programming can becoming too difficult to organize and track how a program is working. As a solution to this complexity, software engineers looked for logical and intuitive ways to **group together various data and actions**. There are multiple ways to accomplish this, but the most popular is **Object Oriented Programming** or **OOP**, which you will encounter again and again in your career as a software engineer.

We've learned how to use functions to create code that is re-usable and maintainable. We have already benefitted from some of the power that objects give us but haven't explored the depths that are available to us.

Procedural programming has its uses but it can be limiting in certain ways. **Object oriented programming** -- known as **OOP** -- seeks to develop strategies for organizing data loosely based on how we think of objects in the real world.

# Importing Your Class Module

Well crafted code should always be modular, meaning each of its reusable parts is separated into its own file.

Classes are very modular, since you can write a class in one file, and then use it anywhere using the Python keyword `import`. Let's make our code modular and separate the class code from the code that instantiates a dog and calls its methods.

Let's import the Dog class into a new file were we'll make some instances of Dog.

>[action]
>Make a new file called `my-dogs.py`. Inside there write the following code.

>```python
import dog
```

Import simply looks for a file with the specified name that also ends with `.py`. So this import statement will run the file `dog.py` and put it into memory for us to use.

You'll notice that if you run `my-dogs.py` the following will display in the terminal

```
Woof!
dog
```

Next lets move our code that calls the Dog class out of the `dog.py` file and into the `my-dogs.py` file.

```py
# dog.py
class Dog:
    def __init__(self, name):
        self.name = name
```

```py
# my-dogs.py
import dog

my_dog = Dog("Rex")
print(my_dog.breed)
```

Now run `$ python3 my-dogs.py`. You should see no difference.

>[info]
>You just **Refactored** your code. That means that you changed the way it was written to be cleaner and more modular, but it is functionally equivalent to before. Great work!

# Use self

When we call an **instance method** we can access the instance itself, inside its method, using the Python keyword `self`.

Read this example:

```python
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(self.name+" says: woof!")
```

With a constructor we are able to specify a unique name for your dog and store it in an instance variable. Instance variables, also called properties, store data that is unique to each object.

Test it for yourself.

1. Add `bark(self)` and update the print statement inside the `bark` method.
1. Now test to see if your bark method includes your dog's name:

Does it work?

# Make Another Dog

If we want another dog we can create a new dog with the name Annie this way.

```python
# my-dogs.py
import dog
...

my_other_dog = Dog("Annie")
print(my_other_dog.name)
```

If you run this you'll see the following.

```
Annie
```

# Dog Challenges & Review Questions

You like dogs! Try these challenges:

1. Make three dogs with fun names and breeds
1. Write two new methods to have the dogs sit and roll over (just print "<<DOG'S NAME>> sits", "<<DOG'S NAME>> rolls over").
1. Have one dog bark, one sit, and one roll over.

Notice how each dog displays it's unique name when you call the bark method. Do you remember why this is?

Notice how each dog makes the same sound "Woof!" when it barks. Why is this?

Now try this:

1. Add this line of code at the bottom: `Dog.greeting = "Woah"`
1. Now ask the dogs to bark again by calling the bark method on each instance.

What happened?

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
