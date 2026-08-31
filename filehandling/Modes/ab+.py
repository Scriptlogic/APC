file = open("file.bin", "ab+")

file.write(b" binary data")

file.seek(0)

data = file.read()
print(data)

file.close()