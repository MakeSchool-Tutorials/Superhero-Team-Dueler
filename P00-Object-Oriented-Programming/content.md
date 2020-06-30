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
1. Use inheritance and polymorphism to define superclasses and subclasses

# Taking a Step Back: Dogs

Every hero needs some help along their journey. Before we dive deep into the supers, we're going to enlist the help of humanity's greatest friend to help us understand the concepts behind **Object Oriented Programming**.

![dog](dog.jpg)

But wait, you might be thinking, how does a dog help us with programming?

## Properties and Methods

We've seen and used objects in Python already. A Python list for example is an object that we've already encountered. Objects hold variables (called **properties**) and functions (called **methods**).

Object oriented programming seeks to represent code similarly to the way you think of objects in the real world by describing the features (properties) - such as eye color, or breed - and actions (methods) - such as bark and eat - that are associated with the object.

## Classes

Before we can build an object however we need to create a **class** -- or the blueprint from which that object is constructed by the computer. A **class** is like a set of instructions that tells the computer how to create your object in memory. A class _describes_ the methods (functions) and properties (variables) that will exist in an object when it's created.

The `class` allows many objects to be created from a single definition just as a factory can produce many cars from a single set of designs. At the same time each object can store unique values associated with it just as each car from a factory can have different options (for example, its color, number of doors, and other features).

## Instantiation

When we create an object of a class in memory, this is called **instantiation**. Think of it as the factory creating a car (object) based on the blueprints of what a car should look like (class). An object can also be referred to as an **instance of a class**, a real thing that brings to life (in code, at least) everything the class described. We'll revisit instantiation further in this chapter.

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
        print("dog initialized!")
```

Hang on, what's that `__init__` method? And what does `self` refer to? Let's take a brief moment to discuss both of these:

## init
This is a required method that every class must have. **`__init__` describes how to create an object based on the blueprint provided by the class**. It's a special method called a **constructor**, _which runs whenever a new instance of the class is created._ We mainly use it to assign values to our properties. In this case, we take the value of `name` and assign it to `self.name` so that we can reference it for that object. But what does `self` mean?

## self

self is a keyword used in classes to refer to the specific object built from the class. If we created 100 dog objects, how does each dog know what the values of its own properties are? Is it a golden retriever, or a poodle? Does it have brown eyes or blue? **The `self` keyword allows an object to keep track of its own properties, separate from any other object of the same class.** It is also a _required_ property to every method within a class, so make sure to **always have it as the first property to any method in a class that you create.**

> [info]
>
> Python will implicitly pass `self` as the first argument to any method call, so you don't need to explicitly state it!


# Make an Instance of the Dog Class

Now to use this **Class** or _blueprint_ of a dog, we have to run it, which saves it into memory and allows us to use it to make instances of the dog class, called **instances**. As we said before, the process of creating an object in memory from the class definition is called **instantiation**. Let's make an instance of the Dog class:

>[action]
> Instantiate a dog instance:
>
```python
# dog.py
class Dog:
    def __init__(self, name):
        self.name = name
        print("dog initialized!")
>
# instantiation call that creates a Dog object:
Dog("Rex")
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

> [solution]
>
> This will print:
>
```bash
dog initialized!
```

Awesome! Our dog has been initialized, but how do we do anything with it? How do we access its name? In order to do this, **we have to save our instance to a variable!**

Remember that variables are just like empty boxes, all they do is hold stuff for us. In this case, we want the `my_dog` variable to hold an instance of our `Dog` class. Without saving the instance to a variable, the instance just lives in memory, but we won't be able to reference or access it.

> [action]
>
> Update your code to save the instance to the `my_dog` variable:
>
```python
# dog.py
class Dog:
    def __init__(self, name):
        self.name = name
        print("dog initialized!")
>
# the same instantiation call that creates a Dog object,
# but now we've assigned it to the value of the my_dog variable
my_dog = Dog("Rex")
print(my_dog)
print(my_dog.name)
```

What do you think this will print?

>[solution]
>
> This will print:
>
```bash
dog initialized! # From the init
<__main__.Dog object at 0x101488278> # The Dog Class
Rex # Your dog's name
```

Note here that for this instance of a dog, `self.name` refers to `Rex`!

# Add a Breed to your Dog

We can extend the **Properties** of our `Dog` class in two ways, either on the fly, or upon **initialization**.

To add a new property on the fly, simply name it and attach it to a dog instance:

```python
# dog.py
class Dog:
    def __init__(self, name):
        self.name = name
        print("dog initialized!")

my_dog = Dog("Rex")
# Adding the "breed" property on the fly
my_dog.breed = "SuperDog"
# will print "SuperDog"
print(my_dog.breed)
```

This works if we want one, specific object to have this property. However, if we want _all_ objects of a class to have this property, we need to add the property to the class upon initialization.

To do this, we need to update the `__init__` constructor:

