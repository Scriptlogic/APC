file = open("student.txt", "r")

data = file.read()

file.close()

new_file = open("uppercase.txt", "w")

new_file.write(data.upper())

new_file.close()

print("Uppercase file created successfully.")