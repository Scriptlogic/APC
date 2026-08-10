numbers = [10, 20, 30, 40, 50]
left_rotated = numbers[1:] + numbers[:1]
print("Left Rotated:", left_rotated)

right_rotated = numbers[-1:] + numbers[:-1]
print("Right Rotated:", right_rotated)