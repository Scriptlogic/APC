text = input("Enter a string: ")
old_char = input("Enter character to replace: ")
new_char = input("Enter replacement character: ")

result = ""

for char in text:
    if char == old_char:
        result += new_char
    else:
        result += char

print(f"Modified string: {result}")