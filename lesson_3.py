# Инкапсуляция - храним важные данные внутри класса
# и изменяем их только через методы с проверками
class BankAccount:
    def __init__(self, owner, balance, code):
        # одно подчёркивание - protected: по договорённости снаружи
        # напрямую не трогают, но технически можно
        self._owner = owner
        # два подчёркивания - private: Python скрывает имя атрибута внутри класса,
        # поэтому снаружи к нему не обращаются напрямую
        self.__balance = balance
        self.__code = code

    # @property превращает метод в геттер-свойство:
    # значение читают как igor_account.code, без скобок
    @property
    def code(self):
        # геттер
        return self.__code

    # @code.setter - сеттер: перехватывает присваивание igor_account.code = "..."
    # и проверяет новое значение перед записью
    @code.setter
    def code(self, new_code):
        # сеттер
        if len(new_code) < 5:
            print("Слишком короткое значение")
            return
        self.__code = new_code

    # геттер - публичный метод для чтения приватного атрибута
    def get_balance(self):
        return self.__balance

    def __balance_positive(self):
        if self.__balance > 0:
            return True
        else:
            return False

    # сеттеры
    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError("Сумма меньше вашего баланса")
        self.__balance -= amount

    def deposit(self, amount):
        self.__balance += amount

igor_account = BankAccount(
    "Igor",
    100_000,
     "qwerty",
)
# igor_account.code = "12345"
# igor_account.owner = "Kurmanbek"
igor_account._owner = "Kurmanbek"  # технически можно, но так нарушается договорённость о protected
print(igor_account._owner)
# print(igor_account.__balance)
# присваивание снаружи НЕ меняет приватный атрибут: сокрытие имени работает
# только внутри класса, поэтому создаётся отдельный обычный атрибут -
# настоящий баланс остаётся прежним
igor_account.__balance = 0
print(igor_account.__balance)
print(igor_account.get_balance())
try:
    igor_account.withdraw(1_000_000)
except ValueError as e:
    print(e)
igor_account.withdraw(1_000)
print(igor_account.get_balance())
print(igor_account.code)
igor_account.code = "1234"
print(igor_account.code)
# так писать код не стоит, в образовательных целях
# name mangling
print(igor_account._BankAccount__balance)
print(igor_account._BankAccount__code)
