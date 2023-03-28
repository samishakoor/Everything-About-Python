class Animals:
    animalType = "Mammal"

class Pets(Animals):
    color = "White"

class Dog(Animals):
    @staticmethod
    def bark():
        print("Bow bow!")

d  = Dog()
d.bark()