# Атрибуты класса общие для всех объектов; атрибуты через self - только у конкретного объекта
class Visitor:
    # organization, created_count - атрибуты класса: значения одни и те же для всех Visitor
    organization = "Курсы"
    created_count = 0

    def __init__(self, name):
        if not Visitor.validate_name(name):
            raise ValueError("Имя должно быть длиннее 1 символа")
        self.name = name
        self.count = 0
        self.visitor_type = "ordinary"
        Visitor.created_count += 1  # обращение через имя класса - меняем общий счётчик, а не атрибут объекта

    def introduce(self):
        print(Visitor.get_organization())
        print(f"Меня зовут {self.name}")

    # cls - сам класс, через который вызвали метод; self здесь не нужен
    @classmethod
    def get_organization(cls):
        return cls.organization

    @classmethod
    def create_vip_visitor(cls, name):
        # альтернативный конструктор
        # cls(...) создаёт объект того класса, через который вызвали метод (сработает и для наследников)
        new_visitor = cls(name)
        new_visitor.visitor_type = "vip"
        return new_visitor

    # @staticmethod - метод без привязки к объекту и классу: не получает self/cls,
    # это обычная функция, которую держат в классе по смыслу
    @staticmethod
    def validate_name(name):
        no_space_name = name.strip()
        if len(no_space_name) < 2:
            return False
        return True


print(Visitor.organization)
print(Visitor.created_count)
# меняем атрибут класса - изменение видно всем объектам
Visitor.organization = "Курсы Geeks"
visitor1 = Visitor("Igor")

try:
    visitor2 = Visitor("    I    ")
    print(visitor2.introduce())
except ValueError as e:
    print(e)

print(visitor1.visitor_type)
print(Visitor.created_count)
print(Visitor.get_organization())
vip_visitor = Visitor.create_vip_visitor("Kurmanbek")
print(vip_visitor.visitor_type)