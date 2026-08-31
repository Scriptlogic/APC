file = open("attendance.txt", "r")

print("Students with attendance below 75%:")

for line in file:
    roll, name, present, total = line.strip().split(",")

    present = int(present)
    total = int(total)

    percentage = (present / total) * 100

    print(name, "-", percentage, "%")

    if percentage < 75:
        print("Below 75%:", name)

file.close()