import matplotlib.pyplot as plt

subjects = ["Python", "Java", "C++", "HTML"]
marks = [80, 70, 90, 60]

plt.bar(subjects, marks, color="skyblue")
plt.title("Student Marks")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()