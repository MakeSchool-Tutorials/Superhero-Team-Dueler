class Dog:
    def __init__(self, name):
        self.name = name
        self._greeting = "Woof!"

    def bark(self):
        print(self._greeting)

    def get_greeting(self):
        return self._greeting
    
    def set_greeting(self, new_greeting):
        self._greeting = new_greeting
         
my_first_dog = Dog("Annie")
my_second_dog = Dog("Wyatt")

print(my_first_dog.name)
print(my_second_dog.name)

my_first_dog.set_greeting("Yap! Yap!")

my_first_dog.bark()
my_second_dog.bark()