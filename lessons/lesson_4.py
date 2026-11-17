from abc import ABC, abstractmethod

# Абстракция - выносим общее действие (send) в интерфейс класса,
# а детали реализации оставляем конкретным классам
# Notification(ABC) - абстрактный класс: это общий интерфейс, свои объекты создавать нельзя
class Notification(ABC):
    # @abstractmethod - метод без реализации: наследник обязан его реализовать,
    # иначе его класс нельзя создать
    @abstractmethod
    def send(self, message):
        pass

# конкретный класс
class EmailNotification(Notification):
    # реализация абстрактного метода
    def send(self, message):
        print(f"уведомление по почте: {message}")

# SMSNotification не реализовал send - поэтому остаётся абстрактным
class SMSNotification(Notification):
    pass

# абстрактный класс тоже нельзя создать напрямую
# simple_notification = Notification()
email_not = EmailNotification()
email_not.send("привет мир")
# при создании SMSNotification Python находит нереализованный send и вызывает TypeError
try:
    sms_not = SMSNotification()
except TypeError as e:
    print(e)