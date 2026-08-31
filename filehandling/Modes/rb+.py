file = open("file.bin", "rb+")

data = file.read()
print(data)

file.write(b" New Data")

file.close()