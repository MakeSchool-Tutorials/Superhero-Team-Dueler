---
title: Create the Arena
slug: arena
---

This chapter will not walk you through as much as the previous chapters. Use what you've learned the last four chapters to finish out strong here!

## Update Hero Class

We created a simple fight in the last section but didn't use some of the classes we built. let's give our hero access to the rest of their equipment by adding these methods to the hero class.

> [action]
>
> Add the following to the Hero class:
>
```python
class Hero:
    # The code you have already written should be here.  
    # Add the following methods to your hero class...
>
    def add_weapon(self, weapon):
        '''Add weapon to self.abilities'''
        # TODO: This method will append the weapon object passed in as an
        # argument to self.abilities.
        # This means that self.abilities will be a list of
        # abilities and weapons.
        pass
>
    def add_armor(self, armor):
        '''Add Armor to self.armors
            armor: Armor Object
        '''
        # TODO: This method will add the armor object that is passed in to
        # the list of armor objects defined in the constructor: `self.armors`.
        pass
```

# Creating the Battle Arena

Our heroes need somewhere to battle. let's have our user create our heroes with all of their respective gear and abilities. Our arena will take care of creating heroes and adding them to their respective teams.

> [action]
>
> Let's create some methods in an Arena class that we can call that will allow for code reuse. Use your favorite loops with the `input()` function to build teams based on user input.
>
```python
class Arena:
    def __init__(self):
        '''Instantiate properties
            team_one: None
            team_two: None
        '''
        # TODO: create instance variables named team_one and team_two that
        # will hold our teams.
>
    def create_ability(self):
        '''Prompt for Ability information.
            return Ability with values from user Input
        '''
        # TODO: This method will allow a user to create an ability.
        # Prompt the user for the necessary information to create a new ability object.
        # return the new ability object.
        pass
>
    def create_weapon(self):
        '''Prompt user for Weapon information
            return Weapon with values from user input.
        '''
        # TODO: This method will allow a user to create a weapon.
        # Prompt the user for the necessary information to create a new weapon object.
        # return the new weapon object.
        pass
>
    def create_armor(self):
        '''Prompt user for Armor information
          return Armor with values from user input.
        '''
        # TODO:This method will allow a user to create a piece of armor.
        #  Prompt the user for the necessary information to create a new armor
        #  object.
        #
        #  return the new armor object with values set by user.
        pass
>
    def create_hero(self):
        '''Prompt user for Hero information
          return Hero with values from user input.
        '''
        # TODO: This method should allow a user to create a hero.
        # User should be able to specify if they want armors, weapons, and
        # abilities.
        # Call the methods you made above and use the return values to build
        # your hero.
        #
        # return the new hero object
        pass
>
    def build_team_one(self):
        '''Prompt the user to build team_one '''
        # TODO: This method should allow a user to create team one.
        # Prompt the user for the number of Heroes on team one
        # call self.create_hero() for every hero that the user wants to add to team one.
        #
        # Add the created hero to team one.
        pass
>
    def build_team_two(self):
        '''Prompt the user to build team_two'''
        # TODO: This method should allow a user to create team two.
        # Prompt the user for the number of Heroes on team two
        # call self.create_hero() for every hero that the user wants to add to team two.
        #
        # Add the created hero to team two.
        pass
>
    def team_battle(self):
        '''Battle team_one and team_two together.'''
        # TODO: This method should battle the teams together.
        # Call the attack method that exists in your team objects
        # for that battle functionality.
        pass
>
    def show_stats(self):
        '''Prints team statistics to terminal.'''
        # TODO: This method should print out battle statistics
        # including each team's average kill/death ratio.
        # Required Stats:
        #     Declare winning team
        #     Show both teams average kill/death ratio.
        #     Show surviving heroes.
        pass
```

Test your functions by either creating a new test file and using pytest, or by calling your methods this way:

```python
if __name__ == "__main__":
    arena = Arena()
    arena.build_team_one()
    arena.build_team_two()
    arena.team_battle()
    arena.show_stats()
```

# Feedback and Review - 2 minutes

**We promise this won't take longer than 2 minutes!**

Please take a moment to rate your understanding of the learning outcomes from this tutorial, and how we can improve it via our [tutorial feedback form](https://forms.gle/HLW9m4pSohADjkX1A)

This allows us to get feedback on how well the students are grasping the learning outcomes, and tells us where we can improve the tutorial experience.

# Creating a Game Loop

Our program right now has the parts and pieces to run once before it exits. This is fine for one off scripts that can run without user input, but games should be interactive. Our interactivity will come from a useful programming pattern called the **game loop**.

A typical game loop will do a few things over and over again:

* check for user input
* check length of time between loops
* update the game state
* render output to screen

Our terminal game isn't really your typical game so our game loop will be a bit different.

Since our game doesn't rely on quickly rendering complicated scenes to the screen we're not so concerned with frame rate and by extension the time between calling our render function. Our program instead will pause for user input and take actions depending on that.

You can create a simple game loop in your `superheroes.py` file this way:

This code snippet will get you started with your game loop. Here on every loop we battle our teams, show the battle outcome, and check whether we want to loop again.

```python
if __name__ == "__main__":
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    #Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        #Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            #Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()
```

**Congrats on finishing the Superhero Team Dueler tutorial!!** This is just the start of what you can make. Add to your game with these stretch challenges.

## Stretch Challenges
> [challenge]
>
> * Add a command line interface that allows for recreating or editing  of teams.
> * Allow use of only "authorized" abilites, weapons, and armor controlled by the Arena.
> * Add tests that cover more edge cases.
> * Change the way health is dealt out across the team. i.e. create heroes that may take damage first or may take more of the team's damage.
> * Write additional classes that implement different ways to attack or defend -- i.e. create a relic class that only defends against abilities.
> * Develop a way to steal weapons and abilities from the opposing team.
> * Add rewards for team success such as weapon drops.
