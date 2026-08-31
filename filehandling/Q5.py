file = open("student.txt", "r")

lines = file.readlines()

print("Total number of lines:", len(lines))

file.close()