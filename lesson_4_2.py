class Visitor:
    organization = "Курсы"
    created_count = 0

    def __init__(self, name):
        self.name = name
        self.count = 0
        self.visitor_type = "ordinary"
        Visitor.created_count += 1

    def introduce(self):
        print(f"Меня зовут {self.name}")

    @classmethod
    def get_organization(cls):
        return cls.organization

    @classmethod
    def create_vip_visitor(cls, name):
        # альтернативный конструктор
        new_visitor = cls(name)
        new_visitor.visitor_type = "vip"
        return new_visitor

print(Visitor.organization)
print(Visitor.created_count)
Visitor.organization = "Курсы Geeks"
visitor1 = Visitor("Igor")
print(visitor1.visitor_type)
print(Visitor.created_count)
print(Visitor.get_organization())
vip_visitor = Visitor.create_vip_visitor("Kurmanbek")
print(vip_visitor.visitor_type)