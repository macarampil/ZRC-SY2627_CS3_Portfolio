class Animal:
    def __init__(self, name):
        self.__name = name

    def eat(self):
        print(f"{self.__name} eats.")

    def make_sound(self):
        print(f"{self.__name} makes a sound.")


class Lion(Animal):
    def make_sound(self):
        print(f"{self._Animal__name} roars loudly!")

    def eat(self):
        print(f"{self._Animal__name} eats fresh meat.")


class Elephant(Animal):
    def make_sound(self):
        print(f"{self._Animal__name} trumpets!")

    def eat(self):
        print(f"{self._Animal__name} eats grass and fruits.")


class Monkey(Animal):
    def make_sound(self):
        print(f"{self._Animal__name} chatters!")

    def eat(self):
        print(f"{self._Animal__name} eats bananas.")


lion1 = Lion("Simba")
elephant1 = Elephant("Dumbo")
monkey1 = Monkey("George")

animals = [lion1, elephant1, monkey1]

for animal in animals:
    animal.make_sound()
    animal.eat()
    print("--------------")