# Program 10: Main Program for texttools Package

from texttools.cleaning import remove_punctuation, remove_extra_spaces
from texttools.tokenization import tokenize
from texttools.frequency import word_frequency

text = input("Enter text: ")

cleaned = remove_punctuation(text)
cleaned = remove_extra_spaces(cleaned)
tokens = tokenize(cleaned)

print("Cleaned Text =", cleaned)
print("Tokens =", tokens)
print("Word Frequency =", word_frequency(tokens))
