# Program 9: Main Program for Banking Package

from banking.account import create_account, get_balance
from banking.transaction import deposit, withdraw
from banking.loan import calculate_loan_interest

create_account(5000)

print("Initial Balance =", get_balance())
print("After Deposit =", deposit(2000))
print("After Withdrawal =", withdraw(1000))
print("Loan Interest =", calculate_loan_interest(100000, 8, 2))
