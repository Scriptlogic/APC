old_word = input("Enter word to replace: ")
new_word = input("Enter new word: ")

file = open("student.txt", "r")

data = file.read()

file.close()

data = data.replace(old_word, new_word)

file = open("student.txt", "w")

file.write(data)

file.close()

print("Word replaced successfully.")