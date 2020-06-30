---
title: Build Hero Class
slug: build-hero-class
---

> [action]
>
> Let's use what we've learned to build the hero class in a file named `hero.py`. Create that file right now. **Not all of the code for this tutorial will be contained in this file!**

Before we get started, it's important to know how we will build out this file:

- Some classes we will give you the code to use. Be sure to read through it and reference the comments so that you know what it is doing. This is important because...
- Other classes we will _NOT_ give you the code, and will only give you a docstring that describes what the code is supposed to do. Use this as a template and replace `pass` with your own code.
    - Use your prior learnings and the code we gave you to help build out the code needed for these classes

Here is an overview of what you will build in this chapter:

* Hero Class
  1. `__init__`: Parameters: name:String, starting_health:Int (default value: 100)
  2. `fight`: Parameters: opponent: Hero Class  


# Build out the Hero Class
Here we define what we want our `Hero` class to look like. Each hero will need attributes such as starting and current health. Let's set these as some starting value when we create each Hero in memory.

Let's walk through each method and smoke test them as we go.

> [action]
>
> Build out the Hero class constructor:
>
```python
class Hero:
    # We want our hero to have a default "starting_health",
    # so we can set that in the function header.
    def __init__(self, name, starting_health=100):
        '''Instance properties:
          name: String
          starting_health: Integer
          current_health: Integer
        '''
>
    # we know the name of our hero, so we assign it here
    self.name = name
    # similarly, our starting health is passed in, just like name
    self.starting_health = starting_health
    # when a hero is created, their current health is
    # always the same as their starting health (no damage taken yet!)
    self.current_health = starting_health
    ```

Ok, we can initialize a hero! Now let's test it:

> [action]
>
> After completing the method, add a call to your newly created constructor at the bottom of the file. This will let you test what you just did.
>
> **Hint:** The bottom of your file should look like this:
>
```python
if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    my_hero = Hero("Grace Hopper", 200)
    print(my_hero.name)
    print(my_hero.current_health)
```

If you've done it correctly you should be able to set the values and see them in the terminal when running the file:

```
Grace Hopper
200
```

Note that we can still provide a value for `starting_health` which replaces the default value of 100 that we gave in the `__init__` method! If when we instantiated our hero we had just put `Hero("Grace Hopper")`, then their `current_health` would've been 100!


# Fight!

It's time to get a one vs one battle happening! Your job is to create a method that will allow each hero to attack the other.

The `fight()` method will take an `opponent` as a parameter. An `opponent` is another instance of `Hero`.

Since we haven't added abilities and armor to our heroes, we'll start by randomly choosing a winner.


The core functionality for this method will come from calling methods that exist in the current instantiated object (using `self`) as well as calling methods on the `opponent` object that is passed in as a parameter.

> [action]
>
> Build the `fight` method for the Hero class! Take everything you've learned so far in this chapter and apply it to creating this method!
>
```python
def fight(self, opponent):
  ''' Current Hero will take turns fighting the opponent hero passed in.
  '''
  # TODO: Fight each hero until a victor emerges.
  # Phases to implement:
  #1) randomly choose winner
```

## Continue To Test it out

You can test out whether your `Hero` class is working properly by adding these tests to your file:

```python
if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")

    hero1.fight(hero2)
```

You should see an output similar to:

```
Wonder Woman won!
```

Since we randomly chose a winner, either hero has an equal likelihood to win. In later chapters, we'll add armor and abilities to the heroes to make the battle much more interesting!

# Move to the Next Section

Great work on building out your first few classes! Now that we have the basic functionality that allows our heroes to duel each other, we can expand on this to make our Superhero Dueler much more complex.
