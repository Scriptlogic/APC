# Program 9: Transaction Module

import banking.account as account

def deposit(amount):
    account.balance += amount
    return account.balance

def withdraw(amount):
    if amount <= account.balance:
        account.balance -= amount
        return account.balance
    return "Insufficient Balance"
