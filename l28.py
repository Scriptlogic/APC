scores = [45, 102, 78, 12, 54, 89, 115, 0, 67, 92]

highest_score = max(scores)
lowest_score = min(scores)
total_runs = sum(scores)
avg_runs = total_runs / len(scores)

centuries = sum(1 for score in scores if score >= 100)
half_centuries = sum(1 for score in scores if 50 <= score <= 99)

print("Highest Score:", highest_score)
print("Lowest Score:", lowest_score)
print("Total Runs:", total_runs)
print("Average Runs:", round(avg_runs, 2))
print("Centuries (>=100):", centuries)
print("Half-Centuries (50-99):", half_centuries)