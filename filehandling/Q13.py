word = input("Enter word to search: ")

file = open("student.txt", "r")

count = 0
line_numbers = []

for line_number, line in enumerate(file, start=1):
    words = line.lower().split()

    if word.lower() in words:
        count += words.count(word.lower())
        line_numbers.append(line_number)

file.close()

print("Number of occurrences:", count)
print("Line numbers:", line_numbers)