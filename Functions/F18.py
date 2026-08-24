def calculate_grade(m1, m2, m3, m4, m5):
    percentage = (m1 + m2 + m3 + m4 + m5) / 5

    if percentage >= 90:
        grade = "A"
    elif percentage >= 75:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    return percentage, grade

m1 = float(input("Enter marks 1: "))
m2 = float(input("Enter marks 2: "))
m3 = float(input("Enter marks 3: "))
m4 = float(input("Enter marks 4: "))
m5 = float(input("Enter marks 5: "))

percentage, grade = calculate_grade(m1, m2, m3, m4, m5)

print("Percentage =", percentage)
print("Grade =", grade)