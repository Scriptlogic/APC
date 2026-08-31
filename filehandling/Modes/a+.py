file = open("file.txt", "a+")

file.write("\nWelcome")

file.seek(0)

print(file.read())

file.close()