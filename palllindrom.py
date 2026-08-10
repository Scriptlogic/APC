text = input("Enter a string: ")
clean_text = text.lower()

if clean_text == clean_text[::-1]:
    print("It is a palindrome!")
else:
    print("It is not a palindrome.")