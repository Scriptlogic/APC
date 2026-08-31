file = open("file.bin", "wb+")

file.write(b"Hello Python")

file.seek(0)

data = file.read()
print(data)

file.close()