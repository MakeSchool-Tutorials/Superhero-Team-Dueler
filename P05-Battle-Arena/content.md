---
title: Create the Arena
slug: arena
---

## Update Hero Class
We created a simple fight in the last section but didn't use some of the classes we built. Lets give our hero access to the rest of their equipment by adding these methods to the hero class.

-
```python
class Hero:
    # The code you have already written should be here.  
    # Add the following methods to your hero class...

    def add_weapon(self, weapon):
        '''
        This method will append the weapon object passed in as an argument to the list of abilities that already exists -- self.abilities.

        This means that self.abilities will be a list of abilities and weapons.
        '''
        pass

    def add_armor(self, armor):
        '''
        This method will add the armor object that is passed in to this method to the list of armor objects defined in the initializer as self.armors.
        '''
        pass

```


Add the methods to your Hero class so that your heroes can use our newly created equipment.


## Creating the Battle Arena
Our heroes still need some help. We need some place that will allow our user to create heroes with all of their gear and abilities. Our arena will take care of creating heroes and adding them to their respective teams. 

Lets create some methods that we can call that will allow for code reuse.

```python
class Arena:
    def __init__(self):
        '''
        Declare variables
        '''
        self.team_one = None
        self.team_two = None
    
    def create_ability(self):
        '''
        This method will allow a user to create an ability.

        Prompt the user for the necessary information to create a new ability object.

        return the new ability object.
        '''
        pass

    def create_weapon(self):
        '''
        This method will allow a user to create a weapon.

        Prompt the user for the necessary information to create a new weapon object.

        return the new weapon object.
        '''
        pass
    
    def create_armor(self):
        '''
        This method will allow a user to create a piece of armor.

        Prompt the user for the necessary information to create a new armor object.

        return the new armor object.
        '''
        pass

    def create_hero(self):
        ''' 
        This method should allow a user to create a hero. 

        User should be able to specify if they want armors, weapons, and abilites. Call the methods you made above and use the return values to build your hero.

        return the new hero object
        '''
        pass

    def build_team_one(self):
        '''
        This method should allow a user to create team one.
        Prompt the user for the number of Heroes on team one and 
        call self.create_hero() for every hero that the user wants to add to team one. 

        Add the created hero to team one.
        '''
        pass

    def build_team_two(self):
        '''
        This method should allow a user to create team two.
        Prompt the user for the number of Heroes on team two and 
        call self.create_hero() for every hero that the user wants to add to team two. 

        Add the created hero to team two.
        '''
        pass

    def team_battle(self):
        '''
        This method should battle the teams together.
        Call the attack method that exists in your team objects to do that battle functionality.
        '''

    def show_stats(self):
        '''
        This method should print out battle statistics 
        including each team's average kill/death ratio.

        Required Stats:
        Declare winning team
        Show both teams average kill/death ratio.
        Show surviving heroes.
        '''
```

Implement the above methods. Use your favorite loops with the `input()` function to build teams based on user input. 

Test your functions by either creating a new test file and using pytest, or by calling your methods this way: 

```python
if __name__ == "__main__":
    arena = Arena()
    arena.build_team_one()
    arena.build_team_two()
    arena.team_battle()
    arena.show_stats()
``` 

## Creating a Game Loop
Our program right now has the parts and pieces to run once before it exits. This is fine for one off scripts that can run without user input, but games should be interactive. Our interactivity will come from a useful programming pattern called the game loop.

A typical game loop will do a few things over and over again:

* check for user input
* check length of time between loops
* update the game state
* render output to screen

Our terminal game isn't really your typical game so our game loop will be a bit different. 

Since our game doesn't rely on quickly rendering complicated scenes to the screen we're not so concerned with framerate and by extension the time between calling our render function. Our program instead will pause for user input and take actions depending on that. 

You can create a simple game loop in your `superheroes.py` file this way:

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
This code snippet will get you started with your game loop. Here on every loop we battle our teams, show the battle outcome, and check whether we want to loop again.

This is just the start of what you can make. Add to your game with these stretch challenges. 

## Stretch Challenges 
* Add a command line interface that allows for recreating or editing  of teams.
* Allow use of only "authorized" abilites, weapons, and armor controlled by the Arena.
* Add tests that cover more edge cases.
* Change the way health is dealt out across the team. i.e. create heroes that may take damage first or may take more of the team's damage.
* Write additional classes that implement different ways to attack or defend -- i.e. create a relic class that only defends against abilities.
* Develop a way to steal weapons and abilities from the opposing team.
* Add rewards for team success such as weapon drops.

