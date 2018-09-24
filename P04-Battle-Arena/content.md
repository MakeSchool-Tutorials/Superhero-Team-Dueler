---
title: Create the Arena
slug: arena
---
## Creating the Battle Arena
Our heroes need a place to fight. This means that we're going to need an object that will manage our game for us. This object will make sure that each team gets a chance to attack the other. These are some methods that need to be completed for a battle to take place.

This `Arena` class will be responsible for making sure that all of our rules are followed in our game. It will be responsible for creating and managing our teams and regulating how they fight.

```python
class Arena:
    def __init__(self):
        """
        Declare variables
        """
        self.team_one = None
        self.team_two = None

    def build_team_one(self):
        """
        This method should allow a user to build team one.
        """

    def build_team_two(self):
        """
        This method should allow user to build team two.
        """
    
    def team_battle(self):
        """
        This method should continue to battle teams until 
        one or both teams are dead.
        """

    def show_stats(self):
        """
        This method should print out the battle statistics 
        including each heroes kill/death ratio.
        """
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
* Change the way health is dealt out across the team. i.e. create heroes that may take damage first or may take more of the teams damage.
* Write additional classes that implement different ways to attack or defend -- i.e. create a relic class that only defends against abilities.
* Develop a way to steal weapons and abilities from the opposing team.
* Add rewards for team success such as weapon drops.

