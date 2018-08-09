class Animal:
    def __init__(self, name, sleep_duration, sleep_time):
        self.name = name
        self.sleep_duration = sleep_duration
        self.sleep_time = sleep_time

    def sleep(self):
        print(
            "{} sleeps for {} hours {}".format(
                self.name,
                self.sleep_duration,
                self.sleep_time))


class Dog(Animal):
    def __init__(self, name, sleep_duration, sleep_time):
        Animal.__init__(self, name, sleep_duration, sleep_time)

    def bark(self):
        print("Woof! Woof!")


my_dog = Dog("Sophie", 12, "at night")
my_dog.sleep()
my_dog.bark()
