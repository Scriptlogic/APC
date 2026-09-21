from abc import ABC, abstractmethod

class BankAccount(ABC):

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass


class SavingsAccount(BankAccount):
    def __init__(self):
        self.balance = 10000

    def deposit(self, amount):
        self.balance += amount
        print("Savings Deposit:", amount)

    def withdraw(self, amount):
        self.balance -= amount
        print("Savings Withdrawal:", amount)

    def show_balance(self):
        print("Balance =", self.balance)


class CurrentAccount(BankAccount):
    def __init__(self):
        self.balance = 20000

    def deposit(self, amount):
        self.balance += amount
        print("Current Deposit:", amount)

    def withdraw(self, amount):
        self.balance -= amount
        print("Current Withdrawal:", amount)

    def show_balance(self):
        print("Balance =", self.balance)


s = SavingsAccount()
s.deposit(2000)
s.withdraw(1000)
s.show_balance()

c = CurrentAccount()
c.deposit(5000)
c.withdraw(2000)
c.show_balance()