# Super Hero Fight Book
class Hero:
    d = 0
    def add_to_class(self):
        Hero.d += 1
    
    def view(self):
        print(self.d)
    
    def add_to_instance(self):
        self.d += 1


print("instantiating victor")
victor = Hero()
print("victor id")
victor.view()
print("Add to victor id")
victor.add_to_class()
print("instantiating hugo")
hugo = Hero()
print("Hugo's id")
hugo.view()
print("Add to victor instance")
victor.add_to_instance()
print("Hugo's id")
hugo.view()
print("Victor's id")
victor.view()
print("Add to hugo's instance")
hugo.add_to_instance()
print("Victor's id")
victor.view()
print("Hugo's Id")
hugo.view()
print("Instantiating batman")
batman = Hero()
print("Batman's id")
batman.view()
print("Add to victor instance")
victor.add_to_class()
print("instantiate hello kitty")
helloKitty = Hero()
print("Kitty's Id")
helloKitty.view()
print("Victor's ID")
victor.view()