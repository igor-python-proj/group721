class Car:
    # конструктор, инициализатор - initializer
    def __init__(self, marka, color):
        self.marka = marka
        self.color = color

    def change_color(self, new_color):
        self.color = new_color

    def drive_to(self, destination):
        self.change_color("black")
        print(f"Машина марки {self.marka} едет в {destination}")

car_1 = Car("BMW", "black")
car_2 = Car("Mercedes", "blue")
print(car_1, car_2)
print(f"Car 1: {car_1.marka}, {car_1.color}")
print(f"Car 2: {car_2.marka}, {car_2.color}")
car_2.drive_to("Каракол")
print(f"Car 2: {car_2.marka}, {car_2.color}")
car_2.change_color("silver")
print(f"Car 2: {car_2.marka}, {car_2.color}")
print(type("gfdgfdgdf"), type(12312))
print(type(car_1))
car_1.marka = "Mercedes"
print(f"Car 1: {car_1.marka}, {car_1.color}")
car_1.horse_power = 100
print(f"Car 1: {car_1.horse_power}, {car_1.marka}")
# print(f"Car 2: {car_2.marka}, {car_2.horse_power}")

# создать класс для игрового персонажа\
# с любыми свойствами(сила, здоровье, имя, роль и тд)