# Program 10: Frequency Module

def word_frequency(words):
    result = {}
    for word in words:
        result[word] = result.get(word, 0) + 1
    return result
