def total_marks(marks):
    return sum(marks)

def percentage(marks):
    return total_marks(marks) / len(marks)

def grade(per):
    if per >= 90:
        return "A+"
    elif per >= 80:
        return "A"
    elif per >= 70:
        return "B"
    elif per >= 60:
        return "C"
    elif per >= 50:
        return "D"
    else:
        return "F"