---
title: Build Ability and Armor Classes
slug: build-ability-and-armor-classes
---

In this chapter we are going to make classes for Armor and Abilities so each of our heroes is unique and each battle has the potential to have a different outcome.

- Some classes we will give you the code to use. Be sure to read through it and reference the comments so that you know what it is doing. This is important because...
- Other classes we will _NOT_ give you the code, and will only give you a docstring that describes what the code is supposed to do. Use this as a template and replace `pass` with your own code.
    - Use your prior learnings and the code we gave you to help build out the code needed for these classes

Here is an overview of what you will build in this chapter:

* Ability Class
  1. `__init__`: Parameters: name: String, max_damage: Integer
  2. `attack`: No Parameters

* Armor Class
  1. `__init__`: Parameters: name: String, max_block: Integer
  2. `block`: Parameters: None

After we implemented the above classes, we are going to expand our Hero class so that it is able to use the armor and abilities classes to make our heroes stronger! To do so, we will adjust the hero class to have the following design:

* Hero Class
  1. `__init__`: Parameters: name:String, starting_health:Int (default value: 100)
  2. `add_ability`: Parameters: ability:Ability Object
  3. `attack`:  No Parameters
  4. `defend`: incoming_damage: Integer
  5. `take_damage`: Parameters: damage
  6. `is_alive`: No Parameters
  7. `fight`: Parameters: opponent: Hero Class  


# Every Hero Needs an Ability

Instead of remaking our `Hero` class first, let's start with the classes our `Hero` class will need to use.

Our hero will need an ability to be able to save the world. let's start by creating a class named `Ability` that our hero can use.

Let's give our `Ability` class two simple methods, `__init__`, and `attack`.

> [action]
>First, in your project directory, make a file named 'ability.py' to contain all the code for the Ability class
>
## Set initial values with a constructor

> [action]
>
> Use a constructor to set the name and attack strength for our `Ability` just like you did in the last section with `name` in our `Dog` class.
>
```python
class Ability:
    def __init__(self, name, max_damage):
        '''
       Initialize the values passed into this
       method as instance variables.
        '''
>
        # Assign the "name" and "max_damage"
        # for a specific instance of the Ability class
        self.name = name
        self.max_damage = max_damage
```

Our next task is to write the `attack` method. To make it more interesting we don't want our Hero to have the same attack value every time. We want to have some range of values that are possible when our Hero attacks. We'll use the random module for this functionality

> [action]
>
> Import `random` at the very top of your file using the following command.
>
```python
import random
```

The `random` module has a method called `randint()` that takes two values, a minimum and maximum value. It will return some random value between the two.

You can then call:

```python
random.randint(2, 7)
```

This will return back to you some value between and including 2 and 7.

> [action]
>
> Use this knowledge to return a random value between 0 and the strongest attack an ability can produce.
>
```python
class Ability:
>
# code for __init__ method
...
>
  def attack(self):
      ''' Return a value between 0 and the value set by self.max_damage.'''
>
      # Pick a random value between 0 and self.max_damage
      random_value = random.randint(0,self.max_damage)
      return random_value
```

## Test your code out

You don't want to write a bunch of code without testing to see if it runs.

> [action]
>
> When you finish the `Ability` class, you can test your work by calling your new methods at the end of the file like this:
>
```python
import random
>
class Ability:
# ability class code
...
>
if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    ability = Ability("Debugging Ability", 20)
    print(ability.name)
    print(ability.attack())
```

If your code is written correctly you should see a number between 0 and 20 appear in the terminal if you use this example to test with.

My code gives me the following:

```
Debugging Ability
4
```

But your values may be different since we're using a random number generator.

# Add Armors
> [action]
>
>In your project directory make a file named 'armor.py' and placing the Armor class inside of it


You can't go into battle unprepared. We need to give our heroes armor that they can use to defend themselves.

> [action]
>
> Create a new class called `Armor` that contains two methods: `__init__` and `block`.

The block method should return an integer between 0 and the max_block strength.

For this class, we will _not_ give you the code. Take your learnings from making the `Ability` class and apply them here, there are a lot of similarities. Remember to remove the `pass` line

> [action]
>
> Build the Constructor
>
```python
class Armor:
    def __init__(self, name, max_block):
        '''Instantiate instance properties.
            name: String
            max_block: Integer
        '''
        # TODO: Create instance variables for the values passed in.
        pass
```

Let's create a method that we can call that will calculate the amount we will block with.

> [action]
>
> Build the `block` method for the Armor class
>
```python
def block(self):
    '''
    Return a random value between 0 and the
    initialized max_block strength.
    '''
    pass
```

When you're done, add to the test code you wrote earlier to check your answer:

> [action]
>
> Create an instance of `Armor` and check that your properties and methods work correctly:
>
```python
if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    armor = Armor("Debugging Shield", 10)
    print(armor.name)
    print(armor.block())
```

If your code is written correctly you should see a number between 0 and 10 appear in the terminal if you use this example to test with.

My code gives me the following:

```
Debugging Shield
7
```

Now that we have built our heroes armors and abilities classes, the next chapter will focus on adding these to our heroes!

# Move to the Next Section

Great work on building out your first few classes!
