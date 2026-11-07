# Атрибуты класса общие для всех объектов; атрибуты через self - только у конкретного объекта
class Visitor:
    # organization, created_count - атрибуты класса: значения одни и те же для всех Visitor
    organization = "Курсы"
    created_count = 0

    def __init__(self, name):
        self.name = name
        self.count = 0
        self.visitor_type = "ordinary"
        Visitor.created_count += 1  # обращение через имя класса - меняем общий счётчик, а не атрибут объекта

    def introduce(self):
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

print(Visitor.organization)
print(Visitor.created_count)
# меняем атрибут класса - изменение видно всем объектам
Visitor.organization = "Курсы Geeks"
visitor1 = Visitor("Igor")
print(visitor1.visitor_type)
print(Visitor.created_count)
print(Visitor.get_organization())
vip_visitor = Visitor.create_vip_visitor("Kurmanbek")
print(vip_visitor.visitor_type)