from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):
    def __init__(self, name):
        self.name = name
        self.species = "Animal"

    def __repr__(self):
        return f"<{self.species} name: {self.name} color: {self.color} sounds: {self.sound()}>"

    def walk(self):
        print("animal is walking")

    @abstractmethod  # this method makes it abstract class
    def sound(self):
        pass


class Dog(Animal):
    def __init__(self, name, color):
        super(Dog, self).__init__(name)
        self.color = color
        self.species = "DOG"

    def sound(self):
        return "Bark"


class Cat(Animal):
    def __init__(self, name, color):
        super(Cat, self).__init__(name)
        self.color = color
        self.species = "CAT"

    def sound(self):
        return "Meow"


animal = [Dog('Tommy', 'brown'), Cat('Tom', 'black')]
for a in animal:
    print(a)