>[action]
>
> Here we go:
>
```python
# dog.py
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        print("dog initialized!")
>
my_dog = Dog("Rex", "SuperDog")
print(my_dog.breed)
```
>
>**Watch Out** - if you add a property upon initialization, it is REQUIRED and you will get an error if you don't provide a value for it during initialization. So only put required properties into __init__. See an example of this error below when we don't provide a "breed" value:
>
```
Traceback (most recent call last):
  File "dog.py", line 6, in <module>
    my_dog = Dog("Rex")
TypeError: __init__() missing 1 required positional argument: 'breed'
```

>Can you produce this error yourself by removing the breed argument "SuperDog" from your `Dog("Rex", "SuperDog")` call?

# Add an Instance Method

A class has really two parts: **properties** (variables) which you've seen, and **methods** (functions) that that an instance of that class can do.

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
        print("dog initialized!")
>
    # Methods are defined as their own named functions inside the class
    # Remember to put the "self" parameter every time we make a class method!
    def bark(self):
        print("Woof!")
>
my_dog = Dog("Rex", "SuperDog")
# Remember python implicitly passes in "self",
# so we don't need to pass it in when we call the function!
my_dog.bark()
```

Our `Dog` class has a method called `bark` that when called will print out `Woof!` to the terminal. The syntax is similar to the syntax that we've already seen when building functions but, there are some key differences.

>[action]
>Run the `dog.py` file

>```$ python3 dog.py```

>What do you see?

The `bark()` method is nested within in a class definition: `class Dog:`. This defines the `bark()` method as a member of the `Dog` class.

We can't call this method on the class. We can't call `Dog.bark()` and expect something to happen. That would be like asking the blueprint of a dog to bark. That does't make sense! Instead we need to make an **Instance** of the `Dog` class and then ask that instance to bark. That is why methods defined in this way are called **Instance Methods**.

>[info]
>Remember classes are groups of data and actions, data attached to classes are key-value pairs called **Properties**, and the actions that class can take are called **Methods**.

# So Far... Procedural vs Object Oriented Programming

So far most code you've written is probably **Procedural** meaning it is written as a **series of unconnected steps** executed by the computer.

When software becomes very complex, procedural programming can become too cumbersome. As a solution to this complexity, software engineers looked for logical and intuitive ways to **group together various data and actions**. There are multiple ways to accomplish this, but the most popular is **Object Oriented Programming** or **OOP**, which you will encounter again and again in your career as a software engineer.

So far we've learned how to use functions to create code that is re-usable and maintainable. We also have already benefitted from some of the power that objects give us but haven't explored the depths that are available to us.

# Importing Your Class Module

Well crafted code should always be modular, meaning each of its reusable parts is separated into its own file.

Classes are very modular, since you can write a class in one file, and then use it elsewhere using the Python keyword `import`. Let's make our code modular and separate the class code from the code that instantiates a dog and calls its methods.

Let's import the Dog class into a new file were we'll make some instances of Dog.

>[action]
>Make a new file called `my_dogs.py`. Inside there write the following code:
>
```python
# my_dogs.py
import dog
```

Import simply looks for a file with the specified name that also ends with `.py`. So this import statement will run the file `dog.py` and put it into memory for us to use.

You'll notice that if you run `my_dogs.py` the following will display in the terminal

```
Woof!
```

> [action]
>
> Next let's move our code that calls the Dog class out of the `dog.py` file and into the `my_dogs.py` file.
>
```python
# my_dogs.py
import dog # we need to specify exactly what we want
>
my_dog = dog.Dog("Rex", "SuperDog")
my_dog.bark()
```

Now that we've moved the instantiation and call to the `bark` method into `my_dogs.py`, we can remove this code from `dog.py`:

> [action]
>
> Refactor `dog.py` to remove the lines you just put in `my_dogs.py`:
>
```python
# dog.py
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        print("dog initialized!")
>
    def bark(self):
        print("Woof!")
```

Now run `$ python3 my_dogs.py`. You should see no difference.

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

Scope and encapsulation can be thought as useful features that allow us to compartmentalize code instead of providing a measure of security.

```python
def greeting():
    message = "Hello World!"
    return message

print(message)
```

If you were to run the above block of code, you will encounter the error:

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

**This same principle is why if in `my_dogs.py` we tried to call `print(name)` or `bark()`, we would get an error. Both `name` and `bark()` only exist within the scope of a `Dog` object!**


# Make Another Dog

> [action]
>
> If we want another dog we can create a new dog with the name Annie this way.
>
```python
# my_dogs.py
import dog
...
>
my_other_dog = dog.Dog("Annie", "SuperDog")
print(my_other_dog.name)
```

If you run this, in addition to your previous print statements, you should see the following:

```
dog initialized!
Annie
```

# What You Can Do Now

After just this step you can do some awesome stuff with classes and their instances. We'll use all of this as we start to build our superhero dueler!

You can...

* Define a class
* Define a class's properties
* Use an `__init__` **constructor** to specify the required properties of a class instance
* Define a class's methods
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
> Notice how each dog displays it's unique name when you print its name property. Do you remember why this is?
>
> Notice how each dog makes the same sound "Woof!" when it barks. Why is this?
