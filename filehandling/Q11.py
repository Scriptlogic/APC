file = open("student.txt", "r")

data = file.read()
words = data.split()

longest = max(words, key=len)

print("Longest word:", longest)

file.close()