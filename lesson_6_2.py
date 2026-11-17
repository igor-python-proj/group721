# Множественное наследование, MRO
# MRO (method resolution order) - порядок, в котором Python ищет методы в цепочке родителей.
# super() идёт по этой цепочке, а не просто к прямому родителю.
class Animal:
    # Общая реализация для всей цепочки - сработает последней.
    def move(self):
        print("Животное двигается")

class Flying(Animal):
    # Переопределяем move(): делаем своё и через super() передаём управление дальше.
    def move(self):
        print("умею летать")
        super().move()

class Swimming(Animal):
    # super() смотрит на MRO объекта: у Duck после Swimming идёт Flying, поэтому вызовется его move().
    def move(self):
        print("умею плавать")
        super().move()

# Порядок родителей важен: он задаёт MRO - Duck -> Swimming -> Flying -> Animal.
class Duck(Swimming, Flying):
    def move(self):
        print("Утка плавает и летает")
        super().move()  # запускает остальные move() по цепочке

donald = Duck()
donald.move()  # сработают все четыре реализации move()
# MRO - method resolution order - порядок поиска метода
print(Duck.mro())  # mro() возвращает список классов
print(Duck.__mro__)  # __mro__ хранит тот же порядок в виде кортежа
fish = Swimming()
fish.move()  # цепочка короче: Swimming -> Animal
print(Swimming.mro())
