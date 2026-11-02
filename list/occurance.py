sentence = input("Enter a sentence: ")
target_word = input("Enter the word to count: ")

# Convert to lowercase for case-insensitive matching
words = sentence.lower().split()
count = words.count(target_word.lower())

print(f"The word '{target_word}' appears {count} time(s).")