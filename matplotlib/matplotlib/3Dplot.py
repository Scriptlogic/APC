
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
z = [5, 10, 15, 20, 25]

ax.plot(x, y, z, marker="o")

ax.set_title("3D Line Plot")
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")

plt.show()
