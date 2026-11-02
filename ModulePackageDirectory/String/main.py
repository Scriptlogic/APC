from string import *

text = input("Enter a string: ")

print("Vowels:", count_vowels(text))
print("Reverse:", reverse_string(text))
print("Palindrome:", is_palindrome(text))
print("Words:", count_words(text))
print("Without spaces:", remove_spaces(text))