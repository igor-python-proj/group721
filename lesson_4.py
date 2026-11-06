from abc import ABC, abstractmethod

# Абстракция
class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass

# конкретный класс
class EmailNotification(Notification):
    # реализация абстрактного метода
    def send(self, message):
        print(f"уведомление по почте: {message}")

class SMSNotification(Notification):
    pass

# simple_notification = Notification()
email_not = EmailNotification()
email_not.send("привет мир")
try:
    sms_not = SMSNotification()
except TypeError as e:
    print(e)