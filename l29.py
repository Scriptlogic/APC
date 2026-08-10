# Sample temperature data for 30 days
temperatures = [
    32, 34, 31, 35, 36, 30, 29, 33, 37, 38,
    31, 32, 34, 35, 36, 30, 28, 27, 33, 34,
    35, 39, 40, 36, 32, 31, 30, 29, 33, 35
]

hottest = max(temperatures)
coldest = min(temperatures)
avg_temp = sum(temperatures) / len(temperatures)

days_above_avg = sum(1 for t in temperatures if t > avg_temp)
days_below_avg = sum(1 for t in temperatures if t < avg_temp)

print("Hottest Day Temp:", hottest)
print("Coldest Day Temp:", coldest)
print("Average Temperature:", round(avg_temp, 2))
print("Days Above Average:", days_above_avg)
print("Days Below Average:", days_below_avg)