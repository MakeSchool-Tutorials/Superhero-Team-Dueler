# Superhero-Team-Dueler
Ever wondered which of your favorite super heroes would win in a fight? Team them up for battle in this introduction to object oriented programming.

## Notes

### Overall 

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


