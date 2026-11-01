import matplotlib.pyplot as plt

marks = [45, 50, 55, 60, 60, 65, 70, 70,
         75, 80, 85, 90, 90, 95]

plt.hist(marks, bins=5, edgecolor="black")
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()