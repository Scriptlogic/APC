# Program 2: Student Result Module

def total_marks(marks):
    return sum(marks)

def percentage(marks):
    return sum(marks) / len(marks)

def grade(percent):
    if percent >= 75:
        return "A"
    elif percent >= 60:
        return "B"
    elif percent >= 50:
        return "C"
    elif percent >= 40:
        return "D"
    else:
        return "F"
