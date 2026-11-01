import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [5, 10, 15, 20, 25]

plt.plot(x, y, marker="o", color="red",
         linestyle="--")
plt.title("Line Plot with Markers")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.grid(True)
plt.show()