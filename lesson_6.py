# Множественное наследование - класс получает методы сразу нескольких родителей.
# Если метод есть у нескольких родителей, Python ищет его по MRO - порядку поиска методов.
class Flying:
    def fly(self):
        print("умею летать")

class Swimming:
    def swim(self):
        print("умею плавать")

# Duck наследует от двух классов сразу и получает оба метода - fly() и swim().
class Duck(Flying, Swimming):
    pass

# Миксин - класс-добавка: даёт наследникам готовый метод, но сам по себе не работает.
# show_info() рассчитывает, что наследник определит get_info().
class InfoMixin:
    def show_info(self):
        print(self.get_info())

# NamedObject хранит общее для разных классов поле - имя.
class NamedObject:
    def __init__(self, name):
        self.name = name

# Product получает name от NamedObject и show_info() от InfoMixin.
# Миксин принято указывать первым, затем основной родитель.
class Product(InfoMixin, NamedObject):
    def get_info(self):
        return f"Товар: {self.name}"

# Room использует тот же show_info(), но сам решает, что вернёт get_info().
class Room(InfoMixin, NamedObject):
    def get_info(self):
        return f"Помещение: {self.name}"


# SOLID = SingleResponsibilityPrinciple + ...
# show_info() общий, а get_info() берётся из конкретного класса:
# один и тот же вызов ведёт себя по-разному - это полиморфизм.
Product("кроссы").show_info()
Room("аудитория 2-4").show_info()
donald = Duck()
donald.fly()  # метод унаследован от Flying
donald.swim()  # метод унаследован от Swimming
