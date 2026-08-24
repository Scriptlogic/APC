words = ["apple", "banana", "cat", "computer", "dog", "python"]

result = list(filter(lambda x: len(x) > 5, words))

print("Words =", result)