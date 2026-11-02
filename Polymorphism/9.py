class Distance:
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def __add__(self, other):
        total_feet = self.feet + other.feet
        total_inches = self.inches + other.inches

        # Normalize inches
        if total_inches >= 12:
            total_feet = total_feet + total_inches // 12
            total_inches = total_inches % 12

        return Distance(total_feet, total_inches)

    def display(self):
        print(self.feet, "feet", self.inches, "inches")


d1 = Distance(5, 8)
d2 = Distance(4, 7)

d3 = d1 + d2

print("Distance 1:")
d1.display()

print("Distance 2:")
d2.display()

print("Total Distance:")
d3.display()