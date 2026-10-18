class Student:

    def __init__(self, name, roll, marks):  
        self.name = name        
        self.roll = roll
        self.marks = marks

    def get_average(self):
        return sum(self.marks) / len(self.marks)

    def get_grade(self):
        avg = self.get_average()
        if avg >= 90: return "A"
        elif avg >= 75: return "B"
        elif avg >= 60: return "C"
        else: return "F"

    def print_report(self):
        print("--- Report ---")
        print(f"Name  : {self.name}")
        print(f"Roll  : {self.roll}")
        print(f"Avg   : {self.get_average():.2f}%")
        print(f"Grade : {self.get_grade()}")
        print()

s1 = Student("Yubhi", 101, [92, 88, 95])
s2 = Student("Arun",  102, [75, 80, 70])
s3 = Student("Priya", 103, [90, 75, 72])

students = [s1, s2, s3]

for student in students:
    student.print_report()

topper = max(students, key=lambda student: student.get_average())

print(f"Topper: {topper.name} with {topper.get_average():.2f}%")
