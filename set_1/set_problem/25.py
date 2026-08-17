# 25. Compare friends of two users

user1 = {"Amit", "Rahul", "Sneha", "Priya", "Karan"}
user2 = {"Rahul", "Priya", "Riya", "Karan", "Neha"}

print("Mutual friends:", user1 & user2)

print("Friends unique to User 1:", user1 - user2)

print("Friends unique to User 2:", user2 - user1)

print("Total unique friends:", len(user1 | user2))