file = open("student.txt", "r")

data = file.read()

words = data.split()

print("Total number of words:", len(words))

file.close()