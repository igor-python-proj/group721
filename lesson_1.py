# Car - класс, "шаблон" для объектов: описывает данные (атрибуты)
# и поведение (методы) всех машин
class Car:
    # __init__ - конструктор (инициализатор): вызывается автоматически
    # при каждом создании объекта и задаёт начальные значения атрибутов
    def __init__(self, marka, color):
        # self - ссылка на конкретный объект, для которого вызван метод;
        # self.marka, self.color - атрибуты объекта
        self.marka = marka
        self.color = color

    def change_color(self, new_color):
        self.color = new_color

    def drive_to(self, destination):
        # методы могут вызывать другие методы этого же класса через self
        self.change_color("black")
        print(f"Машина марки {self.marka} едет в {destination}")

# создаём два независимых объекта одного класса;
# __init__ вызывается для каждого со своими аргументами
car_1 = Car("BMW", "black")
car_2 = Car("Mercedes", "blue")
# без специального метода Python печатает служебное представление объекта
print(car_1, car_2)
print(f"Car 1: {car_1.marka}, {car_1.color}")
print(f"Car 2: {car_2.marka}, {car_2.color}")
# вызов метода: объект.имя_метода(аргументы); self указывать не нужно - Python передаст его сам
car_2.drive_to("Каракол")
print(f"Car 2: {car_2.marka}, {car_2.color}")
car_2.change_color("silver")
print(f"Car 2: {car_2.marka}, {car_2.color}")
print(type("gfdgfdgdf"), type(12312))
# type() показывает класс объекта - для car_1 это Car
print(type(car_1))
car_1.marka = "Mercedes"
print(f"Car 1: {car_1.marka}, {car_1.color}")
# динамический атрибут: Python позволяет добавлять свойства объекту на лету,
# но это плохая практика - атрибут появится только у car_1 и приведёт к ошибкам
car_1.horse_power = 100
print(f"Car 1: {car_1.horse_power}, {car_1.marka}")
# print(f"Car 2: {car_2.marka}, {car_2.horse_power}")

# создать класс для игрового персонажа\
# с любыми свойствами(сила, здоровье, имя, роль и тд)