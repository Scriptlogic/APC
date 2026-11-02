text = input("Enter a string: ")

seen = set()
result = []

for char in text:
    if char not in seen:
        seen.add(char)
        result.append(char)

# Join the list back into a single string
final_string = "".join(result)

print(f"Result: {final_string}")