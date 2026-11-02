sentence = input("Enter a sentence: ")

# Split sentence into words
words = sentence.split()

if words:
    # Key=len finds the item with the minimum length
    shortest_word = min(words, key=len)
    print(f"Shortest word: {shortest_word}")
    print(f"Length: {len(shortest_word)}")
else:
    print("No words entered.")