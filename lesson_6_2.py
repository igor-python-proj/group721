# Множественное наследование, MRO
class Animal:
    def move(self):
        print("Животное двигается")

class Flying(Animal):
    def move(self):
        print("умею летать")
        super().move()

class Swimming(Animal):
    def move(self):
        print("умею плавать")
        super().move()

class Duck(Swimming, Flying):
    def move(self):
        print("Утка плавает и летает")
        super().move()

donald = Duck()
donald.move()
# MRO - method resolution order - порядок поиска метода
print(Duck.mro())
print(Duck.__mro__)
fish = Swimming()
fish.move()
print(Swimming.mro())
