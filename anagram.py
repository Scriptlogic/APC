str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

# Clean strings: convert to lowercase and remove spaces
clean1 = str1.lower().replace(" ", "")
clean2 = str2.lower().replace(" ", "")

# Compare sorted character lists
if sorted(clean1) == sorted(clean2):
    print("The strings are anagrams!")
else:
    print("The strings are NOT anagrams.")