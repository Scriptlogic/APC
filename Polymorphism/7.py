class BankAccount:
    def calculate_interest(self):
        print("Calculating interest")


class SavingsAccount(BankAccount):
    def calculate_interest(self):
        amount = 10000
        rate = 4
        interest = amount * rate / 100
        print("Savings Account Interest =", interest)


class CurrentAccount(BankAccount):
    def calculate_interest(self):
        amount = 10000
        rate = 2
        interest = amount * rate / 100
        print("Current Account Interest =", interest)


class FixedDepositAccount(BankAccount):
    def calculate_interest(self):
        amount = 10000
        rate = 7
        interest = amount * rate / 100
        print("Fixed Deposit Interest =", interest)


b = SavingsAccount()
b.calculate_interest()

b = CurrentAccount()
b.calculate_interest()

b = FixedDepositAccount()
b.calculate_interest()