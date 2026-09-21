class Academic:
    def __init__(self, marks):
        self.marks = marks


class Sports:
    def __init__(self, sports_points):
        self.sports_points = sports_points


class Student(Academic, Sports):
    def __init__(self, marks, sports_points):
        Academic.__init__(self, marks)
        Sports.__init__(self, sports_points)

    def calculate_performance(self):
        total = self.marks + self.sports_points
        print("Academic Marks:", self.marks)
        print("Sports Points:", self.sports_points)
        print("Overall Performance:", total)



s = Student(85, 10)

s.calculate_performance()