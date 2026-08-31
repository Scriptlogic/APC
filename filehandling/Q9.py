file = open("student.txt", "r")

data = file.read()

vowels = 0
consonants = 0

for ch in data:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("Total vowels:", vowels)
print("Total consonants:", consonants)

file.close()