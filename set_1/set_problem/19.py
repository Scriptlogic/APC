# 19. Compare morning and afternoon students

morning = {"Amit", "Sneha", "Rahul", "Priya"}
afternoon = {"Rahul", "Priya", "Riya", "Karan"}

print("Present in both sessions:", morning & afternoon)

print("Only in morning:", morning - afternoon)

print("Only in afternoon:", afternoon - morning)

print("Present in at least one session:", morning | afternoon)