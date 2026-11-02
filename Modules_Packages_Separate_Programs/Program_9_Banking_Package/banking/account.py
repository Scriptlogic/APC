# Program 9: Account Module

balance = 0

def create_account(initial_balance=0):
    global balance
    balance = initial_balance
    return balance

def get_balance():
    return balance
