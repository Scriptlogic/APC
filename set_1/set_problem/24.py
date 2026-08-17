# 24. Compare visitors from two days

day1 = {101, 102, 103, 104, 105}
day2 = {103, 104, 105, 106, 107}

print("Unique visitors across both days:", day1 | day2)

print("Returning visitors:", day1 & day2)

print("Visitors only on first day:", day1 - day2)

print("Visitors only on second day:", day2 - day1)