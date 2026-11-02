class Notification:
    def send(self):
        print("Sending notification")


class EmailNotification(Notification):
    def send(self):
        print("Sending notification through Email")


class SMSNotification(Notification):
    def send(self):
        print("Sending notification through SMS")


class PushNotification(Notification):
    def send(self):
        print("Sending Push Notification")


n = EmailNotification()
n.send()

n = SMSNotification()
n.send()

n = PushNotification()
n.send()