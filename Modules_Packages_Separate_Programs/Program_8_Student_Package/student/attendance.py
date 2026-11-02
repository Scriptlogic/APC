# Program 8: Attendance Module

def attendance_percentage(attended, total):
    return attended / total * 100

def eligible(attended, total):
    return attendance_percentage(attended, total) >= 75
