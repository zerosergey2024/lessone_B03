class Animal():
    def make_saund(self):
        pass
class Bird(Animal):
    def __init__ (self, sparrowe):
        self.sparrow = sparrowe
    def make_saund(selfself):
        print("song")

class Mammal(Animal):
    def __init__ (self, cow):
        self.cow = cow
    def make_saund(self):
        print("muu")

class Reptile(Animal):
    def __init__ (self, crocodile):
        self.crocodile = crocodile
    def make_saund(self):
        print("roar")

    sparrow = Bird("sparrow")
    cow = Mammal("cow")
    crocodile = Reptile("crocodile")

    animals = [sparrow, cow, crocodile]

    for animal in animals:
        animal.make_saund()

