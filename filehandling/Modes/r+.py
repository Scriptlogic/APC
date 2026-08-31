file = open("file.txt", "r+")

print(file.read())

file.write("\nhello")

file.close()