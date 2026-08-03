sentence = input("Enter a sentence: ")

# Split sentence into words
words = sentence.split()

if words:
    # Key=len finds the item with the maximum length
    longest_word = max(words, key=len)
    print(f"Longest word: {longest_word}")
    print(f"Length: {len(longest_word)}")
else:
    print("No words entered.")