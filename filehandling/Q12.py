file = open("student.txt", "r")

data = file.read()
words = data.lower().split()

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("Word occurrences:")

for word, count in word_count.items():
    print(word, ":", count)

file.close()