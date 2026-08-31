file = open("transactions.txt", "r")

total_deposits = 0
total_withdrawals = 0
largest_transaction = 0

for line in file:
    transaction, amount = line.strip().split(",")

    amount = float(amount)

    if transaction == "deposit":
        total_deposits += amount

    elif transaction == "withdrawal":
        total_withdrawals += amount

    if amount > largest_transaction:
        largest_transaction = amount

file.close()

final_balance = total_deposits - total_withdrawals

print("Total Deposits:", total_deposits)
print("Total Withdrawals:", total_withdrawals)
print("Final Balance:", final_balance)
print("Largest Transaction:", largest_transaction)