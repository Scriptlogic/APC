
text = input("Enter a string: ")
vowels = 0
consonants = 0
digits = 0
spaces = 0
special_chars = 0
vowel_set = "aeiouAEIOU"
for char in text:
    if char in vowel_set:
        vowels += 1
    elif char.isalpha():  
        consonants += 1
    elif char.isdigit():  
        digits += 1
    elif char.isspace():  
        spaces += 1
    else: 
        special_chars += 1
print("\n--- Character Breakdown ---")
print(f"Vowels:             {vowels}")
print(f"Consonants:         {consonants}")
print(f"Digits:             {digits}")
print(f"Spaces:             {spaces}")
print(f"Special Characters: {special_chars}")