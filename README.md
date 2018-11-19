# Superhero-Team-Dueler
Ever wondered which of your favorite super heroes would win in a fight? Team them up for battle in this introduction to object oriented programming.

## Notes

### Overall 

Too wordy, cutting extraneous words might make it more readable. For example: 

> Here we define what we want our Hero class to look like. Each hero should have a name and should be able to have several different abilities. Also a hero will need other attributes such as starting and current health. We'll need to set these at some starting value when we create each Hero in memory.

vs 

> Here you define what the Hero class will look like. Each hero should have a name and several different abilities. A hero also needs other attributes such as starting and current health. You need to set these at some starting value when each Hero is created in memory.

Might be good to be more specific. 

> Here you define what the Hero class will look like. Each hero should have a name and several different abilities. A hero also needs other **properties** such as starting and current health. You need to define these in the **constructor** function of the class.

The voice is written mostly as "Our". For example 

> Our dog here is simply an instance of our Animal...

and 

> We don't want to put a bark method in Animal...

Might better as: 

> Your dog here is simply an instance of our Animal...

and 

> You don't want to put a bark method in Animal...

Some of the example don't state a clear objective. I don't feel it will be completely clear to a student what 
they supposed to accomplish at each step. 

Good to define terms early on an use them consistently throughout the tutorial. 


## Class Variables 

The tutorial mentions class variables in an obtuse way. It also shows an example of 
class variables and self to reference the variable rather than the class name: 

```
class Dog: 
  greeting = "Woof"
  ...
  print(self.greeting) # Get class variable with self
  ...
```

This seems to add confusion. Might be better to use this convention. 

```
class Dog: 
  greeting = "Woof"
  ...
  print(Dog.greeting) # get class variable via class name
  ...
```

## Needs a story

Adding some background story would help. Currently the tutorial says things like: 

> Each hero should have a name and should be able to have several different abilities. 

Inbstead it might be more engaging to inlcude a narrative:

> Superman uses his super strength to save the world. You'll need to define this ability! 


