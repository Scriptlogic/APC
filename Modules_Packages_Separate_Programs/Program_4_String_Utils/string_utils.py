# Program 4: String Utility Module

def count_vowels(text):
    return sum(1 for ch in text.lower() if ch in "aeiou")

def reverse_string(text):
    return text[::-1]

def check_palindrome(text):
    return text == text[::-1]

def count_words(text):
    return len(text.split())

def remove_spaces(text):
    return text.replace(" ", "")
