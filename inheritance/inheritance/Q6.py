class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def display_account(self):
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)


class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return self.balance * self.interest_rate / 100

    def display_savings(self):
        self.display_account()
        print("Interest Rate:", self.interest_rate)
        print("Interest:", self.calculate_interest())


class PremiumSavingsAccount(SavingsAccount):
    def __init__(self, account_number, balance, interest_rate, benefits):
        super().__init__(account_number, balance, interest_rate)
        self.benefits = benefits

    def display_details(self):
        self.display_savings()
        print("Additional Benefits:", self.benefits)


p = PremiumSavingsAccount(12345, 50000, 6, "Free ATM Transactions")

p.display_details()