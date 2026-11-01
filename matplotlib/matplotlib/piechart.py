import matplotlib.pyplot as plt

labels = ["Python", "Java", "C++", "HTML"]
values = [40, 25, 20, 15]

plt.pie(values, labels=labels, autopct="%1.1f%%",
        startangle=90)
plt.title("Programming Language Preferences")
plt.show()