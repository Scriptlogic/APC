file = open("file.txt", "wb+")

file.write(b"\n Happy")

file.seek(0)

print(file.read())