sentence = input("Enter a sentence: ")

word_count = 0
in_word = False

for char in sentence:
    if char != " " and not in_word:
        in_word = True
        word_count += 1
    elif char == " ":
        in_word = False

print(f"Total number of words: {word_count}")