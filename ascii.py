text = input("Enter a string: ")

print("\nCharacter | ASCII Value")
print("-" * 23)

for char in text:
    print(f"    '{char}'   |    {ord(char)}")