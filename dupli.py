text = input("Enter a string: ")

seen = set()
duplicates = set()

for char in text:
    if char in seen:
        duplicates.add(char)
    else:
        seen.add(char)

if duplicates:
    print("Duplicate characters found:", ", ".join(repr(c) for c in duplicates))
else:
    print("No duplicate characters found.")
    