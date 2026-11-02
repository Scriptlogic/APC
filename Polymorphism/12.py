class Payment:
    def make_payment(self):
        print("Making payment")


class UPIPayment(Payment):
    def make_payment(self):
        print("Payment made using UPI")


class CardPayment(Payment):
    def make_payment(self):
        print("Payment made using Credit/Debit Card")


class WalletPayment(Payment):
    def make_payment(self):
        print("Payment made using Wallet")


def process_payment(payment):
    payment.make_payment()


p1 = UPIPayment()
process_payment(p1)

p2 = CardPayment()
process_payment(p2)

p3 = WalletPayment()
process_payment(p3)