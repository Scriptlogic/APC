def count_vowels(s):
    count = 0

    for ch in s:
        if ch in "aeiouAEIOU":
            count = count + 1

    return count

s = input("Enter a string: ")

print("Number of vowels =", count_vowels(s))