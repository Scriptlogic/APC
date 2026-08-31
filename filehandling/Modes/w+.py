file = open("file.txt", "w+")
file.write("\nhappy")
file.seek(0)  
print(file.read())

file.close()