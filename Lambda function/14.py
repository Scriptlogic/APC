words = ["apple", "cat", "banana", "dog", "computer"]

result = sorted(words, key=lambda x: len(x))

print("Sorted words =", result)