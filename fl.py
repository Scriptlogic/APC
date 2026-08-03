text = input("Enter a string: ")

if text:
    first_char = text[0]
    last_char = text[len(text) - 1]
    
    print(f"First character: {first_char}")
    print(f"Last character: {last_char}")
else:
    print("The string is empty!")